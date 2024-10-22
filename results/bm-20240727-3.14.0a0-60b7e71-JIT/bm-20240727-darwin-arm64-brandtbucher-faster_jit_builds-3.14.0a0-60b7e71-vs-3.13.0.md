# Results vs. 3.13.0

- fork: brandtbucher
- ref: faster_jit_builds
- machine: darwin-arm64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 176 ms: 1.01x faster                                                     |
| docutils       | 1.44 sec                                               | 1.57 sec: 1.08x slower                                                   |
| html5lib       | 36.6 ms                                                | 30.9 ms: 1.19x faster                                                    |
| Geometric mean | (ref)                                                  | 1.06x faster                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 291 ms                                                 | 226 ms: 1.28x faster                                                     |
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                                    |
| async_tree_eager_tg              | 48.4 ms                                                | 41.4 ms: 1.17x faster                                                    |
| async_tree_eager                 | 70.5 ms                                                | 61.8 ms: 1.14x faster                                                    |
| async_tree_memoization           | 270 ms                                                 | 240 ms: 1.13x faster                                                     |
| asyncio_tcp                      | 457 ms                                                 | 408 ms: 1.12x faster                                                     |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 125 ms: 1.11x faster                                                     |
| async_tree_eager_memoization     | 169 ms                                                 | 152 ms: 1.11x faster                                                     |
| async_tree_none_tg               | 198 ms                                                 | 182 ms: 1.09x faster                                                     |
| async_tree_none                  | 212 ms                                                 | 195 ms: 1.09x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                     |
| async_generators                 | 294 ms                                                 | 289 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 453 ms: 1.02x faster                                                     |
| async_tree_io                    | 507 ms                                                 | 547 ms: 1.08x slower                                                     |
| async_tree_eager_io              | 513 ms                                                 | 640 ms: 1.25x slower                                                     |
| async_tree_eager_io_tg           | 477 ms                                                 | 676 ms: 1.42x slower                                                     |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                     |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 45.9 ms: 1.22x faster                                                    |
| nbody          | 73.9 ms                                                | 63.0 ms: 1.17x faster                                                    |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.13x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 73.4 ms: 1.07x faster                                                    |
| regex_dna      | 148 ms                                                 | 150 ms: 1.02x slower                                                     |
| regex_v8       | 16.9 ms                                                | 17.3 ms: 1.02x slower                                                    |
| regex_effbot   | 2.63 ms                                                | 2.73 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                  | 1.00x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.24 sec: 1.25x faster                                                   |
| pickle_pure_python   | 213 us                                                 | 173 us: 1.23x faster                                                     |
| unpickle_pure_python | 163 us                                                 | 133 us: 1.23x faster                                                     |
| xml_etree_process    | 40.9 ms                                                | 35.4 ms: 1.15x faster                                                    |
| xml_etree_generate   | 56.6 ms                                                | 51.7 ms: 1.09x faster                                                    |
| json_dumps           | 6.56 ms                                                | 6.19 ms: 1.06x faster                                                    |
| xml_etree_iterparse  | 74.2 ms                                                | 72.7 ms: 1.02x faster                                                    |
| json_loads           | 16.9 us                                                | 17.0 us: 1.00x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 14.3 ms: 1.05x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.43 ms: 1.19x faster                                                    |
| django_template | 22.2 ms                                                | 21.3 ms: 1.04x faster                                                    |
| genshi_text     | 16.9 ms                                                | 16.5 ms: 1.02x faster                                                    |
| genshi_xml      | 34.4 ms                                                | 39.6 ms: 1.15x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                             |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.6 us: 1.64x faster                                                    |
| deepcopy                         | 232 us                                                 | 154 us: 1.51x faster                                                     |
| generators                       | 31.5 ms                                                | 21.6 ms: 1.46x faster                                                    |
| deepcopy_reduce                  | 2.06 us                                                | 1.54 us: 1.34x faster                                                    |
| async_tree_memoization_tg        | 291 ms                                                 | 226 ms: 1.28x faster                                                     |
| tomli_loads                      | 1.56 sec                                               | 1.24 sec: 1.25x faster                                                   |
| pickle_pure_python               | 213 us                                                 | 173 us: 1.23x faster                                                     |
| unpickle_pure_python             | 163 us                                                 | 133 us: 1.23x faster                                                     |
| float                            | 56.2 ms                                                | 45.9 ms: 1.22x faster                                                    |
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                                    |
| mako                             | 7.68 ms                                                | 6.43 ms: 1.19x faster                                                    |
| logging_simple                   | 3.57 us                                                | 3.00 us: 1.19x faster                                                    |
| html5lib                         | 36.6 ms                                                | 30.9 ms: 1.19x faster                                                    |
| deltablue                        | 2.68 ms                                                | 2.28 ms: 1.18x faster                                                    |
| nbody                            | 73.9 ms                                                | 63.0 ms: 1.17x faster                                                    |
| logging_format                   | 3.85 us                                                | 3.29 us: 1.17x faster                                                    |
| async_tree_eager_tg              | 48.4 ms                                                | 41.4 ms: 1.17x faster                                                    |
| richards                         | 35.4 ms                                                | 30.4 ms: 1.17x faster                                                    |
| xml_etree_process                | 40.9 ms                                                | 35.4 ms: 1.15x faster                                                    |
| spectral_norm                    | 77.3 ms                                                | 67.1 ms: 1.15x faster                                                    |
| scimark_monte_carlo              | 50.4 ms                                                | 43.9 ms: 1.15x faster                                                    |
| async_tree_eager                 | 70.5 ms                                                | 61.8 ms: 1.14x faster                                                    |
| logging_silent                   | 69.9 ns                                                | 61.4 ns: 1.14x faster                                                    |
| go                               | 115 ms                                                 | 101 ms: 1.14x faster                                                     |
| fannkuch                         | 282 ms                                                 | 248 ms: 1.14x faster                                                     |
| raytrace                         | 182 ms                                                 | 160 ms: 1.13x faster                                                     |
| richards_super                   | 39.1 ms                                                | 34.6 ms: 1.13x faster                                                    |
| pyflate                          | 351 ms                                                 | 311 ms: 1.13x faster                                                     |
| async_tree_memoization           | 270 ms                                                 | 240 ms: 1.13x faster                                                     |
| asyncio_tcp                      | 457 ms                                                 | 408 ms: 1.12x faster                                                     |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 125 ms: 1.11x faster                                                     |
| hexiom                           | 4.85 ms                                                | 4.36 ms: 1.11x faster                                                    |
| async_tree_eager_memoization     | 169 ms                                                 | 152 ms: 1.11x faster                                                     |
| scimark_fft                      | 201 ms                                                 | 182 ms: 1.10x faster                                                     |
| nqueens                          | 62.9 ms                                                | 57.1 ms: 1.10x faster                                                    |
| xml_etree_generate               | 56.6 ms                                                | 51.7 ms: 1.09x faster                                                    |
| dask                             | 255 ms                                                 | 234 ms: 1.09x faster                                                     |
| pprint_safe_repr                 | 531 ms                                                 | 487 ms: 1.09x faster                                                     |
| async_tree_none_tg               | 198 ms                                                 | 182 ms: 1.09x faster                                                     |
| async_tree_none                  | 212 ms                                                 | 195 ms: 1.09x faster                                                     |
| sqlglot_normalize                | 189 ms                                                 | 175 ms: 1.08x faster                                                     |
| bench_thread_pool                | 506 us                                                 | 470 us: 1.08x faster                                                     |
| typing_runtime_protocols         | 101 us                                                 | 93.8 us: 1.08x faster                                                    |
| pprint_pformat                   | 1.08 sec                                               | 1.00 sec: 1.08x faster                                                   |
| chaos                            | 41.3 ms                                                | 38.5 ms: 1.07x faster                                                    |
| bpe_tokeniser                    | 3.24 sec                                               | 3.03 sec: 1.07x faster                                                   |
| regex_compile                    | 78.5 ms                                                | 73.4 ms: 1.07x faster                                                    |
| telco                            | 4.80 ms                                                | 4.51 ms: 1.07x faster                                                    |
| sqlglot_optimize                 | 34.9 ms                                                | 32.8 ms: 1.06x faster                                                    |
| json_dumps                       | 6.56 ms                                                | 6.19 ms: 1.06x faster                                                    |
| thrift                           | 466 us                                                 | 440 us: 1.06x faster                                                     |
| scimark_sor                      | 106 ms                                                 | 101 ms: 1.05x faster                                                     |
| mdp                              | 1.50 sec                                               | 1.44 sec: 1.04x faster                                                   |
| sympy_str                        | 145 ms                                                 | 140 ms: 1.04x faster                                                     |
| crypto_pyaes                     | 54.0 ms                                                | 51.9 ms: 1.04x faster                                                    |
| meteor_contest                   | 73.8 ms                                                | 70.9 ms: 1.04x faster                                                    |
| django_template                  | 22.2 ms                                                | 21.3 ms: 1.04x faster                                                    |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                     |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.89 ms: 1.03x faster                                                    |
| sympy_sum                        | 75.6 ms                                                | 73.4 ms: 1.03x faster                                                    |
| sqlglot_parse                    | 856 us                                                 | 835 us: 1.03x faster                                                     |
| sympy_expand                     | 246 ms                                                 | 241 ms: 1.02x faster                                                     |
| xml_etree_iterparse              | 74.2 ms                                                | 72.7 ms: 1.02x faster                                                    |
| sqlglot_transpile                | 1.02 ms                                                | 1.00 ms: 1.02x faster                                                    |
| genshi_text                      | 16.9 ms                                                | 16.5 ms: 1.02x faster                                                    |
| async_generators                 | 294 ms                                                 | 289 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 453 ms: 1.02x faster                                                     |
| json                             | 2.94 ms                                                | 2.89 ms: 1.02x faster                                                    |
| sympy_integrate                  | 11.3 ms                                                | 11.2 ms: 1.01x faster                                                    |
| 2to3                             | 178 ms                                                 | 176 ms: 1.01x faster                                                     |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                                    |
| dulwich_log                      | 28.7 ms                                                | 28.5 ms: 1.01x faster                                                    |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                     |
| json_loads                       | 16.9 us                                                | 17.0 us: 1.00x slower                                                    |
| comprehensions                   | 12.2 us                                                | 12.3 us: 1.01x slower                                                    |
| regex_dna                        | 148 ms                                                 | 150 ms: 1.02x slower                                                     |
| regex_v8                         | 16.9 ms                                                | 17.3 ms: 1.02x slower                                                    |
| pathlib                          | 22.8 ms                                                | 23.6 ms: 1.04x slower                                                    |
| regex_effbot                     | 2.63 ms                                                | 2.73 ms: 1.04x slower                                                    |
| python_startup_no_site           | 13.7 ms                                                | 14.3 ms: 1.05x slower                                                    |
| scimark_lu                       | 76.5 ms                                                | 80.2 ms: 1.05x slower                                                    |
| async_tree_io                    | 507 ms                                                 | 547 ms: 1.08x slower                                                     |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.08x slower                                                   |
| create_gc_cycles                 | 803 us                                                 | 903 us: 1.12x slower                                                     |
| genshi_xml                       | 34.4 ms                                                | 39.6 ms: 1.15x slower                                                    |
| async_tree_eager_io              | 513 ms                                                 | 640 ms: 1.25x slower                                                     |
| async_tree_eager_io_tg           | 477 ms                                                 | 676 ms: 1.42x slower                                                     |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                     |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                                             |

Benchmark hidden because not significant (10): tornado_http, async_tree_cpu_io_mixed_tg, coverage, asyncio_tcp_ssl, python_startup, pycparser, xml_etree_parse, bench_mp_pool, async_tree_io_tg, pylint
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.98x