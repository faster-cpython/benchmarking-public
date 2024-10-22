# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: darwin-arm64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 159 ms: 1.12x faster                                                  |
| docutils       | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                |
| html5lib       | 36.6 ms                                                | 30.1 ms: 1.22x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.24x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 61.1 ms: 1.15x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 42.1 ms: 1.15x faster                                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 123 ms: 1.13x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 258 ms: 1.13x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 153 ms: 1.11x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 247 ms: 1.10x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 199 ms: 1.07x faster                                                  |
| async_generators                 | 294 ms                                                 | 278 ms: 1.06x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 189 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 462 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 541 ms: 1.08x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 580 ms: 1.14x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 680 ms: 1.33x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 708 ms: 1.48x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (3): asyncio_tcp, async_tree_cpu_io_mixed, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 60.0 ms: 1.23x faster                                                 |
| float          | 56.2 ms                                                | 48.7 ms: 1.16x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 67.2 ms: 1.17x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.44 ms: 1.08x faster                                                 |
| regex_v8       | 16.9 ms                                                | 16.4 ms: 1.03x faster                                                 |
| regex_dna      | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 181 us: 1.17x faster                                                  |
| unpickle_pure_python | 163 us                                                 | 140 us: 1.17x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 37.6 ms: 1.09x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                | 52.7 ms: 1.07x faster                                                 |
| tomli_loads          | 1.56 sec                                               | 1.48 sec: 1.06x faster                                                |
| json_dumps           | 6.56 ms                                                | 6.43 ms: 1.02x faster                                                 |
| pickle_list          | 2.99 us                                                | 2.94 us: 1.02x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 73.7 ms: 1.01x faster                                                 |
| pickle               | 7.36 us                                                | 7.42 us: 1.01x slower                                                 |
| pickle_dict          | 18.2 us                                                | 18.3 us: 1.01x slower                                                 |
| unpickle             | 9.15 us                                                | 9.24 us: 1.01x slower                                                 |
| xml_etree_parse      | 109 ms                                                 | 110 ms: 1.01x slower                                                  |
| json_loads           | 16.9 us                                                | 17.1 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 17.0 ms: 1.00x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 13.8 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.9 ms: 1.22x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 30.2 ms: 1.14x faster                                                 |
| django_template | 22.2 ms                                                | 20.0 ms: 1.11x faster                                                 |
| mako            | 7.68 ms                                                | 6.93 ms: 1.11x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.5 us: 1.65x faster                                                 |
| deepcopy                         | 232 us                                                 | 145 us: 1.61x faster                                                  |
| generators                       | 31.5 ms                                                | 20.5 ms: 1.53x faster                                                 |
| go                               | 115 ms                                                 | 79.2 ms: 1.45x faster                                                 |
| unpack_sequence                  | 36.1 ns                                                | 26.4 ns: 1.37x faster                                                 |
| deepcopy_reduce                  | 2.06 us                                                | 1.51 us: 1.36x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.12 ms: 1.27x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.24x faster                                                 |
| nbody                            | 73.9 ms                                                | 60.0 ms: 1.23x faster                                                 |
| html5lib                         | 36.6 ms                                                | 30.1 ms: 1.22x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 13.9 ms: 1.22x faster                                                 |
| raytrace                         | 182 ms                                                 | 149 ms: 1.21x faster                                                  |
| hexiom                           | 4.85 ms                                                | 4.05 ms: 1.20x faster                                                 |
| logging_simple                   | 3.57 us                                                | 3.02 us: 1.18x faster                                                 |
| nqueens                          | 62.9 ms                                                | 53.3 ms: 1.18x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 181 us: 1.17x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 43.1 ms: 1.17x faster                                                 |
| regex_compile                    | 78.5 ms                                                | 67.2 ms: 1.17x faster                                                 |
| unpickle_pure_python             | 163 us                                                 | 140 us: 1.17x faster                                                  |
| float                            | 56.2 ms                                                | 48.7 ms: 1.16x faster                                                 |
| pprint_safe_repr                 | 531 ms                                                 | 460 ms: 1.15x faster                                                  |
| spectral_norm                    | 77.3 ms                                                | 67.0 ms: 1.15x faster                                                 |
| chaos                            | 41.3 ms                                                | 35.8 ms: 1.15x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 61.1 ms: 1.15x faster                                                 |
| sqlglot_parse                    | 856 us                                                 | 743 us: 1.15x faster                                                  |
| logging_silent                   | 69.9 ns                                                | 60.7 ns: 1.15x faster                                                 |
| pprint_pformat                   | 1.08 sec                                               | 938 ms: 1.15x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 42.1 ms: 1.15x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.35 us: 1.15x faster                                                 |
| richards_super                   | 39.1 ms                                                | 34.2 ms: 1.15x faster                                                 |
| richards                         | 35.4 ms                                                | 31.1 ms: 1.14x faster                                                 |
| genshi_xml                       | 34.4 ms                                                | 30.2 ms: 1.14x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 93.1 ms: 1.14x faster                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 905 us: 1.13x faster                                                  |
| bench_thread_pool                | 506 us                                                 | 448 us: 1.13x faster                                                  |
| scimark_lu                       | 76.5 ms                                                | 67.8 ms: 1.13x faster                                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 123 ms: 1.13x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 258 ms: 1.13x faster                                                  |
| comprehensions                   | 12.2 us                                                | 10.9 us: 1.12x faster                                                 |
| 2to3                             | 178 ms                                                 | 159 ms: 1.12x faster                                                  |
| sqlglot_normalize                | 189 ms                                                 | 169 ms: 1.11x faster                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 31.4 ms: 1.11x faster                                                 |
| django_template                  | 22.2 ms                                                | 20.0 ms: 1.11x faster                                                 |
| mako                             | 7.68 ms                                                | 6.93 ms: 1.11x faster                                                 |
| pycparser                        | 706 ms                                                 | 637 ms: 1.11x faster                                                  |
| thrift                           | 466 us                                                 | 420 us: 1.11x faster                                                  |
| sympy_str                        | 145 ms                                                 | 131 ms: 1.11x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.2 ms: 1.11x faster                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 153 ms: 1.11x faster                                                  |
| sympy_sum                        | 75.6 ms                                                | 68.4 ms: 1.10x faster                                                 |
| async_tree_memoization           | 270 ms                                                 | 247 ms: 1.10x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 183 ms: 1.10x faster                                                  |
| pyflate                          | 351 ms                                                 | 321 ms: 1.09x faster                                                  |
| xml_etree_process                | 40.9 ms                                                | 37.6 ms: 1.09x faster                                                 |
| sympy_expand                     | 246 ms                                                 | 228 ms: 1.08x faster                                                  |
| fannkuch                         | 282 ms                                                 | 260 ms: 1.08x faster                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.77 ms: 1.08x faster                                                 |
| crypto_pyaes                     | 54.0 ms                                                | 50.1 ms: 1.08x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.44 ms: 1.08x faster                                                 |
| xml_etree_generate               | 56.6 ms                                                | 52.7 ms: 1.07x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 94.4 us: 1.07x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 199 ms: 1.07x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 27.2 ms: 1.06x faster                                                 |
| async_generators                 | 294 ms                                                 | 278 ms: 1.06x faster                                                  |
| mdp                              | 1.50 sec                                               | 1.42 sec: 1.06x faster                                                |
| tomli_loads                      | 1.56 sec                                               | 1.48 sec: 1.06x faster                                                |
| coverage                         | 46.1 ms                                                | 44.0 ms: 1.05x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 189 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                  |
| bpe_tokeniser                    | 3.24 sec                                               | 3.13 sec: 1.04x faster                                                |
| docutils                         | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                |
| regex_v8                         | 16.9 ms                                                | 16.4 ms: 1.03x faster                                                 |
| meteor_contest                   | 73.8 ms                                                | 71.8 ms: 1.03x faster                                                 |
| bench_mp_pool                    | 50.9 ms                                                | 49.7 ms: 1.02x faster                                                 |
| regex_dna                        | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| json_dumps                       | 6.56 ms                                                | 6.43 ms: 1.02x faster                                                 |
| telco                            | 4.80 ms                                                | 4.71 ms: 1.02x faster                                                 |
| pickle_list                      | 2.99 us                                                | 2.94 us: 1.02x faster                                                 |
| gc_traversal                     | 2.48 ms                                                | 2.45 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 73.7 ms: 1.01x faster                                                 |
| python_startup                   | 17.0 ms                                                | 17.0 ms: 1.00x faster                                                 |
| sqlite_synth                     | 1.54 us                                                | 1.55 us: 1.00x slower                                                 |
| pickle                           | 7.36 us                                                | 7.42 us: 1.01x slower                                                 |
| pickle_dict                      | 18.2 us                                                | 18.3 us: 1.01x slower                                                 |
| unpickle                         | 9.15 us                                                | 9.24 us: 1.01x slower                                                 |
| python_startup_no_site           | 13.7 ms                                                | 13.8 ms: 1.01x slower                                                 |
| xml_etree_parse                  | 109 ms                                                 | 110 ms: 1.01x slower                                                  |
| json_loads                       | 16.9 us                                                | 17.1 us: 1.01x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 462 ms: 1.03x slower                                                  |
| pathlib                          | 22.8 ms                                                | 23.6 ms: 1.04x slower                                                 |
| async_tree_io_tg                 | 500 ms                                                 | 541 ms: 1.08x slower                                                  |
| create_gc_cycles                 | 803 us                                                 | 895 us: 1.11x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 580 ms: 1.14x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 680 ms: 1.33x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 708 ms: 1.48x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (7): asyncio_tcp, unpickle_list, pylint, async_tree_cpu_io_mixed, json, tornado_http, asyncio_tcp_ssl
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.99x