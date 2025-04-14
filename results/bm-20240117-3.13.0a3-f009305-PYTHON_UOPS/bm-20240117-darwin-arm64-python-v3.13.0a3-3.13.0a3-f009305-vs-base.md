# Results vs. base

- fork: python
- ref: v3.13.0a3
- machine: darwin-arm64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.001x slower
- HPT reliability: 64.94%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240117-3.13.0a3-f009305/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| 2to3           | 170 ms                                                                                               | 172 ms: 1.01x slower                                                                                             |
| chameleon      | 4.87 ms                                                                                              | 4.93 ms: 1.01x slower                                                                                            |
| Geometric mean | (ref)                                                                                                | 1.03x slower                                                                                                     |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20240117-3.13.0a3-f009305/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| async_tree_io                    | 703 ms                                                                                               | 706 ms: 1.00x slower                                                                                             |
| async_tree_eager_tg              | 47.2 ms                                                                                              | 47.5 ms: 1.01x slower                                                                                            |
| async_tree_eager_cpu_io_mixed    | 370 ms                                                                                               | 372 ms: 1.01x slower                                                                                             |
| async_tree_eager_cpu_io_mixed_tg | 342 ms                                                                                               | 344 ms: 1.01x slower                                                                                             |
| async_tree_eager_memoization     | 173 ms                                                                                               | 174 ms: 1.01x slower                                                                                             |
| async_tree_eager_memoization_tg  | 140 ms                                                                                               | 142 ms: 1.01x slower                                                                                             |
| Geometric mean                   | (ref)                                                                                                | 1.00x slower                                                                                                     |

Benchmark hidden because not significant (10): async_tree_memoization_tg, async_tree_eager, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_eager_io_tg, async_tree_none, async_tree_eager_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240117-3.13.0a3-f009305/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| pidigits       | 282 ms                                                                                               | 282 ms: 1.00x faster                                                                                             |
| Geometric mean | (ref)                                                                                                | 1.00x faster                                                                                                     |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240117-3.13.0a3-f009305/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 2.77 ms                                                                                              | 2.77 ms: 1.00x slower                                                                                            |
| Geometric mean | (ref)                                                                                                | 1.00x slower                                                                                                     |

Benchmark hidden because not significant (3): regex_compile, regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240117-3.13.0a3-f009305/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| unpickle             | 9.29 us                                                                                              | 9.19 us: 1.01x faster                                                                                            |
| pickle_pure_python   | 198 us                                                                                               | 196 us: 1.01x faster                                                                                             |
| pickle_dict          | 18.2 us                                                                                              | 18.0 us: 1.01x faster                                                                                            |
| unpickle_list        | 3.11 us                                                                                              | 3.09 us: 1.01x faster                                                                                            |
| unpickle_pure_python | 154 us                                                                                               | 153 us: 1.00x faster                                                                                             |
| xml_etree_generate   | 56.3 ms                                                                                              | 56.2 ms: 1.00x faster                                                                                            |
| json_dumps           | 6.52 ms                                                                                              | 6.55 ms: 1.00x slower                                                                                            |
| tomli_loads          | 1.54 sec                                                                                             | 1.55 sec: 1.01x slower                                                                                           |
| pickle_list          | 2.93 us                                                                                              | 2.97 us: 1.01x slower                                                                                            |
| xml_etree_iterparse  | 71.9 ms                                                                                              | 77.2 ms: 1.07x slower                                                                                            |
| xml_etree_parse      | 99.6 ms                                                                                              | 111 ms: 1.11x slower                                                                                             |
| Geometric mean       | (ref)                                                                                                | 1.01x slower                                                                                                     |

Benchmark hidden because not significant (3): json_loads, xml_etree_process, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240117-3.13.0a3-f009305/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                                                              | 14.7 ms: 1.19x slower                                                                                            |
| python_startup         | 13.9 ms                                                                                              | 16.6 ms: 1.19x slower                                                                                            |
| Geometric mean         | (ref)                                                                                                | 1.19x slower                                                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240117-3.13.0a3-f009305/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json |
|-----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 33.6 ms                                                                                              | 33.5 ms: 1.01x faster                                                                                            |
| mako            | 7.54 ms                                                                                              | 7.61 ms: 1.01x slower                                                                                            |
| django_template | 21.7 ms                                                                                              | 21.9 ms: 1.01x slower                                                                                            |
| Geometric mean  | (ref)                                                                                                | 1.00x slower                                                                                                     |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                        | results/bm-20240117-3.13.0a3-f009305/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| mypy2                            | 597 ms                                                                                               | 385 ms: 1.55x faster                                                                                             |
| generators                       | 28.4 ms                                                                                              | 28.0 ms: 1.02x faster                                                                                            |
| bench_thread_pool                | 500 us                                                                                               | 492 us: 1.02x faster                                                                                             |
| telco                            | 4.65 ms                                                                                              | 4.58 ms: 1.02x faster                                                                                            |
| richards                         | 33.8 ms                                                                                              | 33.3 ms: 1.01x faster                                                                                            |
| nqueens                          | 60.9 ms                                                                                              | 60.1 ms: 1.01x faster                                                                                            |
| unpickle                         | 9.29 us                                                                                              | 9.19 us: 1.01x faster                                                                                            |
| pickle_pure_python               | 198 us                                                                                               | 196 us: 1.01x faster                                                                                             |
| pickle_dict                      | 18.2 us                                                                                              | 18.0 us: 1.01x faster                                                                                            |
| meteor_contest                   | 72.7 ms                                                                                              | 72.0 ms: 1.01x faster                                                                                            |
| sqlglot_optimize                 | 33.9 ms                                                                                              | 33.7 ms: 1.01x faster                                                                                            |
| json                             | 2.98 ms                                                                                              | 2.96 ms: 1.01x faster                                                                                            |
| pycparser                        | 700 ms                                                                                               | 695 ms: 1.01x faster                                                                                             |
| unpickle_list                    | 3.11 us                                                                                              | 3.09 us: 1.01x faster                                                                                            |
| dulwich_log                      | 29.4 ms                                                                                              | 29.2 ms: 1.01x faster                                                                                            |
| sqlglot_normalize                | 183 ms                                                                                               | 182 ms: 1.01x faster                                                                                             |
| richards_super                   | 37.3 ms                                                                                              | 37.1 ms: 1.01x faster                                                                                            |
| genshi_xml                       | 33.6 ms                                                                                              | 33.5 ms: 1.01x faster                                                                                            |
| comprehensions                   | 12.1 us                                                                                              | 12.1 us: 1.00x faster                                                                                            |
| scimark_monte_carlo              | 47.5 ms                                                                                              | 47.3 ms: 1.00x faster                                                                                            |
| create_gc_cycles                 | 706 us                                                                                               | 703 us: 1.00x faster                                                                                             |
| unpickle_pure_python             | 154 us                                                                                               | 153 us: 1.00x faster                                                                                             |
| logging_format                   | 3.79 us                                                                                              | 3.78 us: 1.00x faster                                                                                            |
| xml_etree_generate               | 56.3 ms                                                                                              | 56.2 ms: 1.00x faster                                                                                            |
| sympy_expand                     | 238 ms                                                                                               | 238 ms: 1.00x faster                                                                                             |
| go                               | 106 ms                                                                                               | 105 ms: 1.00x faster                                                                                             |
| logging_simple                   | 3.49 us                                                                                              | 3.48 us: 1.00x faster                                                                                            |
| pidigits                         | 282 ms                                                                                               | 282 ms: 1.00x faster                                                                                             |
| pprint_pformat                   | 1.05 sec                                                                                             | 1.05 sec: 1.00x faster                                                                                           |
| regex_effbot                     | 2.77 ms                                                                                              | 2.77 ms: 1.00x slower                                                                                            |
| logging_silent                   | 69.9 ns                                                                                              | 70.2 ns: 1.00x slower                                                                                            |
| async_tree_io                    | 703 ms                                                                                               | 706 ms: 1.00x slower                                                                                             |
| json_dumps                       | 6.52 ms                                                                                              | 6.55 ms: 1.00x slower                                                                                            |
| thrift                           | 458 us                                                                                               | 460 us: 1.00x slower                                                                                             |
| async_generators                 | 296 ms                                                                                               | 297 ms: 1.00x slower                                                                                             |
| coroutines                       | 18.7 ms                                                                                              | 18.8 ms: 1.00x slower                                                                                            |
| tomli_loads                      | 1.54 sec                                                                                             | 1.55 sec: 1.01x slower                                                                                           |
| sympy_sum                        | 72.5 ms                                                                                              | 72.9 ms: 1.01x slower                                                                                            |
| typing_runtime_protocols         | 70.9 us                                                                                              | 71.3 us: 1.01x slower                                                                                            |
| async_tree_eager_tg              | 47.2 ms                                                                                              | 47.5 ms: 1.01x slower                                                                                            |
| sympy_integrate                  | 10.7 ms                                                                                              | 10.8 ms: 1.01x slower                                                                                            |
| async_tree_eager_cpu_io_mixed    | 370 ms                                                                                               | 372 ms: 1.01x slower                                                                                             |
| deepcopy                         | 225 us                                                                                               | 227 us: 1.01x slower                                                                                             |
| async_tree_eager_cpu_io_mixed_tg | 342 ms                                                                                               | 344 ms: 1.01x slower                                                                                             |
| async_tree_eager_memoization     | 173 ms                                                                                               | 174 ms: 1.01x slower                                                                                             |
| mako                             | 7.54 ms                                                                                              | 7.61 ms: 1.01x slower                                                                                            |
| async_tree_eager_memoization_tg  | 140 ms                                                                                               | 142 ms: 1.01x slower                                                                                             |
| django_template                  | 21.7 ms                                                                                              | 21.9 ms: 1.01x slower                                                                                            |
| deepcopy_reduce                  | 1.98 us                                                                                              | 2.00 us: 1.01x slower                                                                                            |
| 2to3                             | 170 ms                                                                                               | 172 ms: 1.01x slower                                                                                             |
| spectral_norm                    | 75.4 ms                                                                                              | 76.3 ms: 1.01x slower                                                                                            |
| chameleon                        | 4.87 ms                                                                                              | 4.93 ms: 1.01x slower                                                                                            |
| coverage                         | 47.2 ms                                                                                              | 47.8 ms: 1.01x slower                                                                                            |
| pickle_list                      | 2.93 us                                                                                              | 2.97 us: 1.01x slower                                                                                            |
| flaskblogging                    | 3.94 ms                                                                                              | 4.12 ms: 1.05x slower                                                                                            |
| bench_mp_pool                    | 45.1 ms                                                                                              | 48.4 ms: 1.07x slower                                                                                            |
| xml_etree_iterparse              | 71.9 ms                                                                                              | 77.2 ms: 1.07x slower                                                                                            |
| xml_etree_parse                  | 99.6 ms                                                                                              | 111 ms: 1.11x slower                                                                                             |
| python_startup_no_site           | 12.3 ms                                                                                              | 14.7 ms: 1.19x slower                                                                                            |
| python_startup                   | 13.9 ms                                                                                              | 16.6 ms: 1.19x slower                                                                                            |
| Geometric mean                   | (ref)                                                                                                | 1.00x slower                                                                                                     |

Benchmark hidden because not significant (48): html5lib, asyncio_tcp_ssl, scimark_fft, hexiom, float, genshi_text, mdp, fannkuch, async_tree_memoization_tg, scimark_sor, async_tree_eager, scimark_lu, scimark_sparse_mat_mult, pprint_safe_repr, regex_compile, nbody, sympy_str, asyncio_websockets, chaos, regex_v8, sqlglot_transpile, async_tree_io_tg, json_loads, async_tree_cpu_io_mixed_tg, sqlite_synth, xml_etree_process, regex_dna, pyflate, gc_traversal, pickle, crypto_pyaes, async_tree_none_tg, sqlglot_parse, deepcopy_memo, docutils, async_tree_cpu_io_mixed, raytrace, async_tree_memoization, async_tree_eager_io_tg, deltablue, async_tree_none, async_tree_eager_io, pathlib, pylint, gunicorn, asyncio_tcp, aiohttp, tornado_http
Ignored benchmarks (2) of results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json: bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 64.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.26x