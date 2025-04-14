# Results vs. base

- fork: python
- ref: v3.13.0a2
- machine: darwin-arm64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.001x slower
- HPT reliability: 67.16%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| 2to3           | 172 ms                                                                                               | 176 ms: 1.02x slower                                                                                             |
| chameleon      | 4.77 ms                                                                                              | 4.75 ms: 1.00x faster                                                                                            |
| Geometric mean | (ref)                                                                                                | 1.00x faster                                                                                                     |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|---------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| async_tree_eager_tg | 49.3 ms                                                                                              | 49.5 ms: 1.00x slower                                                                                            |
| async_generators    | 295 ms                                                                                               | 299 ms: 1.01x slower                                                                                             |
| asyncio_tcp         | 399 ms                                                                                               | 430 ms: 1.08x slower                                                                                             |
| Geometric mean      | (ref)                                                                                                | 1.00x slower                                                                                                     |

Benchmark hidden because not significant (18): asyncio_tcp_ssl, async_tree_cpu_io_mixed, coroutines, asyncio_websockets, async_tree_memoization, async_tree_eager_io, async_tree_eager_io_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed, async_tree_none, async_tree_eager_memoization, async_tree_eager, async_tree_io_tg, async_tree_eager_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| nbody          | 71.8 ms                                                                                              | 71.5 ms: 1.00x faster                                                                                            |
| Geometric mean | (ref)                                                                                                | 1.00x slower                                                                                                     |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 17.0 ms                                                                                              | 17.3 ms: 1.02x slower                                                                                            |
| regex_effbot   | 2.56 ms                                                                                              | 2.63 ms: 1.03x slower                                                                                            |
| regex_dna      | 152 ms                                                                                               | 158 ms: 1.04x slower                                                                                             |
| Geometric mean | (ref)                                                                                                | 1.02x slower                                                                                                     |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| json_dumps           | 6.57 ms                                                                                              | 6.54 ms: 1.00x faster                                                                                            |
| pickle_dict          | 18.0 us                                                                                              | 18.0 us: 1.00x slower                                                                                            |
| xml_etree_generate   | 55.8 ms                                                                                              | 56.0 ms: 1.00x slower                                                                                            |
| unpickle_pure_python | 155 us                                                                                               | 155 us: 1.00x slower                                                                                             |
| xml_etree_iterparse  | 75.9 ms                                                                                              | 76.3 ms: 1.01x slower                                                                                            |
| pickle_list          | 2.92 us                                                                                              | 2.94 us: 1.01x slower                                                                                            |
| pickle_pure_python   | 198 us                                                                                               | 200 us: 1.01x slower                                                                                             |
| Geometric mean       | (ref)                                                                                                | 1.00x slower                                                                                                     |

Benchmark hidden because not significant (7): xml_etree_parse, pickle, tomli_loads, json_loads, xml_etree_process, unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 14.7 ms                                                                                              | 14.7 ms: 1.00x slower                                                                                            |
| python_startup         | 16.5 ms                                                                                              | 16.6 ms: 1.01x slower                                                                                            |
| Geometric mean         | (ref)                                                                                                | 1.00x slower                                                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|-----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| django_template | 21.4 ms                                                                                              | 21.5 ms: 1.00x slower                                                                                            |
| mako            | 7.33 ms                                                                                              | 7.35 ms: 1.00x slower                                                                                            |
| Geometric mean  | (ref)                                                                                                | 1.00x slower                                                                                                     |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark              | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| sqlite_synth           | 1.69 us                                                                                              | 1.60 us: 1.06x faster                                                                                            |
| logging_silent         | 71.1 ns                                                                                              | 70.6 ns: 1.01x faster                                                                                            |
| json                   | 2.99 ms                                                                                              | 2.97 ms: 1.01x faster                                                                                            |
| pprint_pformat         | 1.01 sec                                                                                             | 1.00 sec: 1.01x faster                                                                                           |
| json_dumps             | 6.57 ms                                                                                              | 6.54 ms: 1.00x faster                                                                                            |
| logging_format         | 3.83 us                                                                                              | 3.82 us: 1.00x faster                                                                                            |
| deepcopy_reduce        | 1.93 us                                                                                              | 1.92 us: 1.00x faster                                                                                            |
| thrift                 | 459 us                                                                                               | 457 us: 1.00x faster                                                                                             |
| logging_simple         | 3.55 us                                                                                              | 3.53 us: 1.00x faster                                                                                            |
| chameleon              | 4.77 ms                                                                                              | 4.75 ms: 1.00x faster                                                                                            |
| pprint_safe_repr       | 496 ms                                                                                               | 495 ms: 1.00x faster                                                                                             |
| mdp                    | 1.56 sec                                                                                             | 1.56 sec: 1.00x faster                                                                                           |
| nbody                  | 71.8 ms                                                                                              | 71.5 ms: 1.00x faster                                                                                            |
| sympy_expand           | 233 ms                                                                                               | 232 ms: 1.00x faster                                                                                             |
| scimark_lu             | 73.0 ms                                                                                              | 72.8 ms: 1.00x faster                                                                                            |
| chaos                  | 41.3 ms                                                                                              | 41.2 ms: 1.00x faster                                                                                            |
| crypto_pyaes           | 48.0 ms                                                                                              | 47.9 ms: 1.00x faster                                                                                            |
| richards               | 34.4 ms                                                                                              | 34.3 ms: 1.00x faster                                                                                            |
| richards_super         | 38.3 ms                                                                                              | 38.2 ms: 1.00x faster                                                                                            |
| deltablue              | 2.45 ms                                                                                              | 2.44 ms: 1.00x faster                                                                                            |
| sqlglot_optimize       | 33.3 ms                                                                                              | 33.3 ms: 1.00x faster                                                                                            |
| scimark_monte_carlo    | 46.7 ms                                                                                              | 46.6 ms: 1.00x faster                                                                                            |
| scimark_sor            | 104 ms                                                                                               | 104 ms: 1.00x faster                                                                                             |
| meteor_contest         | 72.9 ms                                                                                              | 72.9 ms: 1.00x faster                                                                                            |
| django_template        | 21.4 ms                                                                                              | 21.5 ms: 1.00x slower                                                                                            |
| scimark_fft            | 201 ms                                                                                               | 201 ms: 1.00x slower                                                                                             |
| python_startup_no_site | 14.7 ms                                                                                              | 14.7 ms: 1.00x slower                                                                                            |
| pickle_dict            | 18.0 us                                                                                              | 18.0 us: 1.00x slower                                                                                            |
| mako                   | 7.33 ms                                                                                              | 7.35 ms: 1.00x slower                                                                                            |
| dulwich_log            | 29.1 ms                                                                                              | 29.2 ms: 1.00x slower                                                                                            |
| async_tree_eager_tg    | 49.3 ms                                                                                              | 49.5 ms: 1.00x slower                                                                                            |
| xml_etree_generate     | 55.8 ms                                                                                              | 56.0 ms: 1.00x slower                                                                                            |
| unpickle_pure_python   | 155 us                                                                                               | 155 us: 1.00x slower                                                                                             |
| sympy_sum              | 71.6 ms                                                                                              | 72.0 ms: 1.00x slower                                                                                            |
| nqueens                | 57.8 ms                                                                                              | 58.1 ms: 1.01x slower                                                                                            |
| xml_etree_iterparse    | 75.9 ms                                                                                              | 76.3 ms: 1.01x slower                                                                                            |
| python_startup         | 16.5 ms                                                                                              | 16.6 ms: 1.01x slower                                                                                            |
| comprehensions         | 11.2 us                                                                                              | 11.3 us: 1.01x slower                                                                                            |
| pickle_list            | 2.92 us                                                                                              | 2.94 us: 1.01x slower                                                                                            |
| pickle_pure_python     | 198 us                                                                                               | 200 us: 1.01x slower                                                                                             |
| telco                  | 4.42 ms                                                                                              | 4.47 ms: 1.01x slower                                                                                            |
| async_generators       | 295 ms                                                                                               | 299 ms: 1.01x slower                                                                                             |
| generators             | 27.7 ms                                                                                              | 28.0 ms: 1.01x slower                                                                                            |
| pathlib                | 25.7 ms                                                                                              | 26.0 ms: 1.01x slower                                                                                            |
| deepcopy_memo          | 24.9 us                                                                                              | 25.3 us: 1.01x slower                                                                                            |
| regex_v8               | 17.0 ms                                                                                              | 17.3 ms: 1.02x slower                                                                                            |
| 2to3                   | 172 ms                                                                                               | 176 ms: 1.02x slower                                                                                             |
| regex_effbot           | 2.56 ms                                                                                              | 2.63 ms: 1.03x slower                                                                                            |
| regex_dna              | 152 ms                                                                                               | 158 ms: 1.04x slower                                                                                             |
| asyncio_tcp            | 399 ms                                                                                               | 430 ms: 1.08x slower                                                                                             |
| mypy2                  | 523 ms                                                                                               | 611 ms: 1.17x slower                                                                                             |
| Geometric mean         | (ref)                                                                                                | 1.00x slower                                                                                                     |

Benchmark hidden because not significant (59): tornado_http, aiohttp, bench_mp_pool, xml_etree_parse, typing_runtime_protocols, flaskblogging, asyncio_tcp_ssl, sqlglot_transpile, sqlglot_parse, pickle, tomli_loads, async_tree_cpu_io_mixed, coroutines, genshi_xml, asyncio_websockets, async_tree_memoization, async_tree_eager_io, async_tree_eager_io_tg, scimark_sparse_mat_mult, sympy_integrate, sympy_str, async_tree_cpu_io_mixed_tg, spectral_norm, pycparser, async_tree_eager_cpu_io_mixed_tg, bpe_tokeniser, pyflate, docutils, hexiom, async_tree_io, genshi_text, sqlglot_normalize, raytrace, pylint, json_loads, async_tree_none_tg, gc_traversal, async_tree_memoization_tg, regex_compile, deepcopy, async_tree_eager_cpu_io_mixed, bench_thread_pool, async_tree_none, xml_etree_process, fannkuch, create_gc_cycles, coverage, go, async_tree_eager_memoization, async_tree_eager, pidigits, async_tree_io_tg, unpickle_list, unpack_sequence, async_tree_eager_memoization_tg, unpickle, float, html5lib, gunicorn

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 67.16% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x