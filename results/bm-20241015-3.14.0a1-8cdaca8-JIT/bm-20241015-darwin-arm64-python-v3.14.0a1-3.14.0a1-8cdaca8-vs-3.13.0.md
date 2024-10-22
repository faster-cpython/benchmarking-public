# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: darwin-arm64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.02x faster
- HPT reliability: 99.68%
- HPT 99th percentile: 1.00x faster
- Memory change: 6.80x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 183 ms: 1.03x slower                                       |
| docutils       | 1.44 sec                                               | 1.57 sec: 1.09x slower                                     |
| html5lib       | 36.6 ms                                                | 34.2 ms: 1.07x faster                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg        | 291 ms                                                 | 234 ms: 1.24x faster                                       |
| coroutines                       | 19.8 ms                                                | 16.7 ms: 1.19x faster                                      |
| async_tree_eager_tg              | 48.4 ms                                                | 42.6 ms: 1.14x faster                                      |
| async_tree_eager_memoization     | 169 ms                                                 | 153 ms: 1.11x faster                                       |
| async_tree_eager                 | 70.5 ms                                                | 63.5 ms: 1.11x faster                                      |
| async_tree_memoization           | 270 ms                                                 | 246 ms: 1.10x faster                                       |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 130 ms: 1.06x faster                                       |
| async_tree_none                  | 212 ms                                                 | 199 ms: 1.06x faster                                       |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                       |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 363 ms: 1.03x faster                                       |
| async_generators                 | 294 ms                                                 | 292 ms: 1.01x faster                                       |
| asyncio_websockets               | 241 ms                                                 | 242 ms: 1.00x slower                                       |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.30 sec: 1.03x slower                                     |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 470 ms: 1.05x slower                                       |
| async_tree_none_tg               | 198 ms                                                 | 213 ms: 1.07x slower                                       |
| async_tree_io                    | 507 ms                                                 | 584 ms: 1.15x slower                                       |
| async_tree_io_tg                 | 500 ms                                                 | 611 ms: 1.22x slower                                       |
| async_tree_eager_io              | 513 ms                                                 | 667 ms: 1.30x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 714 ms: 1.50x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 56.2 ms                                                | 48.2 ms: 1.17x faster                                      |
| nbody          | 73.9 ms                                                | 65.3 ms: 1.13x faster                                      |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 74.8 ms: 1.05x faster                                      |
| regex_effbot   | 2.63 ms                                                | 2.61 ms: 1.01x faster                                      |
| regex_v8       | 16.9 ms                                                | 16.8 ms: 1.01x faster                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.25 sec: 1.25x faster                                     |
| unpickle_pure_python | 163 us                                                 | 132 us: 1.24x faster                                       |
| pickle_pure_python   | 213 us                                                 | 178 us: 1.19x faster                                       |
| xml_etree_process    | 40.9 ms                                                | 34.8 ms: 1.18x faster                                      |
| xml_etree_generate   | 56.6 ms                                                | 50.4 ms: 1.12x faster                                      |
| json_loads           | 16.9 us                                                | 16.5 us: 1.02x faster                                      |
| xml_etree_iterparse  | 74.2 ms                                                | 73.1 ms: 1.01x faster                                      |
| unpickle             | 9.15 us                                                | 9.02 us: 1.01x faster                                      |
| xml_etree_parse      | 109 ms                                                 | 107 ms: 1.01x faster                                       |
| pickle_list          | 2.99 us                                                | 2.95 us: 1.01x faster                                      |
| pickle               | 7.36 us                                                | 7.33 us: 1.01x faster                                      |
| unpickle_list        | 2.93 us                                                | 2.97 us: 1.01x slower                                      |
| json_dumps           | 6.56 ms                                                | 7.13 ms: 1.09x slower                                      |
| Geometric mean       | (ref)                                                  | 1.06x faster                                               |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 14.6 ms: 1.07x slower                                      |
| python_startup         | 17.0 ms                                                | 19.0 ms: 1.11x slower                                      |
| Geometric mean         | (ref)                                                  | 1.09x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.46 ms: 1.19x faster                                      |
| genshi_text     | 16.9 ms                                                | 16.6 ms: 1.01x faster                                      |
| django_template | 22.2 ms                                                | 23.0 ms: 1.03x slower                                      |
| genshi_xml      | 34.4 ms                                                | 42.3 ms: 1.23x slower                                      |
| Geometric mean  | (ref)                                                  | 1.01x slower                                               |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.8 us: 1.62x faster                                      |
| deepcopy                         | 232 us                                                 | 154 us: 1.51x faster                                       |
| deepcopy_reduce                  | 2.06 us                                                | 1.53 us: 1.35x faster                                      |
| tomli_loads                      | 1.56 sec                                               | 1.25 sec: 1.25x faster                                     |
| generators                       | 31.5 ms                                                | 25.4 ms: 1.24x faster                                      |
| async_tree_memoization_tg        | 291 ms                                                 | 234 ms: 1.24x faster                                       |
| unpickle_pure_python             | 163 us                                                 | 132 us: 1.24x faster                                       |
| scimark_sor                      | 106 ms                                                 | 86.0 ms: 1.23x faster                                      |
| pickle_pure_python               | 213 us                                                 | 178 us: 1.19x faster                                       |
| mako                             | 7.68 ms                                                | 6.46 ms: 1.19x faster                                      |
| coroutines                       | 19.8 ms                                                | 16.7 ms: 1.19x faster                                      |
| scimark_lu                       | 76.5 ms                                                | 64.6 ms: 1.18x faster                                      |
| go                               | 115 ms                                                 | 97.6 ms: 1.18x faster                                      |
| xml_etree_process                | 40.9 ms                                                | 34.8 ms: 1.18x faster                                      |
| float                            | 56.2 ms                                                | 48.2 ms: 1.17x faster                                      |
| logging_simple                   | 3.57 us                                                | 3.10 us: 1.15x faster                                      |
| async_tree_eager_tg              | 48.4 ms                                                | 42.6 ms: 1.14x faster                                      |
| nbody                            | 73.9 ms                                                | 65.3 ms: 1.13x faster                                      |
| logging_format                   | 3.85 us                                                | 3.42 us: 1.13x faster                                      |
| deltablue                        | 2.68 ms                                                | 2.38 ms: 1.12x faster                                      |
| xml_etree_generate               | 56.6 ms                                                | 50.4 ms: 1.12x faster                                      |
| spectral_norm                    | 77.3 ms                                                | 69.3 ms: 1.11x faster                                      |
| async_tree_eager_memoization     | 169 ms                                                 | 153 ms: 1.11x faster                                       |
| async_tree_eager                 | 70.5 ms                                                | 63.5 ms: 1.11x faster                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 45.5 ms: 1.11x faster                                      |
| async_tree_memoization           | 270 ms                                                 | 246 ms: 1.10x faster                                       |
| pprint_safe_repr                 | 531 ms                                                 | 483 ms: 1.10x faster                                       |
| thrift                           | 466 us                                                 | 426 us: 1.09x faster                                       |
| pprint_pformat                   | 1.08 sec                                               | 990 ms: 1.09x faster                                       |
| pyflate                          | 351 ms                                                 | 325 ms: 1.08x faster                                       |
| html5lib                         | 36.6 ms                                                | 34.2 ms: 1.07x faster                                      |
| nqueens                          | 62.9 ms                                                | 58.8 ms: 1.07x faster                                      |
| bench_thread_pool                | 506 us                                                 | 474 us: 1.07x faster                                       |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 130 ms: 1.06x faster                                       |
| bpe_tokeniser                    | 3.24 sec                                               | 3.05 sec: 1.06x faster                                     |
| raytrace                         | 182 ms                                                 | 171 ms: 1.06x faster                                       |
| async_tree_none                  | 212 ms                                                 | 199 ms: 1.06x faster                                       |
| scimark_fft                      | 201 ms                                                 | 190 ms: 1.06x faster                                       |
| coverage                         | 46.1 ms                                                | 43.8 ms: 1.05x faster                                      |
| telco                            | 4.80 ms                                                | 4.57 ms: 1.05x faster                                      |
| regex_compile                    | 78.5 ms                                                | 74.8 ms: 1.05x faster                                      |
| fannkuch                         | 282 ms                                                 | 269 ms: 1.05x faster                                       |
| pycparser                        | 706 ms                                                 | 678 ms: 1.04x faster                                       |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                       |
| typing_runtime_protocols         | 101 us                                                 | 97.8 us: 1.03x faster                                      |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 363 ms: 1.03x faster                                       |
| json_loads                       | 16.9 us                                                | 16.5 us: 1.02x faster                                      |
| pathlib                          | 22.8 ms                                                | 22.4 ms: 1.02x faster                                      |
| sqlglot_normalize                | 189 ms                                                 | 186 ms: 1.02x faster                                       |
| xml_etree_iterparse              | 74.2 ms                                                | 73.1 ms: 1.01x faster                                      |
| unpickle                         | 9.15 us                                                | 9.02 us: 1.01x faster                                      |
| xml_etree_parse                  | 109 ms                                                 | 107 ms: 1.01x faster                                       |
| genshi_text                      | 16.9 ms                                                | 16.6 ms: 1.01x faster                                      |
| pickle_list                      | 2.99 us                                                | 2.95 us: 1.01x faster                                      |
| richards_super                   | 39.1 ms                                                | 38.7 ms: 1.01x faster                                      |
| richards                         | 35.4 ms                                                | 35.0 ms: 1.01x faster                                      |
| regex_effbot                     | 2.63 ms                                                | 2.61 ms: 1.01x faster                                      |
| async_generators                 | 294 ms                                                 | 292 ms: 1.01x faster                                       |
| regex_v8                         | 16.9 ms                                                | 16.8 ms: 1.01x faster                                      |
| pickle                           | 7.36 us                                                | 7.33 us: 1.01x faster                                      |
| sqlite_synth                     | 1.54 us                                                | 1.54 us: 1.00x faster                                      |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                       |
| sympy_expand                     | 246 ms                                                 | 246 ms: 1.00x faster                                       |
| logging_silent                   | 69.9 ns                                                | 69.8 ns: 1.00x faster                                      |
| asyncio_websockets               | 241 ms                                                 | 242 ms: 1.00x slower                                       |
| chaos                            | 41.3 ms                                                | 41.5 ms: 1.01x slower                                      |
| dulwich_log                      | 28.7 ms                                                | 28.9 ms: 1.01x slower                                      |
| meteor_contest                   | 73.8 ms                                                | 74.4 ms: 1.01x slower                                      |
| unpickle_list                    | 2.93 us                                                | 2.97 us: 1.01x slower                                      |
| sqlglot_parse                    | 856 us                                                 | 875 us: 1.02x slower                                       |
| hexiom                           | 4.85 ms                                                | 4.96 ms: 1.02x slower                                      |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.30 sec: 1.03x slower                                     |
| 2to3                             | 178 ms                                                 | 183 ms: 1.03x slower                                       |
| sqlglot_transpile                | 1.02 ms                                                | 1.06 ms: 1.03x slower                                      |
| django_template                  | 22.2 ms                                                | 23.0 ms: 1.03x slower                                      |
| sympy_str                        | 145 ms                                                 | 151 ms: 1.04x slower                                       |
| mdp                              | 1.50 sec                                               | 1.56 sec: 1.04x slower                                     |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.14 ms: 1.05x slower                                      |
| sympy_sum                        | 75.6 ms                                                | 79.4 ms: 1.05x slower                                      |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 470 ms: 1.05x slower                                       |
| sqlglot_optimize                 | 34.9 ms                                                | 37.1 ms: 1.06x slower                                      |
| python_startup_no_site           | 13.7 ms                                                | 14.6 ms: 1.07x slower                                      |
| async_tree_none_tg               | 198 ms                                                 | 213 ms: 1.07x slower                                       |
| comprehensions                   | 12.2 us                                                | 13.1 us: 1.08x slower                                      |
| json_dumps                       | 6.56 ms                                                | 7.13 ms: 1.09x slower                                      |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.09x slower                                     |
| sympy_integrate                  | 11.3 ms                                                | 12.5 ms: 1.11x slower                                      |
| python_startup                   | 17.0 ms                                                | 19.0 ms: 1.11x slower                                      |
| async_tree_io                    | 507 ms                                                 | 584 ms: 1.15x slower                                       |
| pylint                           | 181 ms                                                 | 212 ms: 1.17x slower                                       |
| gc_traversal                     | 2.48 ms                                                | 2.94 ms: 1.18x slower                                      |
| bench_mp_pool                    | 50.9 ms                                                | 61.8 ms: 1.21x slower                                      |
| async_tree_io_tg                 | 500 ms                                                 | 611 ms: 1.22x slower                                       |
| genshi_xml                       | 34.4 ms                                                | 42.3 ms: 1.23x slower                                      |
| async_tree_eager_io              | 513 ms                                                 | 667 ms: 1.30x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 714 ms: 1.50x slower                                       |
| create_gc_cycles                 | 803 us                                                 | 1.30 ms: 1.62x slower                                      |
| unpack_sequence                  | 36.1 ns                                                | 76.0 ns: 2.10x slower                                      |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (7): tornado_http, async_tree_cpu_io_mixed, asyncio_tcp, json, crypto_pyaes, pickle_dict, regex_dna
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: sphinx

# HPT report

- Reliability score: 99.68% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 6.80x