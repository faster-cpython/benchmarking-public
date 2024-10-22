# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a5
- machine: darwin-arm64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.00x slower
- HPT reliability: 66.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 173 ms: 1.03x faster                                       |
| chameleon      | 5.08 ms                                                | 5.13 ms: 1.01x slower                                      |
| docutils       | 1.44 sec                                               | 1.47 sec: 1.02x slower                                     |
| html5lib       | 36.6 ms                                                | 35.5 ms: 1.03x faster                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 19.2 ms: 1.03x faster                                      |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 344 ms: 1.01x faster                                       |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 141 ms: 1.02x slower                                       |
| async_tree_eager                 | 70.5 ms                                                | 72.2 ms: 1.02x slower                                      |
| async_generators                 | 294 ms                                                 | 302 ms: 1.03x slower                                       |
| async_tree_eager_memoization     | 169 ms                                                 | 175 ms: 1.04x slower                                       |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.32 sec: 1.05x slower                                     |
| async_tree_memoization_tg        | 291 ms                                                 | 323 ms: 1.11x slower                                       |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 525 ms: 1.14x slower                                       |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 531 ms: 1.19x slower                                       |
| async_tree_none                  | 212 ms                                                 | 257 ms: 1.21x slower                                       |
| async_tree_memoization           | 270 ms                                                 | 335 ms: 1.24x slower                                       |
| async_tree_none_tg               | 198 ms                                                 | 259 ms: 1.31x slower                                       |
| async_tree_eager_io              | 513 ms                                                 | 676 ms: 1.32x slower                                       |
| async_tree_io_tg                 | 500 ms                                                 | 672 ms: 1.34x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 649 ms: 1.36x slower                                       |
| async_tree_io                    | 507 ms                                                 | 710 ms: 1.40x slower                                       |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.15x slower                                               |

Benchmark hidden because not significant (3): asyncio_tcp, async_tree_eager_cpu_io_mixed, async_tree_eager_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 282 ms: 1.00x faster                                       |
| nbody          | 73.9 ms                                                | 73.7 ms: 1.00x faster                                      |
| float          | 56.2 ms                                                | 57.0 ms: 1.01x slower                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 75.1 ms: 1.04x faster                                      |
| regex_effbot   | 2.63 ms                                                | 2.56 ms: 1.03x faster                                      |
| regex_v8       | 16.9 ms                                                | 17.1 ms: 1.01x slower                                      |
| regex_dna      | 148 ms                                                 | 152 ms: 1.03x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 201 us: 1.06x faster                                       |
| unpickle_pure_python | 163 us                                                 | 157 us: 1.04x faster                                       |
| xml_etree_parse      | 109 ms                                                 | 106 ms: 1.02x faster                                       |
| xml_etree_process    | 40.9 ms                                                | 40.4 ms: 1.01x faster                                      |
| pickle_list          | 2.99 us                                                | 2.96 us: 1.01x faster                                      |
| pickle               | 7.36 us                                                | 7.31 us: 1.01x faster                                      |
| json_dumps           | 6.56 ms                                                | 6.52 ms: 1.01x faster                                      |
| pickle_dict          | 18.2 us                                                | 18.2 us: 1.00x slower                                      |
| json_loads           | 16.9 us                                                | 17.1 us: 1.01x slower                                      |
| unpickle             | 9.15 us                                                | 9.30 us: 1.02x slower                                      |
| xml_etree_iterparse  | 74.2 ms                                                | 75.9 ms: 1.02x slower                                      |
| xml_etree_generate   | 56.6 ms                                                | 58.1 ms: 1.03x slower                                      |
| unpickle_list        | 2.93 us                                                | 3.05 us: 1.04x slower                                      |
| Geometric mean       | (ref)                                                  | 1.00x faster                                               |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 12.9 ms: 1.32x faster                                      |
| python_startup_no_site | 13.7 ms                                                | 11.3 ms: 1.21x faster                                      |
| Geometric mean         | (ref)                                                  | 1.26x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.9 ms: 1.06x faster                                      |
| genshi_xml      | 34.4 ms                                                | 33.8 ms: 1.02x faster                                      |
| mako            | 7.68 ms                                                | 7.57 ms: 1.01x faster                                      |
| django_template | 22.2 ms                                                | 22.2 ms: 1.00x faster                                      |
| Geometric mean  | (ref)                                                  | 1.02x faster                                               |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols         | 101 us                                                 | 72.9 us: 1.39x faster                                      |
| python_startup                   | 17.0 ms                                                | 12.9 ms: 1.32x faster                                      |
| gunicorn                         | 1.31 ms                                                | 1.08 ms: 1.22x faster                                      |
| python_startup_no_site           | 13.7 ms                                                | 11.3 ms: 1.21x faster                                      |
| aiohttp                          | 1.26 ms                                                | 1.06 ms: 1.19x faster                                      |
| dask                             | 255 ms                                                 | 225 ms: 1.13x faster                                       |
| create_gc_cycles                 | 803 us                                                 | 710 us: 1.13x faster                                       |
| bench_mp_pool                    | 50.9 ms                                                | 45.4 ms: 1.12x faster                                      |
| crypto_pyaes                     | 54.0 ms                                                | 48.7 ms: 1.11x faster                                      |
| generators                       | 31.5 ms                                                | 28.6 ms: 1.10x faster                                      |
| deltablue                        | 2.68 ms                                                | 2.45 ms: 1.09x faster                                      |
| go                               | 115 ms                                                 | 105 ms: 1.09x faster                                       |
| sqlglot_parse                    | 856 us                                                 | 795 us: 1.08x faster                                       |
| raytrace                         | 182 ms                                                 | 171 ms: 1.06x faster                                       |
| genshi_text                      | 16.9 ms                                                | 15.9 ms: 1.06x faster                                      |
| pickle_pure_python               | 213 us                                                 | 201 us: 1.06x faster                                       |
| sqlglot_transpile                | 1.02 ms                                                | 972 us: 1.05x faster                                       |
| deepcopy_memo                    | 27.2 us                                                | 25.9 us: 1.05x faster                                      |
| regex_compile                    | 78.5 ms                                                | 75.1 ms: 1.04x faster                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 48.3 ms: 1.04x faster                                      |
| unpickle_pure_python             | 163 us                                                 | 157 us: 1.04x faster                                       |
| sympy_integrate                  | 11.3 ms                                                | 10.9 ms: 1.04x faster                                      |
| telco                            | 4.80 ms                                                | 4.63 ms: 1.04x faster                                      |
| chaos                            | 41.3 ms                                                | 39.9 ms: 1.03x faster                                      |
| html5lib                         | 36.6 ms                                                | 35.5 ms: 1.03x faster                                      |
| richards_super                   | 39.1 ms                                                | 38.0 ms: 1.03x faster                                      |
| coroutines                       | 19.8 ms                                                | 19.2 ms: 1.03x faster                                      |
| scimark_lu                       | 76.5 ms                                                | 74.3 ms: 1.03x faster                                      |
| thrift                           | 466 us                                                 | 452 us: 1.03x faster                                       |
| 2to3                             | 178 ms                                                 | 173 ms: 1.03x faster                                       |
| pyflate                          | 351 ms                                                 | 342 ms: 1.03x faster                                       |
| gc_traversal                     | 2.48 ms                                                | 2.42 ms: 1.03x faster                                      |
| fannkuch                         | 282 ms                                                 | 274 ms: 1.03x faster                                       |
| richards                         | 35.4 ms                                                | 34.5 ms: 1.03x faster                                      |
| regex_effbot                     | 2.63 ms                                                | 2.56 ms: 1.03x faster                                      |
| xml_etree_parse                  | 109 ms                                                 | 106 ms: 1.02x faster                                       |
| bench_thread_pool                | 506 us                                                 | 495 us: 1.02x faster                                       |
| sqlglot_normalize                | 189 ms                                                 | 185 ms: 1.02x faster                                       |
| sqlglot_optimize                 | 34.9 ms                                                | 34.2 ms: 1.02x faster                                      |
| logging_simple                   | 3.57 us                                                | 3.50 us: 1.02x faster                                      |
| pprint_pformat                   | 1.08 sec                                               | 1.06 sec: 1.02x faster                                     |
| spectral_norm                    | 77.3 ms                                                | 75.8 ms: 1.02x faster                                      |
| genshi_xml                       | 34.4 ms                                                | 33.8 ms: 1.02x faster                                      |
| pprint_safe_repr                 | 531 ms                                                 | 522 ms: 1.02x faster                                       |
| sympy_str                        | 145 ms                                                 | 143 ms: 1.02x faster                                       |
| logging_format                   | 3.85 us                                                | 3.80 us: 1.02x faster                                      |
| mako                             | 7.68 ms                                                | 7.57 ms: 1.01x faster                                      |
| sympy_expand                     | 246 ms                                                 | 243 ms: 1.01x faster                                       |
| deepcopy                         | 232 us                                                 | 230 us: 1.01x faster                                       |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 344 ms: 1.01x faster                                       |
| xml_etree_process                | 40.9 ms                                                | 40.4 ms: 1.01x faster                                      |
| pickle_list                      | 2.99 us                                                | 2.96 us: 1.01x faster                                      |
| comprehensions                   | 12.2 us                                                | 12.1 us: 1.01x faster                                      |
| pycparser                        | 706 ms                                                 | 700 ms: 1.01x faster                                       |
| sympy_sum                        | 75.6 ms                                                | 75.0 ms: 1.01x faster                                      |
| pickle                           | 7.36 us                                                | 7.31 us: 1.01x faster                                      |
| json_dumps                       | 6.56 ms                                                | 6.52 ms: 1.01x faster                                      |
| hexiom                           | 4.85 ms                                                | 4.83 ms: 1.01x faster                                      |
| pidigits                         | 284 ms                                                 | 282 ms: 1.00x faster                                       |
| scimark_sor                      | 106 ms                                                 | 105 ms: 1.00x faster                                       |
| nbody                            | 73.9 ms                                                | 73.7 ms: 1.00x faster                                      |
| meteor_contest                   | 73.8 ms                                                | 73.6 ms: 1.00x faster                                      |
| django_template                  | 22.2 ms                                                | 22.2 ms: 1.00x faster                                      |
| logging_silent                   | 69.9 ns                                                | 70.0 ns: 1.00x slower                                      |
| pickle_dict                      | 18.2 us                                                | 18.2 us: 1.00x slower                                      |
| regex_v8                         | 16.9 ms                                                | 17.1 ms: 1.01x slower                                      |
| chameleon                        | 5.08 ms                                                | 5.13 ms: 1.01x slower                                      |
| json_loads                       | 16.9 us                                                | 17.1 us: 1.01x slower                                      |
| float                            | 56.2 ms                                                | 57.0 ms: 1.01x slower                                      |
| docutils                         | 1.44 sec                                               | 1.47 sec: 1.02x slower                                     |
| unpickle                         | 9.15 us                                                | 9.30 us: 1.02x slower                                      |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 141 ms: 1.02x slower                                       |
| sqlite_synth                     | 1.54 us                                                | 1.57 us: 1.02x slower                                      |
| xml_etree_iterparse              | 74.2 ms                                                | 75.9 ms: 1.02x slower                                      |
| async_tree_eager                 | 70.5 ms                                                | 72.2 ms: 1.02x slower                                      |
| xml_etree_generate               | 56.6 ms                                                | 58.1 ms: 1.03x slower                                      |
| regex_dna                        | 148 ms                                                 | 152 ms: 1.03x slower                                       |
| async_generators                 | 294 ms                                                 | 302 ms: 1.03x slower                                       |
| dulwich_log                      | 28.7 ms                                                | 29.6 ms: 1.03x slower                                      |
| scimark_fft                      | 201 ms                                                 | 207 ms: 1.03x slower                                       |
| async_tree_eager_memoization     | 169 ms                                                 | 175 ms: 1.04x slower                                       |
| nqueens                          | 62.9 ms                                                | 65.2 ms: 1.04x slower                                      |
| unpickle_list                    | 2.93 us                                                | 3.05 us: 1.04x slower                                      |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.13 ms: 1.05x slower                                      |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.32 sec: 1.05x slower                                     |
| coverage                         | 46.1 ms                                                | 48.4 ms: 1.05x slower                                      |
| pathlib                          | 22.8 ms                                                | 24.8 ms: 1.09x slower                                      |
| mdp                              | 1.50 sec                                               | 1.64 sec: 1.10x slower                                     |
| async_tree_memoization_tg        | 291 ms                                                 | 323 ms: 1.11x slower                                       |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 525 ms: 1.14x slower                                       |
| mypy2                            | 396 ms                                                 | 457 ms: 1.15x slower                                       |
| flaskblogging                    | 2.89 ms                                                | 3.40 ms: 1.18x slower                                      |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 531 ms: 1.19x slower                                       |
| async_tree_none                  | 212 ms                                                 | 257 ms: 1.21x slower                                       |
| async_tree_memoization           | 270 ms                                                 | 335 ms: 1.24x slower                                       |
| async_tree_none_tg               | 198 ms                                                 | 259 ms: 1.31x slower                                       |
| async_tree_eager_io              | 513 ms                                                 | 676 ms: 1.32x slower                                       |
| async_tree_io_tg                 | 500 ms                                                 | 672 ms: 1.34x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 649 ms: 1.36x slower                                       |
| async_tree_io                    | 507 ms                                                 | 710 ms: 1.40x slower                                       |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (8): tornado_http, pylint, asyncio_tcp, tomli_loads, async_tree_eager_cpu_io_mixed, async_tree_eager_tg, deepcopy_reduce, json
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 66.57% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x