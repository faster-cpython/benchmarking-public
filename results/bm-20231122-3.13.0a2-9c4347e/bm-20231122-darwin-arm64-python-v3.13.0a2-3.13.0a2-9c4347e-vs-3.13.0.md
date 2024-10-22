# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a2
- machine: darwin-arm64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.01x slower
- HPT reliability: 86.33%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 172 ms: 1.03x faster                                       |
| chameleon      | 5.08 ms                                                | 4.77 ms: 1.07x faster                                      |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.01x slower                                     |
| html5lib       | 36.6 ms                                                | 35.9 ms: 1.02x faster                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_tcp                      | 457 ms                                                 | 399 ms: 1.14x faster                                       |
| coroutines                       | 19.8 ms                                                | 18.3 ms: 1.08x faster                                      |
| async_tree_eager                 | 70.5 ms                                                | 68.3 ms: 1.03x faster                                      |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 372 ms: 1.01x faster                                       |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 346 ms: 1.01x faster                                       |
| async_generators                 | 294 ms                                                 | 295 ms: 1.00x slower                                       |
| async_tree_eager_tg              | 48.4 ms                                                | 49.3 ms: 1.02x slower                                      |
| async_tree_eager_memoization     | 169 ms                                                 | 173 ms: 1.02x slower                                       |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 143 ms: 1.03x slower                                       |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.33 sec: 1.05x slower                                     |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 525 ms: 1.14x slower                                       |
| async_tree_memoization_tg        | 291 ms                                                 | 336 ms: 1.16x slower                                       |
| async_tree_none                  | 212 ms                                                 | 256 ms: 1.21x slower                                       |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 542 ms: 1.21x slower                                       |
| async_tree_memoization           | 270 ms                                                 | 334 ms: 1.23x slower                                       |
| async_tree_eager_io              | 513 ms                                                 | 676 ms: 1.32x slower                                       |
| async_tree_none_tg               | 198 ms                                                 | 270 ms: 1.36x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 654 ms: 1.37x slower                                       |
| async_tree_io_tg                 | 500 ms                                                 | 694 ms: 1.39x slower                                       |
| async_tree_io                    | 507 ms                                                 | 710 ms: 1.40x slower                                       |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.14x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 71.8 ms: 1.03x faster                                      |
| pidigits       | 284 ms                                                 | 282 ms: 1.00x faster                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 74.6 ms: 1.05x faster                                      |
| regex_effbot   | 2.63 ms                                                | 2.56 ms: 1.03x faster                                      |
| regex_v8       | 16.9 ms                                                | 17.0 ms: 1.00x slower                                      |
| regex_dna      | 148 ms                                                 | 152 ms: 1.03x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 198 us: 1.07x faster                                       |
| unpickle_pure_python | 163 us                                                 | 155 us: 1.06x faster                                       |
| xml_etree_process    | 40.9 ms                                                | 39.2 ms: 1.04x faster                                      |
| pickle_list          | 2.99 us                                                | 2.92 us: 1.02x faster                                      |
| unpickle             | 9.15 us                                                | 9.01 us: 1.02x faster                                      |
| xml_etree_generate   | 56.6 ms                                                | 55.8 ms: 1.02x faster                                      |
| tomli_loads          | 1.56 sec                                               | 1.54 sec: 1.01x faster                                     |
| pickle_dict          | 18.2 us                                                | 18.0 us: 1.01x faster                                      |
| json_loads           | 16.9 us                                                | 16.8 us: 1.01x faster                                      |
| xml_etree_parse      | 109 ms                                                 | 110 ms: 1.01x slower                                       |
| unpickle_list        | 2.93 us                                                | 2.99 us: 1.02x slower                                      |
| xml_etree_iterparse  | 74.2 ms                                                | 75.9 ms: 1.02x slower                                      |
| Geometric mean       | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (2): pickle, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 16.5 ms: 1.03x faster                                      |
| python_startup_no_site | 13.7 ms                                                | 14.7 ms: 1.08x slower                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.7 ms: 1.08x faster                                      |
| mako            | 7.68 ms                                                | 7.33 ms: 1.05x faster                                      |
| genshi_xml      | 34.4 ms                                                | 33.1 ms: 1.04x faster                                      |
| django_template | 22.2 ms                                                | 21.4 ms: 1.04x faster                                      |
| Geometric mean  | (ref)                                                  | 1.05x faster                                               |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols         | 101 us                                                 | 73.5 us: 1.37x faster                                      |
| unpack_sequence                  | 36.1 ns                                                | 27.6 ns: 1.31x faster                                      |
| asyncio_tcp                      | 457 ms                                                 | 399 ms: 1.14x faster                                       |
| create_gc_cycles                 | 803 us                                                 | 704 us: 1.14x faster                                       |
| generators                       | 31.5 ms                                                | 27.7 ms: 1.14x faster                                      |
| crypto_pyaes                     | 54.0 ms                                                | 48.0 ms: 1.13x faster                                      |
| go                               | 115 ms                                                 | 105 ms: 1.10x faster                                       |
| deltablue                        | 2.68 ms                                                | 2.45 ms: 1.09x faster                                      |
| deepcopy_memo                    | 27.2 us                                                | 24.9 us: 1.09x faster                                      |
| nqueens                          | 62.9 ms                                                | 57.8 ms: 1.09x faster                                      |
| telco                            | 4.80 ms                                                | 4.42 ms: 1.09x faster                                      |
| coroutines                       | 19.8 ms                                                | 18.3 ms: 1.08x faster                                      |
| comprehensions                   | 12.2 us                                                | 11.2 us: 1.08x faster                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 46.7 ms: 1.08x faster                                      |
| genshi_text                      | 16.9 ms                                                | 15.7 ms: 1.08x faster                                      |
| pickle_pure_python               | 213 us                                                 | 198 us: 1.07x faster                                       |
| sympy_integrate                  | 11.3 ms                                                | 10.6 ms: 1.07x faster                                      |
| pprint_pformat                   | 1.08 sec                                               | 1.01 sec: 1.07x faster                                     |
| pprint_safe_repr                 | 531 ms                                                 | 496 ms: 1.07x faster                                       |
| deepcopy_reduce                  | 2.06 us                                                | 1.93 us: 1.07x faster                                      |
| chameleon                        | 5.08 ms                                                | 4.77 ms: 1.07x faster                                      |
| sympy_str                        | 145 ms                                                 | 137 ms: 1.06x faster                                       |
| sqlglot_parse                    | 856 us                                                 | 807 us: 1.06x faster                                       |
| sympy_expand                     | 246 ms                                                 | 233 ms: 1.06x faster                                       |
| unpickle_pure_python             | 163 us                                                 | 155 us: 1.06x faster                                       |
| sympy_sum                        | 75.6 ms                                                | 71.6 ms: 1.06x faster                                      |
| deepcopy                         | 232 us                                                 | 221 us: 1.05x faster                                       |
| regex_compile                    | 78.5 ms                                                | 74.6 ms: 1.05x faster                                      |
| sqlglot_normalize                | 189 ms                                                 | 180 ms: 1.05x faster                                       |
| bench_mp_pool                    | 50.9 ms                                                | 48.5 ms: 1.05x faster                                      |
| pyflate                          | 351 ms                                                 | 335 ms: 1.05x faster                                       |
| scimark_lu                       | 76.5 ms                                                | 73.0 ms: 1.05x faster                                      |
| sqlglot_optimize                 | 34.9 ms                                                | 33.3 ms: 1.05x faster                                      |
| mako                             | 7.68 ms                                                | 7.33 ms: 1.05x faster                                      |
| spectral_norm                    | 77.3 ms                                                | 74.1 ms: 1.04x faster                                      |
| xml_etree_process                | 40.9 ms                                                | 39.2 ms: 1.04x faster                                      |
| sqlglot_transpile                | 1.02 ms                                                | 983 us: 1.04x faster                                       |
| fannkuch                         | 282 ms                                                 | 271 ms: 1.04x faster                                       |
| genshi_xml                       | 34.4 ms                                                | 33.1 ms: 1.04x faster                                      |
| bench_thread_pool                | 506 us                                                 | 487 us: 1.04x faster                                       |
| django_template                  | 22.2 ms                                                | 21.4 ms: 1.04x faster                                      |
| python_startup                   | 17.0 ms                                                | 16.5 ms: 1.03x faster                                      |
| gc_traversal                     | 2.48 ms                                                | 2.41 ms: 1.03x faster                                      |
| 2to3                             | 178 ms                                                 | 172 ms: 1.03x faster                                       |
| async_tree_eager                 | 70.5 ms                                                | 68.3 ms: 1.03x faster                                      |
| richards                         | 35.4 ms                                                | 34.4 ms: 1.03x faster                                      |
| nbody                            | 73.9 ms                                                | 71.8 ms: 1.03x faster                                      |
| regex_effbot                     | 2.63 ms                                                | 2.56 ms: 1.03x faster                                      |
| pickle_list                      | 2.99 us                                                | 2.92 us: 1.02x faster                                      |
| richards_super                   | 39.1 ms                                                | 38.3 ms: 1.02x faster                                      |
| html5lib                         | 36.6 ms                                                | 35.9 ms: 1.02x faster                                      |
| pycparser                        | 706 ms                                                 | 693 ms: 1.02x faster                                       |
| scimark_sor                      | 106 ms                                                 | 104 ms: 1.02x faster                                       |
| hexiom                           | 4.85 ms                                                | 4.77 ms: 1.02x faster                                      |
| unpickle                         | 9.15 us                                                | 9.01 us: 1.02x faster                                      |
| xml_etree_generate               | 56.6 ms                                                | 55.8 ms: 1.02x faster                                      |
| thrift                           | 466 us                                                 | 459 us: 1.01x faster                                       |
| tomli_loads                      | 1.56 sec                                               | 1.54 sec: 1.01x faster                                     |
| raytrace                         | 182 ms                                                 | 179 ms: 1.01x faster                                       |
| meteor_contest                   | 73.8 ms                                                | 72.9 ms: 1.01x faster                                      |
| pickle_dict                      | 18.2 us                                                | 18.0 us: 1.01x faster                                      |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 372 ms: 1.01x faster                                       |
| logging_simple                   | 3.57 us                                                | 3.55 us: 1.01x faster                                      |
| json_loads                       | 16.9 us                                                | 16.8 us: 1.01x faster                                      |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 346 ms: 1.01x faster                                       |
| pidigits                         | 284 ms                                                 | 282 ms: 1.00x faster                                       |
| logging_format                   | 3.85 us                                                | 3.83 us: 1.00x faster                                      |
| regex_v8                         | 16.9 ms                                                | 17.0 ms: 1.00x slower                                      |
| async_generators                 | 294 ms                                                 | 295 ms: 1.00x slower                                       |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.01x slower                                     |
| dulwich_log                      | 28.7 ms                                                | 29.1 ms: 1.01x slower                                      |
| xml_etree_parse                  | 109 ms                                                 | 110 ms: 1.01x slower                                       |
| json                             | 2.94 ms                                                | 2.99 ms: 1.02x slower                                      |
| logging_silent                   | 69.9 ns                                                | 71.1 ns: 1.02x slower                                      |
| async_tree_eager_tg              | 48.4 ms                                                | 49.3 ms: 1.02x slower                                      |
| coverage                         | 46.1 ms                                                | 47.0 ms: 1.02x slower                                      |
| unpickle_list                    | 2.93 us                                                | 2.99 us: 1.02x slower                                      |
| xml_etree_iterparse              | 74.2 ms                                                | 75.9 ms: 1.02x slower                                      |
| async_tree_eager_memoization     | 169 ms                                                 | 173 ms: 1.02x slower                                       |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 143 ms: 1.03x slower                                       |
| regex_dna                        | 148 ms                                                 | 152 ms: 1.03x slower                                       |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.10 ms: 1.04x slower                                      |
| mdp                              | 1.50 sec                                               | 1.56 sec: 1.04x slower                                     |
| bpe_tokeniser                    | 3.24 sec                                               | 3.40 sec: 1.05x slower                                     |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.33 sec: 1.05x slower                                     |
| python_startup_no_site           | 13.7 ms                                                | 14.7 ms: 1.08x slower                                      |
| sqlite_synth                     | 1.54 us                                                | 1.69 us: 1.10x slower                                      |
| pathlib                          | 22.8 ms                                                | 25.7 ms: 1.13x slower                                      |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 525 ms: 1.14x slower                                       |
| async_tree_memoization_tg        | 291 ms                                                 | 336 ms: 1.16x slower                                       |
| async_tree_none                  | 212 ms                                                 | 256 ms: 1.21x slower                                       |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 542 ms: 1.21x slower                                       |
| async_tree_memoization           | 270 ms                                                 | 334 ms: 1.23x slower                                       |
| async_tree_eager_io              | 513 ms                                                 | 676 ms: 1.32x slower                                       |
| mypy2                            | 396 ms                                                 | 523 ms: 1.32x slower                                       |
| async_tree_none_tg               | 198 ms                                                 | 270 ms: 1.36x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 654 ms: 1.37x slower                                       |
| async_tree_io_tg                 | 500 ms                                                 | 694 ms: 1.39x slower                                       |
| async_tree_io                    | 507 ms                                                 | 710 ms: 1.40x slower                                       |
| flaskblogging                    | 2.89 ms                                                | 4.13 ms: 1.43x slower                                      |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (9): pylint, scimark_fft, pickle, chaos, float, json_dumps, gunicorn, aiohttp, tornado_http
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: dask

# HPT report

- Reliability score: 86.33% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x