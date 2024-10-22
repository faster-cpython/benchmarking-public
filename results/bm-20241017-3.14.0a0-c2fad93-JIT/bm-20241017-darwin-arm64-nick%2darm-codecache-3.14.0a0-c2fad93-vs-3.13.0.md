# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: darwin-arm64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 6.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 170 ms: 1.05x faster                                           |
| docutils       | 1.44 sec                                               | 1.50 sec: 1.04x slower                                         |
| html5lib       | 36.6 ms                                                | 32.7 ms: 1.12x faster                                          |
| Geometric mean | (ref)                                                  | 1.04x faster                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                          |
| async_tree_memoization_tg        | 291 ms                                                 | 246 ms: 1.18x faster                                           |
| async_tree_eager_tg              | 48.4 ms                                                | 41.7 ms: 1.16x faster                                          |
| async_tree_eager                 | 70.5 ms                                                | 61.9 ms: 1.14x faster                                          |
| async_tree_eager_memoization     | 169 ms                                                 | 151 ms: 1.12x faster                                           |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 129 ms: 1.08x faster                                           |
| async_tree_none                  | 212 ms                                                 | 198 ms: 1.07x faster                                           |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 335 ms: 1.04x faster                                           |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 360 ms: 1.04x faster                                           |
| async_generators                 | 294 ms                                                 | 288 ms: 1.02x faster                                           |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 460 ms: 1.03x slower                                           |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.30 sec: 1.03x slower                                         |
| async_tree_io_tg                 | 500 ms                                                 | 539 ms: 1.08x slower                                           |
| async_tree_io                    | 507 ms                                                 | 580 ms: 1.14x slower                                           |
| async_tree_eager_io              | 513 ms                                                 | 681 ms: 1.33x slower                                           |
| async_tree_eager_io_tg           | 477 ms                                                 | 703 ms: 1.47x slower                                           |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (5): asyncio_tcp, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 56.2 ms                                                | 46.2 ms: 1.22x faster                                          |
| nbody          | 73.9 ms                                                | 63.7 ms: 1.16x faster                                          |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                           |
| Geometric mean | (ref)                                                  | 1.12x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 72.0 ms: 1.09x faster                                          |
| regex_effbot   | 2.63 ms                                                | 2.63 ms: 1.00x faster                                          |
| regex_v8       | 16.9 ms                                                | 17.0 ms: 1.00x slower                                          |
| regex_dna      | 148 ms                                                 | 149 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.25 sec: 1.25x faster                                         |
| unpickle_pure_python | 163 us                                                 | 131 us: 1.24x faster                                           |
| pickle_pure_python   | 213 us                                                 | 176 us: 1.21x faster                                           |
| xml_etree_process    | 40.9 ms                                                | 33.9 ms: 1.21x faster                                          |
| xml_etree_generate   | 56.6 ms                                                | 49.5 ms: 1.14x faster                                          |
| json_dumps           | 6.56 ms                                                | 6.16 ms: 1.06x faster                                          |
| json_loads           | 16.9 us                                                | 16.4 us: 1.03x faster                                          |
| xml_etree_iterparse  | 74.2 ms                                                | 72.4 ms: 1.02x faster                                          |
| xml_etree_parse      | 109 ms                                                 | 106 ms: 1.02x faster                                           |
| pickle               | 7.36 us                                                | 7.29 us: 1.01x faster                                          |
| unpickle             | 9.15 us                                                | 9.07 us: 1.01x faster                                          |
| pickle_dict          | 18.2 us                                                | 18.6 us: 1.02x slower                                          |
| unpickle_list        | 2.93 us                                                | 3.00 us: 1.02x slower                                          |
| pickle_list          | 2.99 us                                                | 3.11 us: 1.04x slower                                          |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 14.9 ms: 1.09x slower                                          |
| python_startup         | 17.0 ms                                                | 19.2 ms: 1.13x slower                                          |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.43 ms: 1.19x faster                                          |
| genshi_text     | 16.9 ms                                                | 14.4 ms: 1.17x faster                                          |
| django_template | 22.2 ms                                                | 20.2 ms: 1.10x faster                                          |
| genshi_xml      | 34.4 ms                                                | 32.1 ms: 1.07x faster                                          |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                   |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.6 us: 1.64x faster                                          |
| deepcopy                         | 232 us                                                 | 149 us: 1.56x faster                                           |
| deepcopy_reduce                  | 2.06 us                                                | 1.49 us: 1.38x faster                                          |
| generators                       | 31.5 ms                                                | 24.2 ms: 1.30x faster                                          |
| tomli_loads                      | 1.56 sec                                               | 1.25 sec: 1.25x faster                                         |
| unpickle_pure_python             | 163 us                                                 | 131 us: 1.24x faster                                           |
| logging_silent                   | 69.9 ns                                                | 56.4 ns: 1.24x faster                                          |
| scimark_sor                      | 106 ms                                                 | 85.8 ms: 1.23x faster                                          |
| float                            | 56.2 ms                                                | 46.2 ms: 1.22x faster                                          |
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                          |
| pickle_pure_python               | 213 us                                                 | 176 us: 1.21x faster                                           |
| xml_etree_process                | 40.9 ms                                                | 33.9 ms: 1.21x faster                                          |
| go                               | 115 ms                                                 | 96.1 ms: 1.20x faster                                          |
| scimark_lu                       | 76.5 ms                                                | 64.0 ms: 1.20x faster                                          |
| mako                             | 7.68 ms                                                | 6.43 ms: 1.19x faster                                          |
| richards                         | 35.4 ms                                                | 29.9 ms: 1.18x faster                                          |
| logging_simple                   | 3.57 us                                                | 3.02 us: 1.18x faster                                          |
| async_tree_memoization_tg        | 291 ms                                                 | 246 ms: 1.18x faster                                           |
| richards_super                   | 39.1 ms                                                | 33.4 ms: 1.17x faster                                          |
| genshi_text                      | 16.9 ms                                                | 14.4 ms: 1.17x faster                                          |
| pprint_safe_repr                 | 531 ms                                                 | 456 ms: 1.16x faster                                           |
| async_tree_eager_tg              | 48.4 ms                                                | 41.7 ms: 1.16x faster                                          |
| nbody                            | 73.9 ms                                                | 63.7 ms: 1.16x faster                                          |
| deltablue                        | 2.68 ms                                                | 2.31 ms: 1.16x faster                                          |
| logging_format                   | 3.85 us                                                | 3.33 us: 1.16x faster                                          |
| xml_etree_generate               | 56.6 ms                                                | 49.5 ms: 1.14x faster                                          |
| async_tree_eager                 | 70.5 ms                                                | 61.9 ms: 1.14x faster                                          |
| pprint_pformat                   | 1.08 sec                                               | 952 ms: 1.13x faster                                           |
| scimark_monte_carlo              | 50.4 ms                                                | 44.6 ms: 1.13x faster                                          |
| spectral_norm                    | 77.3 ms                                                | 68.6 ms: 1.13x faster                                          |
| html5lib                         | 36.6 ms                                                | 32.7 ms: 1.12x faster                                          |
| async_tree_eager_memoization     | 169 ms                                                 | 151 ms: 1.12x faster                                           |
| pyflate                          | 351 ms                                                 | 314 ms: 1.12x faster                                           |
| nqueens                          | 62.9 ms                                                | 56.6 ms: 1.11x faster                                          |
| thrift                           | 466 us                                                 | 423 us: 1.10x faster                                           |
| fannkuch                         | 282 ms                                                 | 257 ms: 1.10x faster                                           |
| django_template                  | 22.2 ms                                                | 20.2 ms: 1.10x faster                                          |
| scimark_fft                      | 201 ms                                                 | 184 ms: 1.09x faster                                           |
| regex_compile                    | 78.5 ms                                                | 72.0 ms: 1.09x faster                                          |
| hexiom                           | 4.85 ms                                                | 4.47 ms: 1.09x faster                                          |
| pycparser                        | 706 ms                                                 | 650 ms: 1.09x faster                                           |
| sqlglot_normalize                | 189 ms                                                 | 174 ms: 1.08x faster                                           |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 129 ms: 1.08x faster                                           |
| async_tree_none                  | 212 ms                                                 | 198 ms: 1.07x faster                                           |
| genshi_xml                       | 34.4 ms                                                | 32.1 ms: 1.07x faster                                          |
| bench_thread_pool                | 506 us                                                 | 475 us: 1.07x faster                                           |
| json_dumps                       | 6.56 ms                                                | 6.16 ms: 1.06x faster                                          |
| typing_runtime_protocols         | 101 us                                                 | 95.0 us: 1.06x faster                                          |
| sqlglot_parse                    | 856 us                                                 | 808 us: 1.06x faster                                           |
| coverage                         | 46.1 ms                                                | 43.5 ms: 1.06x faster                                          |
| telco                            | 4.80 ms                                                | 4.56 ms: 1.05x faster                                          |
| bpe_tokeniser                    | 3.24 sec                                               | 3.08 sec: 1.05x faster                                         |
| 2to3                             | 178 ms                                                 | 170 ms: 1.05x faster                                           |
| sympy_expand                     | 246 ms                                                 | 236 ms: 1.04x faster                                           |
| sqlglot_transpile                | 1.02 ms                                                | 984 us: 1.04x faster                                           |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 335 ms: 1.04x faster                                           |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 360 ms: 1.04x faster                                           |
| chaos                            | 41.3 ms                                                | 39.8 ms: 1.04x faster                                          |
| crypto_pyaes                     | 54.0 ms                                                | 52.2 ms: 1.04x faster                                          |
| sqlglot_optimize                 | 34.9 ms                                                | 33.8 ms: 1.03x faster                                          |
| pathlib                          | 22.8 ms                                                | 22.2 ms: 1.03x faster                                          |
| json_loads                       | 16.9 us                                                | 16.4 us: 1.03x faster                                          |
| sympy_str                        | 145 ms                                                 | 142 ms: 1.02x faster                                           |
| xml_etree_iterparse              | 74.2 ms                                                | 72.4 ms: 1.02x faster                                          |
| xml_etree_parse                  | 109 ms                                                 | 106 ms: 1.02x faster                                           |
| async_generators                 | 294 ms                                                 | 288 ms: 1.02x faster                                           |
| json                             | 2.94 ms                                                | 2.89 ms: 1.02x faster                                          |
| sympy_sum                        | 75.6 ms                                                | 74.5 ms: 1.02x faster                                          |
| mdp                              | 1.50 sec                                               | 1.48 sec: 1.01x faster                                         |
| pickle                           | 7.36 us                                                | 7.29 us: 1.01x faster                                          |
| unpickle                         | 9.15 us                                                | 9.07 us: 1.01x faster                                          |
| raytrace                         | 182 ms                                                 | 180 ms: 1.01x faster                                           |
| sqlite_synth                     | 1.54 us                                                | 1.53 us: 1.01x faster                                          |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.97 ms: 1.01x faster                                          |
| dulwich_log                      | 28.7 ms                                                | 28.6 ms: 1.00x faster                                          |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                           |
| regex_effbot                     | 2.63 ms                                                | 2.63 ms: 1.00x faster                                          |
| regex_v8                         | 16.9 ms                                                | 17.0 ms: 1.00x slower                                          |
| meteor_contest                   | 73.8 ms                                                | 74.5 ms: 1.01x slower                                          |
| regex_dna                        | 148 ms                                                 | 149 ms: 1.01x slower                                           |
| comprehensions                   | 12.2 us                                                | 12.5 us: 1.02x slower                                          |
| pickle_dict                      | 18.2 us                                                | 18.6 us: 1.02x slower                                          |
| unpickle_list                    | 2.93 us                                                | 3.00 us: 1.02x slower                                          |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 460 ms: 1.03x slower                                           |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.30 sec: 1.03x slower                                         |
| docutils                         | 1.44 sec                                               | 1.50 sec: 1.04x slower                                         |
| sympy_integrate                  | 11.3 ms                                                | 11.8 ms: 1.04x slower                                          |
| pickle_list                      | 2.99 us                                                | 3.11 us: 1.04x slower                                          |
| async_tree_io_tg                 | 500 ms                                                 | 539 ms: 1.08x slower                                           |
| python_startup_no_site           | 13.7 ms                                                | 14.9 ms: 1.09x slower                                          |
| python_startup                   | 17.0 ms                                                | 19.2 ms: 1.13x slower                                          |
| async_tree_io                    | 507 ms                                                 | 580 ms: 1.14x slower                                           |
| gc_traversal                     | 2.48 ms                                                | 2.91 ms: 1.17x slower                                          |
| bench_mp_pool                    | 50.9 ms                                                | 61.0 ms: 1.20x slower                                          |
| async_tree_eager_io              | 513 ms                                                 | 681 ms: 1.33x slower                                           |
| async_tree_eager_io_tg           | 477 ms                                                 | 703 ms: 1.47x slower                                           |
| create_gc_cycles                 | 803 us                                                 | 1.29 ms: 1.61x slower                                          |
| unpack_sequence                  | 36.1 ns                                                | 75.2 ns: 2.08x slower                                          |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                   |

Benchmark hidden because not significant (7): asyncio_tcp, async_tree_memoization, tornado_http, async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_websockets, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241017-3.14.0a0-c2fad93-JIT/bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93.json: sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 6.38x