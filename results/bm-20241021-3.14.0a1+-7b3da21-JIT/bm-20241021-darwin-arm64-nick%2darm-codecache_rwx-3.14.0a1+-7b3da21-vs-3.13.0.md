# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache_rwx
- machine: darwin-arm64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 6.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 171 ms: 1.04x faster                                                |
| docutils       | 1.44 sec                                               | 1.49 sec: 1.03x slower                                              |
| html5lib       | 36.6 ms                                                | 31.1 ms: 1.18x faster                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg        | 291 ms                                                 | 234 ms: 1.24x faster                                                |
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                               |
| async_tree_eager_tg              | 48.4 ms                                                | 42.4 ms: 1.14x faster                                               |
| async_tree_eager                 | 70.5 ms                                                | 61.8 ms: 1.14x faster                                               |
| async_tree_eager_memoization     | 169 ms                                                 | 152 ms: 1.12x faster                                                |
| async_tree_none                  | 212 ms                                                 | 198 ms: 1.07x faster                                                |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 130 ms: 1.07x faster                                                |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 335 ms: 1.04x faster                                                |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                                |
| async_generators                 | 294 ms                                                 | 291 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 468 ms: 1.05x slower                                                |
| async_tree_none_tg               | 198 ms                                                 | 212 ms: 1.07x slower                                                |
| async_tree_io                    | 507 ms                                                 | 580 ms: 1.14x slower                                                |
| async_tree_io_tg                 | 500 ms                                                 | 609 ms: 1.22x slower                                                |
| async_tree_eager_io              | 513 ms                                                 | 667 ms: 1.30x slower                                                |
| async_tree_eager_io_tg           | 477 ms                                                 | 714 ms: 1.50x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 48.1 ms: 1.17x faster                                               |
| nbody          | 73.9 ms                                                | 65.6 ms: 1.13x faster                                               |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 71.0 ms: 1.10x faster                                               |
| regex_effbot   | 2.63 ms                                                | 2.45 ms: 1.07x faster                                               |
| regex_dna      | 148 ms                                                 | 142 ms: 1.04x faster                                                |
| regex_v8       | 16.9 ms                                                | 16.6 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.23 sec: 1.26x faster                                              |
| unpickle_pure_python | 163 us                                                 | 133 us: 1.23x faster                                                |
| xml_etree_process    | 40.9 ms                                                | 34.2 ms: 1.20x faster                                               |
| pickle_pure_python   | 213 us                                                 | 179 us: 1.19x faster                                                |
| xml_etree_generate   | 56.6 ms                                                | 50.2 ms: 1.13x faster                                               |
| xml_etree_iterparse  | 74.2 ms                                                | 72.7 ms: 1.02x faster                                               |
| json_loads           | 16.9 us                                                | 16.6 us: 1.02x faster                                               |
| xml_etree_parse      | 109 ms                                                 | 108 ms: 1.01x faster                                                |
| json_dumps           | 6.56 ms                                                | 7.17 ms: 1.09x slower                                               |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 13.5 ms: 1.01x faster                                               |
| python_startup         | 17.0 ms                                                | 17.4 ms: 1.02x slower                                               |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.45 ms: 1.19x faster                                               |
| genshi_text     | 16.9 ms                                                | 14.4 ms: 1.17x faster                                               |
| django_template | 22.2 ms                                                | 20.4 ms: 1.09x faster                                               |
| genshi_xml      | 34.4 ms                                                | 32.1 ms: 1.07x faster                                               |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                        |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.7 us: 1.63x faster                                               |
| deepcopy                         | 232 us                                                 | 148 us: 1.57x faster                                                |
| deepcopy_reduce                  | 2.06 us                                                | 1.53 us: 1.34x faster                                               |
| generators                       | 31.5 ms                                                | 24.1 ms: 1.31x faster                                               |
| go                               | 115 ms                                                 | 89.9 ms: 1.28x faster                                               |
| tomli_loads                      | 1.56 sec                                               | 1.23 sec: 1.26x faster                                              |
| async_tree_memoization_tg        | 291 ms                                                 | 234 ms: 1.24x faster                                                |
| unpickle_pure_python             | 163 us                                                 | 133 us: 1.23x faster                                                |
| scimark_sor                      | 106 ms                                                 | 86.1 ms: 1.23x faster                                               |
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                               |
| xml_etree_process                | 40.9 ms                                                | 34.2 ms: 1.20x faster                                               |
| mako                             | 7.68 ms                                                | 6.45 ms: 1.19x faster                                               |
| pickle_pure_python               | 213 us                                                 | 179 us: 1.19x faster                                                |
| scimark_lu                       | 76.5 ms                                                | 65.0 ms: 1.18x faster                                               |
| html5lib                         | 36.6 ms                                                | 31.1 ms: 1.18x faster                                               |
| logging_simple                   | 3.57 us                                                | 3.04 us: 1.18x faster                                               |
| float                            | 56.2 ms                                                | 48.1 ms: 1.17x faster                                               |
| genshi_text                      | 16.9 ms                                                | 14.4 ms: 1.17x faster                                               |
| logging_format                   | 3.85 us                                                | 3.33 us: 1.16x faster                                               |
| deltablue                        | 2.68 ms                                                | 2.32 ms: 1.15x faster                                               |
| pprint_safe_repr                 | 531 ms                                                 | 460 ms: 1.15x faster                                                |
| async_tree_eager_tg              | 48.4 ms                                                | 42.4 ms: 1.14x faster                                               |
| async_tree_eager                 | 70.5 ms                                                | 61.8 ms: 1.14x faster                                               |
| richards                         | 35.4 ms                                                | 31.1 ms: 1.14x faster                                               |
| richards_super                   | 39.1 ms                                                | 34.6 ms: 1.13x faster                                               |
| xml_etree_generate               | 56.6 ms                                                | 50.2 ms: 1.13x faster                                               |
| nbody                            | 73.9 ms                                                | 65.6 ms: 1.13x faster                                               |
| pyflate                          | 351 ms                                                 | 312 ms: 1.13x faster                                                |
| raytrace                         | 182 ms                                                 | 162 ms: 1.12x faster                                                |
| async_tree_eager_memoization     | 169 ms                                                 | 152 ms: 1.12x faster                                                |
| pylint                           | 181 ms                                                 | 162 ms: 1.12x faster                                                |
| spectral_norm                    | 77.3 ms                                                | 69.3 ms: 1.11x faster                                               |
| scimark_monte_carlo              | 50.4 ms                                                | 45.3 ms: 1.11x faster                                               |
| thrift                           | 466 us                                                 | 419 us: 1.11x faster                                                |
| fannkuch                         | 282 ms                                                 | 254 ms: 1.11x faster                                                |
| pprint_pformat                   | 1.08 sec                                               | 974 ms: 1.11x faster                                                |
| regex_compile                    | 78.5 ms                                                | 71.0 ms: 1.10x faster                                               |
| sqlglot_normalize                | 189 ms                                                 | 173 ms: 1.09x faster                                                |
| django_template                  | 22.2 ms                                                | 20.4 ms: 1.09x faster                                               |
| nqueens                          | 62.9 ms                                                | 57.9 ms: 1.08x faster                                               |
| hexiom                           | 4.85 ms                                                | 4.49 ms: 1.08x faster                                               |
| bench_thread_pool                | 506 us                                                 | 469 us: 1.08x faster                                                |
| pycparser                        | 706 ms                                                 | 656 ms: 1.08x faster                                                |
| bpe_tokeniser                    | 3.24 sec                                               | 3.02 sec: 1.07x faster                                              |
| regex_effbot                     | 2.63 ms                                                | 2.45 ms: 1.07x faster                                               |
| async_tree_none                  | 212 ms                                                 | 198 ms: 1.07x faster                                                |
| genshi_xml                       | 34.4 ms                                                | 32.1 ms: 1.07x faster                                               |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 130 ms: 1.07x faster                                                |
| telco                            | 4.80 ms                                                | 4.54 ms: 1.06x faster                                               |
| coverage                         | 46.1 ms                                                | 43.7 ms: 1.06x faster                                               |
| scimark_fft                      | 201 ms                                                 | 190 ms: 1.06x faster                                                |
| typing_runtime_protocols         | 101 us                                                 | 96.8 us: 1.04x faster                                               |
| sqlglot_parse                    | 856 us                                                 | 822 us: 1.04x faster                                                |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 335 ms: 1.04x faster                                                |
| 2to3                             | 178 ms                                                 | 171 ms: 1.04x faster                                                |
| sqlglot_optimize                 | 34.9 ms                                                | 33.6 ms: 1.04x faster                                               |
| regex_dna                        | 148 ms                                                 | 142 ms: 1.04x faster                                                |
| sympy_expand                     | 246 ms                                                 | 237 ms: 1.04x faster                                                |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                                |
| json                             | 2.94 ms                                                | 2.84 ms: 1.03x faster                                               |
| sqlglot_transpile                | 1.02 ms                                                | 993 us: 1.03x faster                                                |
| chaos                            | 41.3 ms                                                | 40.3 ms: 1.02x faster                                               |
| pathlib                          | 22.8 ms                                                | 22.3 ms: 1.02x faster                                               |
| xml_etree_iterparse              | 74.2 ms                                                | 72.7 ms: 1.02x faster                                               |
| json_loads                       | 16.9 us                                                | 16.6 us: 1.02x faster                                               |
| regex_v8                         | 16.9 ms                                                | 16.6 ms: 1.02x faster                                               |
| sympy_str                        | 145 ms                                                 | 143 ms: 1.02x faster                                                |
| python_startup_no_site           | 13.7 ms                                                | 13.5 ms: 1.01x faster                                               |
| meteor_contest                   | 73.8 ms                                                | 72.9 ms: 1.01x faster                                               |
| xml_etree_parse                  | 109 ms                                                 | 108 ms: 1.01x faster                                                |
| async_generators                 | 294 ms                                                 | 291 ms: 1.01x faster                                                |
| logging_silent                   | 69.9 ns                                                | 69.4 ns: 1.01x faster                                               |
| dulwich_log                      | 28.7 ms                                                | 28.5 ms: 1.01x faster                                               |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                |
| crypto_pyaes                     | 54.0 ms                                                | 54.3 ms: 1.00x slower                                               |
| mdp                              | 1.50 sec                                               | 1.52 sec: 1.01x slower                                              |
| python_startup                   | 17.0 ms                                                | 17.4 ms: 1.02x slower                                               |
| docutils                         | 1.44 sec                                               | 1.49 sec: 1.03x slower                                              |
| sympy_integrate                  | 11.3 ms                                                | 11.8 ms: 1.04x slower                                               |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 468 ms: 1.05x slower                                                |
| comprehensions                   | 12.2 us                                                | 12.7 us: 1.05x slower                                               |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.15 ms: 1.05x slower                                               |
| async_tree_none_tg               | 198 ms                                                 | 212 ms: 1.07x slower                                                |
| json_dumps                       | 6.56 ms                                                | 7.17 ms: 1.09x slower                                               |
| async_tree_io                    | 507 ms                                                 | 580 ms: 1.14x slower                                                |
| bench_mp_pool                    | 50.9 ms                                                | 60.1 ms: 1.18x slower                                               |
| gc_traversal                     | 2.48 ms                                                | 2.95 ms: 1.19x slower                                               |
| async_tree_io_tg                 | 500 ms                                                 | 609 ms: 1.22x slower                                                |
| async_tree_eager_io              | 513 ms                                                 | 667 ms: 1.30x slower                                                |
| async_tree_eager_io_tg           | 477 ms                                                 | 714 ms: 1.50x slower                                                |
| create_gc_cycles                 | 803 us                                                 | 1.32 ms: 1.65x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (5): tornado_http, async_tree_memoization, async_tree_cpu_io_mixed, sympy_sum, asyncio_websockets
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20241021-3.14.0a1+-7b3da21-JIT/bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21.json: sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 6.25x