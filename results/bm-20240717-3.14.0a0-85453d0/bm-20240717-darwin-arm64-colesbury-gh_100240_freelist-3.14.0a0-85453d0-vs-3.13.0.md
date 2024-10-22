# Results vs. 3.13.0

- fork: colesbury
- ref: gh_100240_freelist
- machine: darwin-arm64
- commit hash: 85453d0
- commit date: 2024-07-17
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 5.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 163 ms: 1.09x faster                                                   |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                 |
| html5lib       | 36.6 ms                                                | 31.4 ms: 1.17x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.2 ms: 1.22x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 239 ms: 1.22x faster                                                   |
| async_tree_memoization           | 270 ms                                                 | 230 ms: 1.18x faster                                                   |
| async_tree_eager_tg              | 48.4 ms                                                | 42.3 ms: 1.15x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 174 ms: 1.14x faster                                                   |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 123 ms: 1.13x faster                                                   |
| async_tree_eager_memoization     | 169 ms                                                 | 150 ms: 1.13x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 192 ms: 1.10x faster                                                   |
| async_tree_eager                 | 70.5 ms                                                | 64.2 ms: 1.10x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 429 ms: 1.06x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 331 ms: 1.05x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 358 ms: 1.05x faster                                                   |
| async_generators                 | 294 ms                                                 | 283 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 450 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 444 ms: 1.01x faster                                                   |
| async_tree_io                    | 507 ms                                                 | 522 ms: 1.03x slower                                                   |
| async_tree_eager_io              | 513 ms                                                 | 707 ms: 1.38x slower                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 697 ms: 1.46x slower                                                   |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 61.7 ms: 1.20x faster                                                  |
| float          | 56.2 ms                                                | 48.6 ms: 1.16x faster                                                  |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 68.6 ms: 1.14x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.58 ms: 1.02x faster                                                  |
| regex_dna      | 148 ms                                                 | 149 ms: 1.01x slower                                                   |
| regex_v8       | 16.9 ms                                                | 17.3 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 180 us: 1.18x faster                                                   |
| unpickle_pure_python | 163 us                                                 | 143 us: 1.14x faster                                                   |
| xml_etree_process    | 40.9 ms                                                | 37.8 ms: 1.08x faster                                                  |
| xml_etree_generate   | 56.6 ms                                                | 53.2 ms: 1.06x faster                                                  |
| tomli_loads          | 1.56 sec                                               | 1.48 sec: 1.05x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 72.2 ms: 1.03x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 106 ms: 1.02x faster                                                   |
| json_dumps           | 6.56 ms                                                | 6.52 ms: 1.01x faster                                                  |
| json_loads           | 16.9 us                                                | 17.2 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 10.5 ms: 1.30x faster                                                  |
| python_startup         | 17.0 ms                                                | 13.4 ms: 1.27x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.0 ms: 1.20x faster                                                  |
| genshi_xml      | 34.4 ms                                                | 30.4 ms: 1.13x faster                                                  |
| django_template | 22.2 ms                                                | 19.8 ms: 1.12x faster                                                  |
| mako            | 7.68 ms                                                | 7.13 ms: 1.08x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.9 us: 1.61x faster                                                  |
| deepcopy                         | 232 us                                                 | 145 us: 1.60x faster                                                   |
| generators                       | 31.5 ms                                                | 22.7 ms: 1.39x faster                                                  |
| deepcopy_reduce                  | 2.06 us                                                | 1.49 us: 1.38x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 10.5 ms: 1.30x faster                                                  |
| deltablue                        | 2.68 ms                                                | 2.09 ms: 1.28x faster                                                  |
| python_startup                   | 17.0 ms                                                | 13.4 ms: 1.27x faster                                                  |
| raytrace                         | 182 ms                                                 | 148 ms: 1.22x faster                                                   |
| coroutines                       | 19.8 ms                                                | 16.2 ms: 1.22x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 239 ms: 1.22x faster                                                   |
| genshi_text                      | 16.9 ms                                                | 14.0 ms: 1.20x faster                                                  |
| nbody                            | 73.9 ms                                                | 61.7 ms: 1.20x faster                                                  |
| pickle_pure_python               | 213 us                                                 | 180 us: 1.18x faster                                                   |
| logging_simple                   | 3.57 us                                                | 3.03 us: 1.18x faster                                                  |
| hexiom                           | 4.85 ms                                                | 4.12 ms: 1.18x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 230 ms: 1.18x faster                                                   |
| logging_silent                   | 69.9 ns                                                | 59.6 ns: 1.17x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 43.2 ms: 1.17x faster                                                  |
| html5lib                         | 36.6 ms                                                | 31.4 ms: 1.17x faster                                                  |
| nqueens                          | 62.9 ms                                                | 54.0 ms: 1.16x faster                                                  |
| go                               | 115 ms                                                 | 98.9 ms: 1.16x faster                                                  |
| float                            | 56.2 ms                                                | 48.6 ms: 1.16x faster                                                  |
| chaos                            | 41.3 ms                                                | 35.7 ms: 1.16x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.33 us: 1.16x faster                                                  |
| sqlglot_parse                    | 856 us                                                 | 741 us: 1.16x faster                                                   |
| spectral_norm                    | 77.3 ms                                                | 67.2 ms: 1.15x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 42.3 ms: 1.15x faster                                                  |
| unpickle_pure_python             | 163 us                                                 | 143 us: 1.14x faster                                                   |
| regex_compile                    | 78.5 ms                                                | 68.6 ms: 1.14x faster                                                  |
| richards_super                   | 39.1 ms                                                | 34.2 ms: 1.14x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 174 ms: 1.14x faster                                                   |
| pprint_pformat                   | 1.08 sec                                               | 948 ms: 1.14x faster                                                   |
| richards                         | 35.4 ms                                                | 31.2 ms: 1.14x faster                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 902 us: 1.14x faster                                                   |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 123 ms: 1.13x faster                                                   |
| pprint_safe_repr                 | 531 ms                                                 | 468 ms: 1.13x faster                                                   |
| genshi_xml                       | 34.4 ms                                                | 30.4 ms: 1.13x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 150 ms: 1.13x faster                                                   |
| bench_thread_pool                | 506 us                                                 | 450 us: 1.12x faster                                                   |
| django_template                  | 22.2 ms                                                | 19.8 ms: 1.12x faster                                                  |
| comprehensions                   | 12.2 us                                                | 10.9 us: 1.12x faster                                                  |
| sqlglot_normalize                | 189 ms                                                 | 170 ms: 1.11x faster                                                   |
| bench_mp_pool                    | 50.9 ms                                                | 45.9 ms: 1.11x faster                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 31.6 ms: 1.11x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 192 ms: 1.10x faster                                                   |
| pycparser                        | 706 ms                                                 | 641 ms: 1.10x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 96.0 ms: 1.10x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 64.2 ms: 1.10x faster                                                  |
| pyflate                          | 351 ms                                                 | 321 ms: 1.09x faster                                                   |
| 2to3                             | 178 ms                                                 | 163 ms: 1.09x faster                                                   |
| scimark_lu                       | 76.5 ms                                                | 70.2 ms: 1.09x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.4 ms: 1.09x faster                                                  |
| sympy_str                        | 145 ms                                                 | 134 ms: 1.09x faster                                                   |
| xml_etree_process                | 40.9 ms                                                | 37.8 ms: 1.08x faster                                                  |
| mako                             | 7.68 ms                                                | 7.13 ms: 1.08x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 186 ms: 1.08x faster                                                   |
| sympy_sum                        | 75.6 ms                                                | 70.4 ms: 1.07x faster                                                  |
| thrift                           | 466 us                                                 | 434 us: 1.07x faster                                                   |
| fannkuch                         | 282 ms                                                 | 263 ms: 1.07x faster                                                   |
| crypto_pyaes                     | 54.0 ms                                                | 50.5 ms: 1.07x faster                                                  |
| xml_etree_generate               | 56.6 ms                                                | 53.2 ms: 1.06x faster                                                  |
| sympy_expand                     | 246 ms                                                 | 232 ms: 1.06x faster                                                   |
| asyncio_tcp                      | 457 ms                                                 | 429 ms: 1.06x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 95.0 us: 1.06x faster                                                  |
| tomli_loads                      | 1.56 sec                                               | 1.48 sec: 1.05x faster                                                 |
| mdp                              | 1.50 sec                                               | 1.43 sec: 1.05x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 331 ms: 1.05x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 358 ms: 1.05x faster                                                   |
| telco                            | 4.80 ms                                                | 4.58 ms: 1.05x faster                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.86 ms: 1.05x faster                                                  |
| bpe_tokeniser                    | 3.24 sec                                               | 3.11 sec: 1.04x faster                                                 |
| async_generators                 | 294 ms                                                 | 283 ms: 1.04x faster                                                   |
| meteor_contest                   | 73.8 ms                                                | 71.7 ms: 1.03x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 72.2 ms: 1.03x faster                                                  |
| xml_etree_parse                  | 109 ms                                                 | 106 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 450 ms: 1.02x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.58 ms: 1.02x faster                                                  |
| coverage                         | 46.1 ms                                                | 45.3 ms: 1.02x faster                                                  |
| gc_traversal                     | 2.48 ms                                                | 2.45 ms: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 444 ms: 1.01x faster                                                   |
| json_dumps                       | 6.56 ms                                                | 6.52 ms: 1.01x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                 |
| json                             | 2.94 ms                                                | 2.96 ms: 1.01x slower                                                  |
| regex_dna                        | 148 ms                                                 | 149 ms: 1.01x slower                                                   |
| pathlib                          | 22.8 ms                                                | 23.2 ms: 1.02x slower                                                  |
| regex_v8                         | 16.9 ms                                                | 17.3 ms: 1.02x slower                                                  |
| json_loads                       | 16.9 us                                                | 17.2 us: 1.02x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 522 ms: 1.03x slower                                                   |
| create_gc_cycles                 | 803 us                                                 | 893 us: 1.11x slower                                                   |
| async_tree_eager_io              | 513 ms                                                 | 707 ms: 1.38x slower                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 697 ms: 1.46x slower                                                   |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (4): tornado_http, pylint, asyncio_tcp_ssl, async_tree_io_tg
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 5.93x