# Results vs. base

- fork: python
- ref: v3.13.0a3
- machine: darwin-arm64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240117-3.13.0a3-f009305/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| 2to3           | 170 ms                                                                                               | 173 ms: 1.02x slower                                                                                             |
| chameleon      | 4.87 ms                                                                                              | 5.03 ms: 1.03x slower                                                                                            |
| docutils       | 1.46 sec                                                                                             | 1.50 sec: 1.03x slower                                                                                           |
| tornado_http   | 78.1 ms                                                                                              | 70.3 ms: 1.11x faster                                                                                            |
| Geometric mean | (ref)                                                                                                | 1.01x faster                                                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240117-3.13.0a3-f009305/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 531 ms                                                                                               | 538 ms: 1.01x slower                                                                                             |
| async_tree_io_tg           | 672 ms                                                                                               | 682 ms: 1.02x slower                                                                                             |
| async_tree_cpu_io_mixed    | 521 ms                                                                                               | 530 ms: 1.02x slower                                                                                             |
| async_tree_io              | 703 ms                                                                                               | 715 ms: 1.02x slower                                                                                             |
| async_tree_memoization     | 329 ms                                                                                               | 337 ms: 1.02x slower                                                                                             |
| async_tree_none_tg         | 260 ms                                                                                               | 267 ms: 1.03x slower                                                                                             |
| async_tree_none            | 253 ms                                                                                               | 261 ms: 1.03x slower                                                                                             |
| async_tree_memoization_tg  | 324 ms                                                                                               | 335 ms: 1.03x slower                                                                                             |
| Geometric mean             | (ref)                                                                                                | 1.02x slower                                                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240117-3.13.0a3-f009305/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| pidigits       | 282 ms                                                                                               | 284 ms: 1.00x slower                                                                                             |
| nbody          | 75.6 ms                                                                                              | 86.4 ms: 1.14x slower                                                                                            |
| float          | 56.9 ms                                                                                              | 68.9 ms: 1.21x slower                                                                                            |
| Geometric mean | (ref)                                                                                                | 1.12x slower                                                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240117-3.13.0a3-f009305/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 157 ms                                                                                               | 156 ms: 1.01x faster                                                                                             |
| regex_v8       | 18.0 ms                                                                                              | 17.9 ms: 1.01x faster                                                                                            |
| regex_compile  | 73.8 ms                                                                                              | 82.6 ms: 1.12x slower                                                                                            |
| Geometric mean | (ref)                                                                                                | 1.03x slower                                                                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240117-3.13.0a3-f009305/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| unpickle             | 9.29 us                                                                                              | 9.16 us: 1.01x faster                                                                                            |
| unpickle_list        | 3.11 us                                                                                              | 3.07 us: 1.01x faster                                                                                            |
| pickle_pure_python   | 198 us                                                                                               | 196 us: 1.01x faster                                                                                             |
| pickle_dict          | 18.2 us                                                                                              | 18.1 us: 1.00x faster                                                                                            |
| pickle               | 7.41 us                                                                                              | 7.44 us: 1.00x slower                                                                                            |
| pickle_list          | 2.93 us                                                                                              | 2.97 us: 1.01x slower                                                                                            |
| json_dumps           | 6.52 ms                                                                                              | 6.61 ms: 1.01x slower                                                                                            |
| xml_etree_process    | 39.9 ms                                                                                              | 40.9 ms: 1.03x slower                                                                                            |
| xml_etree_generate   | 56.3 ms                                                                                              | 58.8 ms: 1.04x slower                                                                                            |
| unpickle_pure_python | 154 us                                                                                               | 165 us: 1.07x slower                                                                                             |
| xml_etree_parse      | 99.6 ms                                                                                              | 107 ms: 1.07x slower                                                                                             |
| tomli_loads          | 1.54 sec                                                                                             | 1.68 sec: 1.09x slower                                                                                           |
| xml_etree_iterparse  | 71.9 ms                                                                                              | 80.9 ms: 1.13x slower                                                                                            |
| Geometric mean       | (ref)                                                                                                | 1.03x slower                                                                                                     |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240117-3.13.0a3-f009305/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                                                              | 12.8 ms: 1.09x faster                                                                                            |
| python_startup_no_site | 12.3 ms                                                                                              | 11.4 ms: 1.08x faster                                                                                            |
| Geometric mean         | (ref)                                                                                                | 1.08x faster                                                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | results/bm-20240117-3.13.0a3-f009305/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json |
|-----------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| mako      | 7.54 ms                                                                                              | 9.85 ms: 1.31x slower                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20240117-3.13.0a3-f009305/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| tornado_http               | 78.1 ms                                                                                              | 70.3 ms: 1.11x faster                                                                                            |
| python_startup             | 13.9 ms                                                                                              | 12.8 ms: 1.09x faster                                                                                            |
| python_startup_no_site     | 12.3 ms                                                                                              | 11.4 ms: 1.08x faster                                                                                            |
| richards                   | 33.8 ms                                                                                              | 32.8 ms: 1.03x faster                                                                                            |
| richards_super             | 37.3 ms                                                                                              | 36.6 ms: 1.02x faster                                                                                            |
| unpickle                   | 9.29 us                                                                                              | 9.16 us: 1.01x faster                                                                                            |
| unpickle_list              | 3.11 us                                                                                              | 3.07 us: 1.01x faster                                                                                            |
| pickle_pure_python         | 198 us                                                                                               | 196 us: 1.01x faster                                                                                             |
| regex_dna                  | 157 ms                                                                                               | 156 ms: 1.01x faster                                                                                             |
| regex_v8                   | 18.0 ms                                                                                              | 17.9 ms: 1.01x faster                                                                                            |
| create_gc_cycles           | 706 us                                                                                               | 703 us: 1.00x faster                                                                                             |
| pickle_dict                | 18.2 us                                                                                              | 18.1 us: 1.00x faster                                                                                            |
| pickle                     | 7.41 us                                                                                              | 7.44 us: 1.00x slower                                                                                            |
| pidigits                   | 282 ms                                                                                               | 284 ms: 1.00x slower                                                                                             |
| async_generators           | 296 ms                                                                                               | 297 ms: 1.00x slower                                                                                             |
| scimark_sor                | 105 ms                                                                                               | 106 ms: 1.01x slower                                                                                             |
| generators                 | 28.4 ms                                                                                              | 28.7 ms: 1.01x slower                                                                                            |
| coroutines                 | 18.7 ms                                                                                              | 18.9 ms: 1.01x slower                                                                                            |
| async_tree_cpu_io_mixed_tg | 531 ms                                                                                               | 538 ms: 1.01x slower                                                                                             |
| pickle_list                | 2.93 us                                                                                              | 2.97 us: 1.01x slower                                                                                            |
| json_dumps                 | 6.52 ms                                                                                              | 6.61 ms: 1.01x slower                                                                                            |
| deepcopy_reduce            | 1.98 us                                                                                              | 2.01 us: 1.01x slower                                                                                            |
| deepcopy                   | 225 us                                                                                               | 229 us: 1.01x slower                                                                                             |
| async_tree_io_tg           | 672 ms                                                                                               | 682 ms: 1.02x slower                                                                                             |
| coverage                   | 47.2 ms                                                                                              | 47.9 ms: 1.02x slower                                                                                            |
| telco                      | 4.65 ms                                                                                              | 4.73 ms: 1.02x slower                                                                                            |
| async_tree_cpu_io_mixed    | 521 ms                                                                                               | 530 ms: 1.02x slower                                                                                             |
| async_tree_io              | 703 ms                                                                                               | 715 ms: 1.02x slower                                                                                             |
| 2to3                       | 170 ms                                                                                               | 173 ms: 1.02x slower                                                                                             |
| json                       | 2.98 ms                                                                                              | 3.04 ms: 1.02x slower                                                                                            |
| logging_format             | 3.79 us                                                                                              | 3.88 us: 1.02x slower                                                                                            |
| sqlite_synth               | 1.60 us                                                                                              | 1.64 us: 1.02x slower                                                                                            |
| dulwich_log                | 29.4 ms                                                                                              | 30.1 ms: 1.02x slower                                                                                            |
| async_tree_memoization     | 329 ms                                                                                               | 337 ms: 1.02x slower                                                                                             |
| xml_etree_process          | 39.9 ms                                                                                              | 40.9 ms: 1.03x slower                                                                                            |
| logging_simple             | 3.49 us                                                                                              | 3.58 us: 1.03x slower                                                                                            |
| docutils                   | 1.46 sec                                                                                             | 1.50 sec: 1.03x slower                                                                                           |
| sqlglot_parse              | 789 us                                                                                               | 811 us: 1.03x slower                                                                                             |
| async_tree_none_tg         | 260 ms                                                                                               | 267 ms: 1.03x slower                                                                                             |
| sqlglot_transpile          | 965 us                                                                                               | 994 us: 1.03x slower                                                                                             |
| logging_silent             | 69.9 ns                                                                                              | 72.1 ns: 1.03x slower                                                                                            |
| async_tree_none            | 253 ms                                                                                               | 261 ms: 1.03x slower                                                                                             |
| scimark_lu                 | 74.2 ms                                                                                              | 76.7 ms: 1.03x slower                                                                                            |
| mdp                        | 1.56 sec                                                                                             | 1.62 sec: 1.03x slower                                                                                           |
| chameleon                  | 4.87 ms                                                                                              | 5.03 ms: 1.03x slower                                                                                            |
| async_tree_memoization_tg  | 324 ms                                                                                               | 335 ms: 1.03x slower                                                                                             |
| sympy_expand               | 238 ms                                                                                               | 247 ms: 1.03x slower                                                                                             |
| bench_thread_pool          | 500 us                                                                                               | 517 us: 1.04x slower                                                                                             |
| deepcopy_memo              | 25.7 us                                                                                              | 26.8 us: 1.04x slower                                                                                            |
| pathlib                    | 24.5 ms                                                                                              | 25.5 ms: 1.04x slower                                                                                            |
| xml_etree_generate         | 56.3 ms                                                                                              | 58.8 ms: 1.04x slower                                                                                            |
| typing_runtime_protocols   | 70.9 us                                                                                              | 74.1 us: 1.04x slower                                                                                            |
| sqlglot_normalize          | 183 ms                                                                                               | 191 ms: 1.05x slower                                                                                             |
| meteor_contest             | 72.7 ms                                                                                              | 76.8 ms: 1.06x slower                                                                                            |
| go                         | 106 ms                                                                                               | 112 ms: 1.06x slower                                                                                             |
| sqlglot_optimize           | 33.9 ms                                                                                              | 36.0 ms: 1.06x slower                                                                                            |
| sympy_str                  | 140 ms                                                                                               | 149 ms: 1.07x slower                                                                                             |
| unpickle_pure_python       | 154 us                                                                                               | 165 us: 1.07x slower                                                                                             |
| xml_etree_parse            | 99.6 ms                                                                                              | 107 ms: 1.07x slower                                                                                             |
| sympy_integrate            | 10.7 ms                                                                                              | 11.6 ms: 1.08x slower                                                                                            |
| tomli_loads                | 1.54 sec                                                                                             | 1.68 sec: 1.09x slower                                                                                           |
| raytrace                   | 171 ms                                                                                               | 186 ms: 1.09x slower                                                                                             |
| sympy_sum                  | 72.5 ms                                                                                              | 79.4 ms: 1.10x slower                                                                                            |
| pyflate                    | 339 ms                                                                                               | 373 ms: 1.10x slower                                                                                             |
| pprint_safe_repr           | 516 ms                                                                                               | 575 ms: 1.11x slower                                                                                             |
| regex_compile              | 73.8 ms                                                                                              | 82.6 ms: 1.12x slower                                                                                            |
| pprint_pformat             | 1.05 sec                                                                                             | 1.18 sec: 1.12x slower                                                                                           |
| nqueens                    | 60.9 ms                                                                                              | 68.4 ms: 1.12x slower                                                                                            |
| xml_etree_iterparse        | 71.9 ms                                                                                              | 80.9 ms: 1.13x slower                                                                                            |
| crypto_pyaes               | 48.3 ms                                                                                              | 54.7 ms: 1.13x slower                                                                                            |
| nbody                      | 75.6 ms                                                                                              | 86.4 ms: 1.14x slower                                                                                            |
| chaos                      | 39.8 ms                                                                                              | 46.7 ms: 1.17x slower                                                                                            |
| scimark_monte_carlo        | 47.5 ms                                                                                              | 57.0 ms: 1.20x slower                                                                                            |
| fannkuch                   | 273 ms                                                                                               | 328 ms: 1.20x slower                                                                                             |
| float                      | 56.9 ms                                                                                              | 68.9 ms: 1.21x slower                                                                                            |
| scimark_fft                | 204 ms                                                                                               | 249 ms: 1.22x slower                                                                                             |
| comprehensions             | 12.1 us                                                                                              | 15.7 us: 1.29x slower                                                                                            |
| mako                       | 7.54 ms                                                                                              | 9.85 ms: 1.31x slower                                                                                            |
| hexiom                     | 4.57 ms                                                                                              | 6.04 ms: 1.32x slower                                                                                            |
| scimark_sparse_mat_mult    | 3.11 ms                                                                                              | 4.19 ms: 1.35x slower                                                                                            |
| spectral_norm              | 75.4 ms                                                                                              | 106 ms: 1.40x slower                                                                                             |
| deltablue                  | 2.44 ms                                                                                              | 3.63 ms: 1.49x slower                                                                                            |
| Geometric mean             | (ref)                                                                                                | 1.06x slower                                                                                                     |

Benchmark hidden because not significant (9): mypy2, asyncio_tcp_ssl, gc_traversal, regex_effbot, json_loads, bench_mp_pool, asyncio_websockets, pycparser, asyncio_tcp
Ignored benchmarks (17) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json: aiohttp, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json: dask, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.98x