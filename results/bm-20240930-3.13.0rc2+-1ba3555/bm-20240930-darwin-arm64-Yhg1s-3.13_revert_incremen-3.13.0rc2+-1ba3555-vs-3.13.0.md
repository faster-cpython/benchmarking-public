# Results vs. 3.13.0

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: darwin-arm64
- commit hash: 1ba3555
- commit date: 2024-09-30
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 174 ms: 1.02x faster                                                   |
| chameleon      | 5.08 ms                                                | 4.75 ms: 1.07x faster                                                  |
| docutils       | 1.44 sec                                               | 1.43 sec: 1.01x faster                                                 |
| html5lib       | 36.6 ms                                                | 34.7 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 18.5 ms: 1.07x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 45.4 ms: 1.07x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 67.6 ms: 1.04x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 135 ms: 1.03x faster                                                   |
| async_tree_eager_memoization     | 169 ms                                                 | 165 ms: 1.03x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 194 ms: 1.02x faster                                                   |
| async_tree_memoization_tg        | 291 ms                                                 | 285 ms: 1.02x faster                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 469 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 454 ms: 1.01x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 344 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 442 ms: 1.01x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 372 ms: 1.01x faster                                                   |
| async_generators                 | 294 ms                                                 | 296 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                 |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (6): async_tree_memoization, async_tree_eager_io, async_tree_io, async_tree_io_tg, async_tree_none, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 54.6 ms: 1.03x faster                                                  |
| pidigits       | 284 ms                                                 | 282 ms: 1.00x faster                                                   |
| nbody          | 73.9 ms                                                | 75.1 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 76.1 ms: 1.03x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.58 ms: 1.02x faster                                                  |
| regex_dna      | 148 ms                                                 | 149 ms: 1.01x slower                                                   |
| regex_v8       | 16.9 ms                                                | 17.4 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 163 us                                                 | 156 us: 1.05x faster                                                   |
| pickle_pure_python   | 213 us                                                 | 203 us: 1.05x faster                                                   |
| tomli_loads          | 1.56 sec                                               | 1.52 sec: 1.03x faster                                                 |
| unpickle_list        | 2.93 us                                                | 2.86 us: 1.02x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 107 ms: 1.01x faster                                                   |
| xml_etree_generate   | 56.6 ms                                                | 56.3 ms: 1.01x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 40.8 ms: 1.00x faster                                                  |
| pickle_dict          | 18.2 us                                                | 18.3 us: 1.01x slower                                                  |
| unpickle             | 9.15 us                                                | 9.21 us: 1.01x slower                                                  |
| pickle_list          | 2.99 us                                                | 3.03 us: 1.01x slower                                                  |
| pickle               | 7.36 us                                                | 7.60 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (3): xml_etree_iterparse, json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 13.2 ms: 1.03x faster                                                  |
| python_startup         | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.7 ms: 1.08x faster                                                  |
| genshi_xml      | 34.4 ms                                                | 32.7 ms: 1.05x faster                                                  |
| mako            | 7.68 ms                                                | 7.54 ms: 1.02x faster                                                  |
| django_template | 22.2 ms                                                | 22.1 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators                       | 31.5 ms                                                | 25.4 ms: 1.24x faster                                                  |
| unpack_sequence                  | 36.1 ns                                                | 31.5 ns: 1.14x faster                                                  |
| dask                             | 255 ms                                                 | 230 ms: 1.11x faster                                                   |
| deltablue                        | 2.68 ms                                                | 2.46 ms: 1.09x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 15.7 ms: 1.08x faster                                                  |
| chameleon                        | 5.08 ms                                                | 4.75 ms: 1.07x faster                                                  |
| coroutines                       | 19.8 ms                                                | 18.5 ms: 1.07x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 45.4 ms: 1.07x faster                                                  |
| spectral_norm                    | 77.3 ms                                                | 72.5 ms: 1.07x faster                                                  |
| html5lib                         | 36.6 ms                                                | 34.7 ms: 1.06x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 47.7 ms: 1.06x faster                                                  |
| bench_thread_pool                | 506 us                                                 | 479 us: 1.06x faster                                                   |
| nqueens                          | 62.9 ms                                                | 59.6 ms: 1.06x faster                                                  |
| fannkuch                         | 282 ms                                                 | 267 ms: 1.05x faster                                                   |
| deepcopy_memo                    | 27.2 us                                                | 25.9 us: 1.05x faster                                                  |
| unpickle_pure_python             | 163 us                                                 | 156 us: 1.05x faster                                                   |
| genshi_xml                       | 34.4 ms                                                | 32.7 ms: 1.05x faster                                                  |
| pickle_pure_python               | 213 us                                                 | 203 us: 1.05x faster                                                   |
| raytrace                         | 182 ms                                                 | 173 ms: 1.05x faster                                                   |
| async_tree_eager                 | 70.5 ms                                                | 67.6 ms: 1.04x faster                                                  |
| go                               | 115 ms                                                 | 110 ms: 1.04x faster                                                   |
| chaos                            | 41.3 ms                                                | 39.6 ms: 1.04x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 13.2 ms: 1.03x faster                                                  |
| hexiom                           | 4.85 ms                                                | 4.70 ms: 1.03x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 135 ms: 1.03x faster                                                   |
| regex_compile                    | 78.5 ms                                                | 76.1 ms: 1.03x faster                                                  |
| logging_simple                   | 3.57 us                                                | 3.47 us: 1.03x faster                                                  |
| float                            | 56.2 ms                                                | 54.6 ms: 1.03x faster                                                  |
| pyflate                          | 351 ms                                                 | 341 ms: 1.03x faster                                                   |
| pprint_safe_repr                 | 531 ms                                                 | 516 ms: 1.03x faster                                                   |
| logging_format                   | 3.85 us                                                | 3.75 us: 1.03x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 165 ms: 1.03x faster                                                   |
| tomli_loads                      | 1.56 sec                                               | 1.52 sec: 1.03x faster                                                 |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.92 ms: 1.03x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 1.05 sec: 1.02x faster                                                 |
| richards                         | 35.4 ms                                                | 34.6 ms: 1.02x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 103 ms: 1.02x faster                                                   |
| unpickle_list                    | 2.93 us                                                | 2.86 us: 1.02x faster                                                  |
| sqlglot_parse                    | 856 us                                                 | 838 us: 1.02x faster                                                   |
| 2to3                             | 178 ms                                                 | 174 ms: 1.02x faster                                                   |
| richards_super                   | 39.1 ms                                                | 38.4 ms: 1.02x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 194 ms: 1.02x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.58 ms: 1.02x faster                                                  |
| deepcopy_reduce                  | 2.06 us                                                | 2.02 us: 1.02x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 197 ms: 1.02x faster                                                   |
| python_startup                   | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 285 ms: 1.02x faster                                                   |
| thrift                           | 466 us                                                 | 457 us: 1.02x faster                                                   |
| mako                             | 7.68 ms                                                | 7.54 ms: 1.02x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 99.2 us: 1.02x faster                                                  |
| mdp                              | 1.50 sec                                               | 1.47 sec: 1.02x faster                                                 |
| deepcopy                         | 232 us                                                 | 228 us: 1.02x faster                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 469 ms: 1.02x faster                                                   |
| xml_etree_parse                  | 109 ms                                                 | 107 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 454 ms: 1.01x faster                                                   |
| docutils                         | 1.44 sec                                               | 1.43 sec: 1.01x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 344 ms: 1.01x faster                                                   |
| comprehensions                   | 12.2 us                                                | 12.0 us: 1.01x faster                                                  |
| pycparser                        | 706 ms                                                 | 698 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 442 ms: 1.01x faster                                                   |
| sqlglot_transpile                | 1.02 ms                                                | 1.01 ms: 1.01x faster                                                  |
| bpe_tokeniser                    | 3.24 sec                                               | 3.21 sec: 1.01x faster                                                 |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 11.2 ms: 1.01x faster                                                  |
| crypto_pyaes                     | 54.0 ms                                                | 53.6 ms: 1.01x faster                                                  |
| sympy_str                        | 145 ms                                                 | 144 ms: 1.01x faster                                                   |
| telco                            | 4.80 ms                                                | 4.77 ms: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 372 ms: 1.01x faster                                                   |
| meteor_contest                   | 73.8 ms                                                | 73.3 ms: 1.01x faster                                                  |
| django_template                  | 22.2 ms                                                | 22.1 ms: 1.01x faster                                                  |
| logging_silent                   | 69.9 ns                                                | 69.5 ns: 1.01x faster                                                  |
| sqlglot_normalize                | 189 ms                                                 | 188 ms: 1.01x faster                                                   |
| xml_etree_generate               | 56.6 ms                                                | 56.3 ms: 1.01x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 28.6 ms: 1.00x faster                                                  |
| pidigits                         | 284 ms                                                 | 282 ms: 1.00x faster                                                   |
| sqlglot_optimize                 | 34.9 ms                                                | 34.8 ms: 1.00x faster                                                  |
| xml_etree_process                | 40.9 ms                                                | 40.8 ms: 1.00x faster                                                  |
| sympy_expand                     | 246 ms                                                 | 247 ms: 1.00x slower                                                   |
| scimark_lu                       | 76.5 ms                                                | 76.9 ms: 1.01x slower                                                  |
| async_generators                 | 294 ms                                                 | 296 ms: 1.01x slower                                                   |
| create_gc_cycles                 | 803 us                                                 | 808 us: 1.01x slower                                                   |
| pickle_dict                      | 18.2 us                                                | 18.3 us: 1.01x slower                                                  |
| unpickle                         | 9.15 us                                                | 9.21 us: 1.01x slower                                                  |
| regex_dna                        | 148 ms                                                 | 149 ms: 1.01x slower                                                   |
| pickle_list                      | 2.99 us                                                | 3.03 us: 1.01x slower                                                  |
| nbody                            | 73.9 ms                                                | 75.1 ms: 1.02x slower                                                  |
| sqlite_synth                     | 1.54 us                                                | 1.57 us: 1.02x slower                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                 |
| json                             | 2.94 ms                                                | 3.01 ms: 1.02x slower                                                  |
| regex_v8                         | 16.9 ms                                                | 17.4 ms: 1.03x slower                                                  |
| pickle                           | 7.36 us                                                | 7.60 us: 1.03x slower                                                  |
| pathlib                          | 22.8 ms                                                | 24.5 ms: 1.08x slower                                                  |
| mypy2                            | 396 ms                                                 | 484 ms: 1.22x slower                                                   |
| flaskblogging                    | 2.89 ms                                                | 3.97 ms: 1.37x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (16): aiohttp, gunicorn, async_tree_memoization, pylint, async_tree_eager_io, async_tree_io, async_tree_io_tg, async_tree_none, bench_mp_pool, sympy_sum, xml_etree_iterparse, asyncio_tcp, json_loads, json_dumps, coverage, tornado_http

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.98x