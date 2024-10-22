# Results vs. 3.13.0

- fork: python
- ref: 54dd77fb8c880d7655ff
- machine: darwin-arm64
- commit hash: 54dd77f
- commit date: 2024-09-24
- overall geometric mean: 1.03x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 176 ms: 1.01x faster                                                  |
| docutils       | 1.44 sec                                               | 1.56 sec: 1.08x slower                                                |
| html5lib       | 36.6 ms                                                | 32.3 ms: 1.13x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.4 ms: 1.20x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 42.2 ms: 1.15x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 258 ms: 1.13x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 124 ms: 1.12x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 64.1 ms: 1.10x faster                                                 |
| asyncio_tcp                      | 457 ms                                                 | 420 ms: 1.09x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 249 ms: 1.09x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 156 ms: 1.08x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 188 ms: 1.06x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 201 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 363 ms: 1.03x faster                                                  |
| async_generators                 | 294 ms                                                 | 292 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 464 ms: 1.04x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 547 ms: 1.09x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 592 ms: 1.17x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 678 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 705 ms: 1.48x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 46.1 ms: 1.22x faster                                                 |
| nbody          | 73.9 ms                                                | 63.5 ms: 1.16x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| regex_compile  | 78.5 ms                                                | 75.6 ms: 1.04x faster                                                 |
| regex_v8       | 16.9 ms                                                | 16.5 ms: 1.03x faster                                                 |
| regex_dna      | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.24 sec: 1.25x faster                                                |
| unpickle_pure_python | 163 us                                                 | 131 us: 1.25x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 34.3 ms: 1.19x faster                                                 |
| pickle_pure_python   | 213 us                                                 | 179 us: 1.19x faster                                                  |
| xml_etree_generate   | 56.6 ms                                                | 51.1 ms: 1.11x faster                                                 |
| json_dumps           | 6.56 ms                                                | 6.17 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 71.7 ms: 1.03x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 106 ms: 1.03x faster                                                  |
| unpickle_list        | 2.93 us                                                | 2.89 us: 1.01x faster                                                 |
| pickle_list          | 2.99 us                                                | 2.98 us: 1.01x faster                                                 |
| pickle               | 7.36 us                                                | 7.47 us: 1.01x slower                                                 |
| unpickle             | 9.15 us                                                | 9.28 us: 1.01x slower                                                 |
| pickle_dict          | 18.2 us                                                | 18.5 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 16.9 ms: 1.01x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 13.8 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                 |
| genshi_text     | 16.9 ms                                                | 16.8 ms: 1.00x faster                                                 |
| django_template | 22.2 ms                                                | 22.8 ms: 1.03x slower                                                 |
| genshi_xml      | 34.4 ms                                                | 41.3 ms: 1.20x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.0 us: 1.70x faster                                                 |
| deepcopy                         | 232 us                                                 | 152 us: 1.53x faster                                                  |
| deepcopy_reduce                  | 2.06 us                                                | 1.51 us: 1.37x faster                                                 |
| generators                       | 31.5 ms                                                | 24.4 ms: 1.29x faster                                                 |
| tomli_loads                      | 1.56 sec                                               | 1.24 sec: 1.25x faster                                                |
| unpickle_pure_python             | 163 us                                                 | 131 us: 1.25x faster                                                  |
| float                            | 56.2 ms                                                | 46.1 ms: 1.22x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 87.3 ms: 1.21x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.4 ms: 1.20x faster                                                 |
| scimark_lu                       | 76.5 ms                                                | 63.9 ms: 1.20x faster                                                 |
| xml_etree_process                | 40.9 ms                                                | 34.3 ms: 1.19x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 179 us: 1.19x faster                                                  |
| mako                             | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                 |
| logging_simple                   | 3.57 us                                                | 3.02 us: 1.18x faster                                                 |
| nbody                            | 73.9 ms                                                | 63.5 ms: 1.16x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.31 us: 1.16x faster                                                 |
| spectral_norm                    | 77.3 ms                                                | 66.7 ms: 1.16x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 42.2 ms: 1.15x faster                                                 |
| go                               | 115 ms                                                 | 100 ms: 1.14x faster                                                  |
| deltablue                        | 2.68 ms                                                | 2.36 ms: 1.14x faster                                                 |
| html5lib                         | 36.6 ms                                                | 32.3 ms: 1.13x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 258 ms: 1.13x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 124 ms: 1.12x faster                                                  |
| logging_silent                   | 69.9 ns                                                | 62.5 ns: 1.12x faster                                                 |
| xml_etree_generate               | 56.6 ms                                                | 51.1 ms: 1.11x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 64.1 ms: 1.10x faster                                                 |
| thrift                           | 466 us                                                 | 424 us: 1.10x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 420 ms: 1.09x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 249 ms: 1.09x faster                                                  |
| nqueens                          | 62.9 ms                                                | 57.9 ms: 1.08x faster                                                 |
| scimark_fft                      | 201 ms                                                 | 185 ms: 1.08x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 156 ms: 1.08x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 93.6 us: 1.08x faster                                                 |
| bench_thread_pool                | 506 us                                                 | 470 us: 1.08x faster                                                  |
| pyflate                          | 351 ms                                                 | 327 ms: 1.07x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| json_dumps                       | 6.56 ms                                                | 6.17 ms: 1.06x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 188 ms: 1.06x faster                                                  |
| bpe_tokeniser                    | 3.24 sec                                               | 3.07 sec: 1.06x faster                                                |
| pprint_safe_repr                 | 531 ms                                                 | 504 ms: 1.05x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 201 ms: 1.05x faster                                                  |
| raytrace                         | 182 ms                                                 | 173 ms: 1.05x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 48.0 ms: 1.05x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 180 ms: 1.05x faster                                                  |
| fannkuch                         | 282 ms                                                 | 269 ms: 1.05x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 1.03 sec: 1.04x faster                                                |
| mdp                              | 1.50 sec                                               | 1.44 sec: 1.04x faster                                                |
| crypto_pyaes                     | 54.0 ms                                                | 52.0 ms: 1.04x faster                                                 |
| regex_compile                    | 78.5 ms                                                | 75.6 ms: 1.04x faster                                                 |
| coverage                         | 46.1 ms                                                | 44.4 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 71.7 ms: 1.03x faster                                                 |
| chaos                            | 41.3 ms                                                | 39.9 ms: 1.03x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 363 ms: 1.03x faster                                                  |
| pycparser                        | 706 ms                                                 | 685 ms: 1.03x faster                                                  |
| regex_v8                         | 16.9 ms                                                | 16.5 ms: 1.03x faster                                                 |
| xml_etree_parse                  | 109 ms                                                 | 106 ms: 1.03x faster                                                  |
| hexiom                           | 4.85 ms                                                | 4.73 ms: 1.03x faster                                                 |
| regex_dna                        | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| json                             | 2.94 ms                                                | 2.90 ms: 1.01x faster                                                 |
| sympy_str                        | 145 ms                                                 | 144 ms: 1.01x faster                                                  |
| unpickle_list                    | 2.93 us                                                | 2.89 us: 1.01x faster                                                 |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.96 ms: 1.01x faster                                                 |
| python_startup                   | 17.0 ms                                                | 16.9 ms: 1.01x faster                                                 |
| 2to3                             | 178 ms                                                 | 176 ms: 1.01x faster                                                  |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                                 |
| async_generators                 | 294 ms                                                 | 292 ms: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| pickle_list                      | 2.99 us                                                | 2.98 us: 1.01x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 16.8 ms: 1.00x faster                                                 |
| sympy_expand                     | 246 ms                                                 | 248 ms: 1.00x slower                                                  |
| python_startup_no_site           | 13.7 ms                                                | 13.8 ms: 1.01x slower                                                 |
| dulwich_log                      | 28.7 ms                                                | 29.0 ms: 1.01x slower                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 35.3 ms: 1.01x slower                                                 |
| pickle                           | 7.36 us                                                | 7.47 us: 1.01x slower                                                 |
| unpickle                         | 9.15 us                                                | 9.28 us: 1.01x slower                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 1.04 ms: 1.01x slower                                                 |
| meteor_contest                   | 73.8 ms                                                | 74.9 ms: 1.02x slower                                                 |
| pickle_dict                      | 18.2 us                                                | 18.5 us: 1.02x slower                                                 |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                |
| sqlite_synth                     | 1.54 us                                                | 1.58 us: 1.02x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 11.6 ms: 1.02x slower                                                 |
| django_template                  | 22.2 ms                                                | 22.8 ms: 1.03x slower                                                 |
| pathlib                          | 22.8 ms                                                | 23.6 ms: 1.04x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 464 ms: 1.04x slower                                                  |
| comprehensions                   | 12.2 us                                                | 12.7 us: 1.05x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.56 sec: 1.08x slower                                                |
| async_tree_io_tg                 | 500 ms                                                 | 547 ms: 1.09x slower                                                  |
| create_gc_cycles                 | 803 us                                                 | 905 us: 1.13x slower                                                  |
| pylint                           | 181 ms                                                 | 205 ms: 1.13x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 592 ms: 1.17x slower                                                  |
| genshi_xml                       | 34.4 ms                                                | 41.3 ms: 1.20x slower                                                 |
| richards_super                   | 39.1 ms                                                | 47.9 ms: 1.22x slower                                                 |
| richards                         | 35.4 ms                                                | 45.9 ms: 1.29x slower                                                 |
| async_tree_eager_io              | 513 ms                                                 | 678 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 705 ms: 1.48x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| unpack_sequence                  | 36.1 ns                                                | 76.0 ns: 2.11x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (7): telco, sqlglot_parse, json_loads, async_tree_cpu_io_mixed, sympy_sum, bench_mp_pool, tornado_http
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.99x