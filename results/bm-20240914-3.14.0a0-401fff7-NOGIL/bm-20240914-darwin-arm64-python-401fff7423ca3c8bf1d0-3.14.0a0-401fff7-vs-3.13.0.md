# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: darwin-arm64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.31x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 249 ms: 1.40x slower                                                  |
| docutils       | 1.44 sec                                               | 1.78 sec: 1.23x slower                                                |
| html5lib       | 36.6 ms                                                | 51.8 ms: 1.41x slower                                                 |
| tornado_http   | 77.2 ms                                                | 103 ms: 1.33x slower                                                  |
| Geometric mean | (ref)                                                  | 1.34x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp                      | 457 ms                                                 | 353 ms: 1.29x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 271 ms: 1.07x faster                                                  |
| async_tree_eager_io              | 513 ms                                                 | 498 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.24 sec: 1.02x faster                                                |
| async_tree_io_tg                 | 500 ms                                                 | 515 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 467 ms: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 370 ms: 1.06x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 399 ms: 1.07x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 541 ms: 1.07x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 494 ms: 1.07x slower                                                  |
| async_tree_none_tg               | 198 ms                                                 | 213 ms: 1.08x slower                                                  |
| async_tree_memoization           | 270 ms                                                 | 296 ms: 1.09x slower                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 188 ms: 1.11x slower                                                  |
| async_generators                 | 294 ms                                                 | 332 ms: 1.13x slower                                                  |
| async_tree_none                  | 212 ms                                                 | 239 ms: 1.13x slower                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 162 ms: 1.17x slower                                                  |
| coroutines                       | 19.8 ms                                                | 25.1 ms: 1.27x slower                                                 |
| async_tree_eager                 | 70.5 ms                                                | 107 ms: 1.53x slower                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 76.3 ms: 1.58x slower                                                 |
| asyncio_websockets               | 241 ms                                                 | 405 ms: 1.68x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.11x slower                                                          |

Benchmark hidden because not significant (1): async_tree_eager_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| float          | 56.2 ms                                                | 97.7 ms: 1.74x slower                                                 |
| nbody          | 73.9 ms                                                | 157 ms: 2.13x slower                                                  |
| Geometric mean | (ref)                                                  | 1.54x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.45 ms: 1.07x faster                                                 |
| regex_dna      | 148 ms                                                 | 139 ms: 1.06x faster                                                  |
| regex_v8       | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                 |
| regex_compile  | 78.5 ms                                                | 121 ms: 1.55x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle               | 7.36 us                                                | 7.01 us: 1.05x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 105 ms: 1.04x faster                                                  |
| pickle_list          | 2.99 us                                                | 2.89 us: 1.04x faster                                                 |
| pickle_dict          | 18.2 us                                                | 18.4 us: 1.01x slower                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 77.1 ms: 1.04x slower                                                 |
| unpickle             | 9.15 us                                                | 9.84 us: 1.08x slower                                                 |
| unpickle_list        | 2.93 us                                                | 3.22 us: 1.10x slower                                                 |
| json_loads           | 16.9 us                                                | 19.2 us: 1.14x slower                                                 |
| json_dumps           | 6.56 ms                                                | 7.92 ms: 1.21x slower                                                 |
| xml_etree_generate   | 56.6 ms                                                | 70.1 ms: 1.24x slower                                                 |
| tomli_loads          | 1.56 sec                                               | 2.03 sec: 1.31x slower                                                |
| xml_etree_process    | 40.9 ms                                                | 58.3 ms: 1.43x slower                                                 |
| unpickle_pure_python | 163 us                                                 | 265 us: 1.62x slower                                                  |
| pickle_pure_python   | 213 us                                                 | 348 us: 1.64x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.17x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 19.2 ms: 1.13x slower                                                 |
| python_startup_no_site | 13.7 ms                                                | 15.6 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 34.4 ms                                                | 50.2 ms: 1.46x slower                                                 |
| genshi_text     | 16.9 ms                                                | 25.3 ms: 1.50x slower                                                 |
| django_template | 22.2 ms                                                | 35.9 ms: 1.62x slower                                                 |
| mako            | 7.68 ms                                                | 13.5 ms: 1.75x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.58x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| sqlglot_normalize                | 189 ms                                                 | 105 ms: 1.80x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 353 ms: 1.29x faster                                                  |
| gc_traversal                     | 2.48 ms                                                | 2.06 ms: 1.21x faster                                                 |
| create_gc_cycles                 | 803 us                                                 | 699 us: 1.15x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.45 ms: 1.07x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 271 ms: 1.07x faster                                                  |
| regex_dna                        | 148 ms                                                 | 139 ms: 1.06x faster                                                  |
| pickle                           | 7.36 us                                                | 7.01 us: 1.05x faster                                                 |
| xml_etree_parse                  | 109 ms                                                 | 105 ms: 1.04x faster                                                  |
| pickle_list                      | 2.99 us                                                | 2.89 us: 1.04x faster                                                 |
| async_tree_eager_io              | 513 ms                                                 | 498 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.24 sec: 1.02x faster                                                |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| sqlite_synth                     | 1.54 us                                                | 1.54 us: 1.00x faster                                                 |
| pickle_dict                      | 18.2 us                                                | 18.4 us: 1.01x slower                                                 |
| regex_v8                         | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                 |
| async_tree_io_tg                 | 500 ms                                                 | 515 ms: 1.03x slower                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 77.1 ms: 1.04x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 467 ms: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 370 ms: 1.06x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 399 ms: 1.07x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 541 ms: 1.07x slower                                                  |
| deepcopy                         | 232 us                                                 | 249 us: 1.07x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 494 ms: 1.07x slower                                                  |
| async_tree_none_tg               | 198 ms                                                 | 213 ms: 1.08x slower                                                  |
| unpickle                         | 9.15 us                                                | 9.84 us: 1.08x slower                                                 |
| async_tree_memoization           | 270 ms                                                 | 296 ms: 1.09x slower                                                  |
| unpickle_list                    | 2.93 us                                                | 3.22 us: 1.10x slower                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 188 ms: 1.11x slower                                                  |
| generators                       | 31.5 ms                                                | 35.0 ms: 1.11x slower                                                 |
| bench_mp_pool                    | 50.9 ms                                                | 56.8 ms: 1.12x slower                                                 |
| python_startup                   | 17.0 ms                                                | 19.2 ms: 1.13x slower                                                 |
| async_generators                 | 294 ms                                                 | 332 ms: 1.13x slower                                                  |
| async_tree_none                  | 212 ms                                                 | 239 ms: 1.13x slower                                                  |
| python_startup_no_site           | 13.7 ms                                                | 15.6 ms: 1.14x slower                                                 |
| json_loads                       | 16.9 us                                                | 19.2 us: 1.14x slower                                                 |
| deepcopy_memo                    | 27.2 us                                                | 31.6 us: 1.16x slower                                                 |
| json                             | 2.94 ms                                                | 3.41 ms: 1.16x slower                                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 162 ms: 1.17x slower                                                  |
| pathlib                          | 22.8 ms                                                | 26.7 ms: 1.17x slower                                                 |
| json_dumps                       | 6.56 ms                                                | 7.92 ms: 1.21x slower                                                 |
| deepcopy_reduce                  | 2.06 us                                                | 2.49 us: 1.21x slower                                                 |
| nqueens                          | 62.9 ms                                                | 76.1 ms: 1.21x slower                                                 |
| meteor_contest                   | 73.8 ms                                                | 89.5 ms: 1.21x slower                                                 |
| pylint                           | 181 ms                                                 | 220 ms: 1.22x slower                                                  |
| mdp                              | 1.50 sec                                               | 1.84 sec: 1.23x slower                                                |
| telco                            | 4.80 ms                                                | 5.90 ms: 1.23x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.78 sec: 1.23x slower                                                |
| coverage                         | 46.1 ms                                                | 56.9 ms: 1.23x slower                                                 |
| xml_etree_generate               | 56.6 ms                                                | 70.1 ms: 1.24x slower                                                 |
| bpe_tokeniser                    | 3.24 sec                                               | 4.03 sec: 1.24x slower                                                |
| coroutines                       | 19.8 ms                                                | 25.1 ms: 1.27x slower                                                 |
| fannkuch                         | 282 ms                                                 | 358 ms: 1.27x slower                                                  |
| tomli_loads                      | 1.56 sec                                               | 2.03 sec: 1.31x slower                                                |
| pycparser                        | 706 ms                                                 | 935 ms: 1.33x slower                                                  |
| tornado_http                     | 77.2 ms                                                | 103 ms: 1.33x slower                                                  |
| scimark_fft                      | 201 ms                                                 | 274 ms: 1.37x slower                                                  |
| pyflate                          | 351 ms                                                 | 484 ms: 1.38x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 15.7 ms: 1.38x slower                                                 |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 4.19 ms: 1.40x slower                                                 |
| 2to3                             | 178 ms                                                 | 249 ms: 1.40x slower                                                  |
| html5lib                         | 36.6 ms                                                | 51.8 ms: 1.41x slower                                                 |
| xml_etree_process                | 40.9 ms                                                | 58.3 ms: 1.43x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 144 us: 1.43x slower                                                  |
| dulwich_log                      | 28.7 ms                                                | 41.2 ms: 1.43x slower                                                 |
| crypto_pyaes                     | 54.0 ms                                                | 77.8 ms: 1.44x slower                                                 |
| genshi_xml                       | 34.4 ms                                                | 50.2 ms: 1.46x slower                                                 |
| thrift                           | 466 us                                                 | 692 us: 1.49x slower                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 52.4 ms: 1.50x slower                                                 |
| genshi_text                      | 16.9 ms                                                | 25.3 ms: 1.50x slower                                                 |
| async_tree_eager                 | 70.5 ms                                                | 107 ms: 1.53x slower                                                  |
| pprint_pformat                   | 1.08 sec                                               | 1.66 sec: 1.54x slower                                                |
| pprint_safe_repr                 | 531 ms                                                 | 817 ms: 1.54x slower                                                  |
| spectral_norm                    | 77.3 ms                                                | 120 ms: 1.55x slower                                                  |
| regex_compile                    | 78.5 ms                                                | 121 ms: 1.55x slower                                                  |
| comprehensions                   | 12.2 us                                                | 18.9 us: 1.55x slower                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 76.3 ms: 1.58x slower                                                 |
| bench_thread_pool                | 506 us                                                 | 798 us: 1.58x slower                                                  |
| scimark_sor                      | 106 ms                                                 | 167 ms: 1.58x slower                                                  |
| hexiom                           | 4.85 ms                                                | 7.77 ms: 1.60x slower                                                 |
| go                               | 115 ms                                                 | 184 ms: 1.60x slower                                                  |
| richards                         | 35.4 ms                                                | 57.0 ms: 1.61x slower                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 81.1 ms: 1.61x slower                                                 |
| sympy_str                        | 145 ms                                                 | 234 ms: 1.61x slower                                                  |
| django_template                  | 22.2 ms                                                | 35.9 ms: 1.62x slower                                                 |
| unpickle_pure_python             | 163 us                                                 | 265 us: 1.62x slower                                                  |
| pickle_pure_python               | 213 us                                                 | 348 us: 1.64x slower                                                  |
| richards_super                   | 39.1 ms                                                | 65.7 ms: 1.68x slower                                                 |
| asyncio_websockets               | 241 ms                                                 | 405 ms: 1.68x slower                                                  |
| logging_simple                   | 3.57 us                                                | 6.17 us: 1.73x slower                                                 |
| float                            | 56.2 ms                                                | 97.7 ms: 1.74x slower                                                 |
| logging_format                   | 3.85 us                                                | 6.73 us: 1.75x slower                                                 |
| mako                             | 7.68 ms                                                | 13.5 ms: 1.75x slower                                                 |
| sympy_expand                     | 246 ms                                                 | 432 ms: 1.75x slower                                                  |
| chaos                            | 41.3 ms                                                | 76.0 ms: 1.84x slower                                                 |
| sympy_sum                        | 75.6 ms                                                | 140 ms: 1.85x slower                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 1.94 ms: 1.89x slower                                                 |
| logging_silent                   | 69.9 ns                                                | 137 ns: 1.96x slower                                                  |
| sqlglot_parse                    | 856 us                                                 | 1.69 ms: 1.98x slower                                                 |
| scimark_lu                       | 76.5 ms                                                | 152 ms: 1.99x slower                                                  |
| raytrace                         | 182 ms                                                 | 381 ms: 2.10x slower                                                  |
| nbody                            | 73.9 ms                                                | 157 ms: 2.13x slower                                                  |
| deltablue                        | 2.68 ms                                                | 5.74 ms: 2.14x slower                                                 |
| unpack_sequence                  | 36.1 ns                                                | 97.9 ns: 2.71x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.31x slower                                                          |

Benchmark hidden because not significant (1): async_tree_eager_io_tg
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.23x
- 95% likely to have a slowdown of 1.23x
- 99% likely to have a slowdown of 1.21x

# Memory
- memory change: 0.99x