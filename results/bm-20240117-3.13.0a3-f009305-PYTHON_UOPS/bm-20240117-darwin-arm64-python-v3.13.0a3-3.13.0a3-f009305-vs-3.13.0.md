# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a3
- machine: darwin-arm64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.01x slower
- HPT reliability: 73.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 172 ms: 1.03x faster                                       |
| chameleon      | 5.08 ms                                                | 4.93 ms: 1.03x faster                                      |
| docutils       | 1.44 sec                                               | 1.46 sec: 1.01x slower                                     |
| html5lib       | 36.6 ms                                                | 35.5 ms: 1.03x faster                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_tcp                      | 457 ms                                                 | 425 ms: 1.08x faster                                       |
| coroutines                       | 19.8 ms                                                | 18.8 ms: 1.05x faster                                      |
| async_tree_eager                 | 70.5 ms                                                | 68.6 ms: 1.03x faster                                      |
| async_tree_eager_tg              | 48.4 ms                                                | 47.5 ms: 1.02x faster                                      |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 344 ms: 1.01x faster                                       |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 372 ms: 1.01x faster                                       |
| async_generators                 | 294 ms                                                 | 297 ms: 1.01x slower                                       |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 142 ms: 1.02x slower                                       |
| async_tree_eager_memoization     | 169 ms                                                 | 174 ms: 1.03x slower                                       |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.32 sec: 1.05x slower                                     |
| async_tree_memoization_tg        | 291 ms                                                 | 324 ms: 1.11x slower                                       |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 522 ms: 1.13x slower                                       |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 532 ms: 1.19x slower                                       |
| async_tree_none                  | 212 ms                                                 | 254 ms: 1.20x slower                                       |
| async_tree_memoization           | 270 ms                                                 | 331 ms: 1.22x slower                                       |
| async_tree_none_tg               | 198 ms                                                 | 260 ms: 1.31x slower                                       |
| async_tree_eager_io              | 513 ms                                                 | 673 ms: 1.31x slower                                       |
| async_tree_io_tg                 | 500 ms                                                 | 672 ms: 1.34x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 646 ms: 1.36x slower                                       |
| async_tree_io                    | 507 ms                                                 | 706 ms: 1.39x slower                                       |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.14x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                       |
| float          | 56.2 ms                                                | 56.8 ms: 1.01x slower                                      |
| nbody          | 73.9 ms                                                | 75.5 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 73.7 ms: 1.06x faster                                      |
| regex_effbot   | 2.63 ms                                                | 2.77 ms: 1.06x slower                                      |
| regex_v8       | 16.9 ms                                                | 18.0 ms: 1.06x slower                                      |
| regex_dna      | 148 ms                                                 | 157 ms: 1.06x slower                                       |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 196 us: 1.09x faster                                       |
| unpickle_pure_python | 163 us                                                 | 153 us: 1.07x faster                                       |
| xml_etree_process    | 40.9 ms                                                | 39.9 ms: 1.02x faster                                      |
| pickle_dict          | 18.2 us                                                | 18.0 us: 1.01x faster                                      |
| xml_etree_generate   | 56.6 ms                                                | 56.2 ms: 1.01x faster                                      |
| pickle_list          | 2.99 us                                                | 2.97 us: 1.01x faster                                      |
| json_dumps           | 6.56 ms                                                | 6.55 ms: 1.00x faster                                      |
| unpickle             | 9.15 us                                                | 9.19 us: 1.00x slower                                      |
| pickle               | 7.36 us                                                | 7.42 us: 1.01x slower                                      |
| json_loads           | 16.9 us                                                | 17.1 us: 1.01x slower                                      |
| xml_etree_parse      | 109 ms                                                 | 111 ms: 1.02x slower                                       |
| xml_etree_iterparse  | 74.2 ms                                                | 77.2 ms: 1.04x slower                                      |
| unpickle_list        | 2.93 us                                                | 3.09 us: 1.05x slower                                      |
| Geometric mean       | (ref)                                                  | 1.00x faster                                               |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 16.6 ms: 1.02x faster                                      |
| python_startup_no_site | 13.7 ms                                                | 14.7 ms: 1.08x slower                                      |
| Geometric mean         | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.8 ms: 1.07x faster                                      |
| genshi_xml      | 34.4 ms                                                | 33.5 ms: 1.03x faster                                      |
| django_template | 22.2 ms                                                | 21.9 ms: 1.01x faster                                      |
| mako            | 7.68 ms                                                | 7.61 ms: 1.01x faster                                      |
| Geometric mean  | (ref)                                                  | 1.03x faster                                               |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols         | 101 us                                                 | 71.3 us: 1.42x faster                                      |
| unpack_sequence                  | 36.1 ns                                                | 28.4 ns: 1.27x faster                                      |
| create_gc_cycles                 | 803 us                                                 | 703 us: 1.14x faster                                       |
| generators                       | 31.5 ms                                                | 28.0 ms: 1.13x faster                                      |
| crypto_pyaes                     | 54.0 ms                                                | 48.4 ms: 1.12x faster                                      |
| deltablue                        | 2.68 ms                                                | 2.45 ms: 1.09x faster                                      |
| go                               | 115 ms                                                 | 105 ms: 1.09x faster                                       |
| pickle_pure_python               | 213 us                                                 | 196 us: 1.09x faster                                       |
| sqlglot_parse                    | 856 us                                                 | 790 us: 1.08x faster                                       |
| asyncio_tcp                      | 457 ms                                                 | 425 ms: 1.08x faster                                       |
| genshi_text                      | 16.9 ms                                                | 15.8 ms: 1.07x faster                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 47.3 ms: 1.07x faster                                      |
| unpickle_pure_python             | 163 us                                                 | 153 us: 1.07x faster                                       |
| regex_compile                    | 78.5 ms                                                | 73.7 ms: 1.06x faster                                      |
| richards                         | 35.4 ms                                                | 33.3 ms: 1.06x faster                                      |
| hexiom                           | 4.85 ms                                                | 4.56 ms: 1.06x faster                                      |
| sqlglot_transpile                | 1.02 ms                                                | 966 us: 1.06x faster                                       |
| raytrace                         | 182 ms                                                 | 172 ms: 1.06x faster                                       |
| deepcopy_memo                    | 27.2 us                                                | 25.8 us: 1.06x faster                                      |
| richards_super                   | 39.1 ms                                                | 37.1 ms: 1.06x faster                                      |
| coroutines                       | 19.8 ms                                                | 18.8 ms: 1.05x faster                                      |
| bench_mp_pool                    | 50.9 ms                                                | 48.4 ms: 1.05x faster                                      |
| sympy_integrate                  | 11.3 ms                                                | 10.8 ms: 1.05x faster                                      |
| telco                            | 4.80 ms                                                | 4.58 ms: 1.05x faster                                      |
| nqueens                          | 62.9 ms                                                | 60.1 ms: 1.05x faster                                      |
| sympy_str                        | 145 ms                                                 | 140 ms: 1.04x faster                                       |
| sqlglot_normalize                | 189 ms                                                 | 182 ms: 1.04x faster                                       |
| sqlglot_optimize                 | 34.9 ms                                                | 33.7 ms: 1.04x faster                                      |
| sympy_sum                        | 75.6 ms                                                | 72.9 ms: 1.04x faster                                      |
| chaos                            | 41.3 ms                                                | 39.8 ms: 1.04x faster                                      |
| sympy_expand                     | 246 ms                                                 | 238 ms: 1.04x faster                                       |
| fannkuch                         | 282 ms                                                 | 272 ms: 1.03x faster                                       |
| pyflate                          | 351 ms                                                 | 340 ms: 1.03x faster                                       |
| gc_traversal                     | 2.48 ms                                                | 2.40 ms: 1.03x faster                                      |
| html5lib                         | 36.6 ms                                                | 35.5 ms: 1.03x faster                                      |
| 2to3                             | 178 ms                                                 | 172 ms: 1.03x faster                                       |
| scimark_lu                       | 76.5 ms                                                | 74.2 ms: 1.03x faster                                      |
| chameleon                        | 5.08 ms                                                | 4.93 ms: 1.03x faster                                      |
| pprint_pformat                   | 1.08 sec                                               | 1.05 sec: 1.03x faster                                     |
| pprint_safe_repr                 | 531 ms                                                 | 516 ms: 1.03x faster                                       |
| mypy2                            | 396 ms                                                 | 385 ms: 1.03x faster                                       |
| bench_thread_pool                | 506 us                                                 | 492 us: 1.03x faster                                       |
| async_tree_eager                 | 70.5 ms                                                | 68.6 ms: 1.03x faster                                      |
| deepcopy_reduce                  | 2.06 us                                                | 2.00 us: 1.03x faster                                      |
| genshi_xml                       | 34.4 ms                                                | 33.5 ms: 1.03x faster                                      |
| logging_simple                   | 3.57 us                                                | 3.48 us: 1.03x faster                                      |
| meteor_contest                   | 73.8 ms                                                | 72.0 ms: 1.02x faster                                      |
| python_startup                   | 17.0 ms                                                | 16.6 ms: 1.02x faster                                      |
| xml_etree_process                | 40.9 ms                                                | 39.9 ms: 1.02x faster                                      |
| deepcopy                         | 232 us                                                 | 227 us: 1.02x faster                                       |
| logging_format                   | 3.85 us                                                | 3.78 us: 1.02x faster                                      |
| async_tree_eager_tg              | 48.4 ms                                                | 47.5 ms: 1.02x faster                                      |
| pycparser                        | 706 ms                                                 | 695 ms: 1.01x faster                                       |
| thrift                           | 466 us                                                 | 460 us: 1.01x faster                                       |
| django_template                  | 22.2 ms                                                | 21.9 ms: 1.01x faster                                      |
| spectral_norm                    | 77.3 ms                                                | 76.3 ms: 1.01x faster                                      |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 344 ms: 1.01x faster                                       |
| pickle_dict                      | 18.2 us                                                | 18.0 us: 1.01x faster                                      |
| mako                             | 7.68 ms                                                | 7.61 ms: 1.01x faster                                      |
| comprehensions                   | 12.2 us                                                | 12.1 us: 1.01x faster                                      |
| xml_etree_generate               | 56.6 ms                                                | 56.2 ms: 1.01x faster                                      |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 372 ms: 1.01x faster                                       |
| pickle_list                      | 2.99 us                                                | 2.97 us: 1.01x faster                                      |
| scimark_sor                      | 106 ms                                                 | 105 ms: 1.01x faster                                       |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                       |
| json_dumps                       | 6.56 ms                                                | 6.55 ms: 1.00x faster                                      |
| logging_silent                   | 69.9 ns                                                | 70.2 ns: 1.00x slower                                      |
| unpickle                         | 9.15 us                                                | 9.19 us: 1.00x slower                                      |
| json                             | 2.94 ms                                                | 2.96 ms: 1.01x slower                                      |
| pickle                           | 7.36 us                                                | 7.42 us: 1.01x slower                                      |
| async_generators                 | 294 ms                                                 | 297 ms: 1.01x slower                                       |
| float                            | 56.2 ms                                                | 56.8 ms: 1.01x slower                                      |
| json_loads                       | 16.9 us                                                | 17.1 us: 1.01x slower                                      |
| docutils                         | 1.44 sec                                               | 1.46 sec: 1.01x slower                                     |
| scimark_fft                      | 201 ms                                                 | 204 ms: 1.01x slower                                       |
| dulwich_log                      | 28.7 ms                                                | 29.2 ms: 1.02x slower                                      |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 142 ms: 1.02x slower                                       |
| xml_etree_parse                  | 109 ms                                                 | 111 ms: 1.02x slower                                       |
| nbody                            | 73.9 ms                                                | 75.5 ms: 1.02x slower                                      |
| async_tree_eager_memoization     | 169 ms                                                 | 174 ms: 1.03x slower                                       |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.10 ms: 1.04x slower                                      |
| coverage                         | 46.1 ms                                                | 47.8 ms: 1.04x slower                                      |
| sqlite_synth                     | 1.54 us                                                | 1.60 us: 1.04x slower                                      |
| xml_etree_iterparse              | 74.2 ms                                                | 77.2 ms: 1.04x slower                                      |
| mdp                              | 1.50 sec                                               | 1.56 sec: 1.04x slower                                     |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.32 sec: 1.05x slower                                     |
| unpickle_list                    | 2.93 us                                                | 3.09 us: 1.05x slower                                      |
| regex_effbot                     | 2.63 ms                                                | 2.77 ms: 1.06x slower                                      |
| bpe_tokeniser                    | 3.24 sec                                               | 3.44 sec: 1.06x slower                                     |
| regex_v8                         | 16.9 ms                                                | 18.0 ms: 1.06x slower                                      |
| regex_dna                        | 148 ms                                                 | 157 ms: 1.06x slower                                       |
| python_startup_no_site           | 13.7 ms                                                | 14.7 ms: 1.08x slower                                      |
| pathlib                          | 22.8 ms                                                | 24.8 ms: 1.09x slower                                      |
| async_tree_memoization_tg        | 291 ms                                                 | 324 ms: 1.11x slower                                       |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 522 ms: 1.13x slower                                       |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 532 ms: 1.19x slower                                       |
| async_tree_none                  | 212 ms                                                 | 254 ms: 1.20x slower                                       |
| async_tree_memoization           | 270 ms                                                 | 331 ms: 1.22x slower                                       |
| async_tree_none_tg               | 198 ms                                                 | 260 ms: 1.31x slower                                       |
| async_tree_eager_io              | 513 ms                                                 | 673 ms: 1.31x slower                                       |
| async_tree_io_tg                 | 500 ms                                                 | 672 ms: 1.34x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 646 ms: 1.36x slower                                       |
| async_tree_io                    | 507 ms                                                 | 706 ms: 1.39x slower                                       |
| flaskblogging                    | 2.89 ms                                                | 4.12 ms: 1.43x slower                                      |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (5): pylint, tomli_loads, gunicorn, aiohttp, tornado_http
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: dask

# HPT report

- Reliability score: 73.50% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x