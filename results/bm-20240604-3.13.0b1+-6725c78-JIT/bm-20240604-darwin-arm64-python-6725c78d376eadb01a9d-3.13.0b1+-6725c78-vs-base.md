# Results vs. base

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: darwin-arm64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json | results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                                                                            | 172 ms: 1.07x slower                                                                                                  |
| chameleon      | 4.31 ms                                                                                                           | 4.41 ms: 1.02x slower                                                                                                 |
| docutils       | 1.43 sec                                                                                                          | 1.50 sec: 1.05x slower                                                                                                |
| html5lib       | 31.4 ms                                                                                                           | 31.9 ms: 1.02x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.04x slower                                                                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json | results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json |
|-------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed | 359 ms                                                                                                            | 361 ms: 1.01x slower                                                                                                  |
| async_tree_eager_tg           | 41.6 ms                                                                                                           | 42.1 ms: 1.01x slower                                                                                                 |
| async_tree_eager              | 61.1 ms                                                                                                           | 63.3 ms: 1.04x slower                                                                                                 |
| Geometric mean                | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmark hidden because not significant (13): async_tree_io, async_tree_io_tg, async_tree_eager_io, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_eager_io_tg, async_tree_none, async_tree_eager_memoization, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json | results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 48.7 ms                                                                                                           | 47.4 ms: 1.03x faster                                                                                                 |
| nbody          | 60.9 ms                                                                                                           | 63.6 ms: 1.04x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json | results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 149 ms                                                                                                            | 149 ms: 1.00x faster                                                                                                  |
| regex_v8       | 17.3 ms                                                                                                           | 17.3 ms: 1.00x slower                                                                                                 |
| regex_compile  | 68.5 ms                                                                                                           | 72.7 ms: 1.06x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json | results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.44 sec                                                                                                          | 1.25 sec: 1.15x faster                                                                                                |
| unpickle_pure_python | 142 us                                                                                                            | 131 us: 1.09x faster                                                                                                  |
| json_dumps           | 6.42 ms                                                                                                           | 6.11 ms: 1.05x faster                                                                                                 |
| xml_etree_process    | 37.3 ms                                                                                                           | 35.9 ms: 1.04x faster                                                                                                 |
| pickle_pure_python   | 178 us                                                                                                            | 173 us: 1.03x faster                                                                                                  |
| xml_etree_iterparse  | 71.7 ms                                                                                                           | 70.3 ms: 1.02x faster                                                                                                 |
| xml_etree_generate   | 52.3 ms                                                                                                           | 51.4 ms: 1.02x faster                                                                                                 |
| pickle_dict          | 18.5 us                                                                                                           | 18.2 us: 1.01x faster                                                                                                 |
| unpickle_list        | 2.91 us                                                                                                           | 2.88 us: 1.01x faster                                                                                                 |
| unpickle             | 9.22 us                                                                                                           | 9.13 us: 1.01x faster                                                                                                 |
| json_loads           | 17.1 us                                                                                                           | 16.9 us: 1.01x faster                                                                                                 |
| xml_etree_parse      | 102 ms                                                                                                            | 102 ms: 1.01x faster                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.03x faster                                                                                                          |

Benchmark hidden because not significant (2): pickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json | results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                                                                           | 15.6 ms: 1.10x slower                                                                                                 |
| python_startup_no_site | 11.2 ms                                                                                                           | 12.7 ms: 1.13x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.12x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json | results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.93 ms                                                                                                           | 6.37 ms: 1.09x faster                                                                                                 |
| django_template | 19.4 ms                                                                                                           | 21.3 ms: 1.10x slower                                                                                                 |
| genshi_text     | 14.0 ms                                                                                                           | 16.0 ms: 1.14x slower                                                                                                 |
| genshi_xml      | 29.9 ms                                                                                                           | 39.5 ms: 1.32x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.11x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                     | results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json | results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json |
|-------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads                   | 1.44 sec                                                                                                          | 1.25 sec: 1.15x faster                                                                                                |
| unpickle_pure_python          | 142 us                                                                                                            | 131 us: 1.09x faster                                                                                                  |
| mako                          | 6.93 ms                                                                                                           | 6.37 ms: 1.09x faster                                                                                                 |
| fannkuch                      | 249 ms                                                                                                            | 235 ms: 1.06x faster                                                                                                  |
| json_dumps                    | 6.42 ms                                                                                                           | 6.11 ms: 1.05x faster                                                                                                 |
| deepcopy_memo                 | 22.6 us                                                                                                           | 21.7 us: 1.04x faster                                                                                                 |
| xml_etree_process             | 37.3 ms                                                                                                           | 35.9 ms: 1.04x faster                                                                                                 |
| float                         | 48.7 ms                                                                                                           | 47.4 ms: 1.03x faster                                                                                                 |
| pickle_pure_python            | 178 us                                                                                                            | 173 us: 1.03x faster                                                                                                  |
| xml_etree_iterparse           | 71.7 ms                                                                                                           | 70.3 ms: 1.02x faster                                                                                                 |
| xml_etree_generate            | 52.3 ms                                                                                                           | 51.4 ms: 1.02x faster                                                                                                 |
| coroutines                    | 16.1 ms                                                                                                           | 15.9 ms: 1.01x faster                                                                                                 |
| pickle_dict                   | 18.5 us                                                                                                           | 18.2 us: 1.01x faster                                                                                                 |
| richards                      | 31.8 ms                                                                                                           | 31.5 ms: 1.01x faster                                                                                                 |
| pprint_safe_repr              | 464 ms                                                                                                            | 459 ms: 1.01x faster                                                                                                  |
| unpickle_list                 | 2.91 us                                                                                                           | 2.88 us: 1.01x faster                                                                                                 |
| unpickle                      | 9.22 us                                                                                                           | 9.13 us: 1.01x faster                                                                                                 |
| json_loads                    | 17.1 us                                                                                                           | 16.9 us: 1.01x faster                                                                                                 |
| pyflate                       | 317 ms                                                                                                            | 314 ms: 1.01x faster                                                                                                  |
| telco                         | 4.58 ms                                                                                                           | 4.55 ms: 1.01x faster                                                                                                 |
| xml_etree_parse               | 102 ms                                                                                                            | 102 ms: 1.01x faster                                                                                                  |
| generators                    | 23.1 ms                                                                                                           | 23.0 ms: 1.01x faster                                                                                                 |
| asyncio_websockets            | 409 ms                                                                                                            | 408 ms: 1.00x faster                                                                                                  |
| regex_dna                     | 149 ms                                                                                                            | 149 ms: 1.00x faster                                                                                                  |
| regex_v8                      | 17.3 ms                                                                                                           | 17.3 ms: 1.00x slower                                                                                                 |
| spectral_norm                 | 66.8 ms                                                                                                           | 67.1 ms: 1.01x slower                                                                                                 |
| pprint_pformat                | 942 ms                                                                                                            | 947 ms: 1.01x slower                                                                                                  |
| thrift                        | 435 us                                                                                                            | 437 us: 1.01x slower                                                                                                  |
| async_tree_eager_cpu_io_mixed | 359 ms                                                                                                            | 361 ms: 1.01x slower                                                                                                  |
| asyncio_tcp_ssl               | 1.23 sec                                                                                                          | 1.24 sec: 1.01x slower                                                                                                |
| create_gc_cycles              | 901 us                                                                                                            | 909 us: 1.01x slower                                                                                                  |
| logging_silent                | 61.6 ns                                                                                                           | 62.2 ns: 1.01x slower                                                                                                 |
| deepcopy_reduce               | 1.80 us                                                                                                           | 1.82 us: 1.01x slower                                                                                                 |
| async_tree_eager_tg           | 41.6 ms                                                                                                           | 42.1 ms: 1.01x slower                                                                                                 |
| html5lib                      | 31.4 ms                                                                                                           | 31.9 ms: 1.02x slower                                                                                                 |
| scimark_fft                   | 183 ms                                                                                                            | 186 ms: 1.02x slower                                                                                                  |
| deepcopy                      | 204 us                                                                                                            | 207 us: 1.02x slower                                                                                                  |
| mdp                           | 1.41 sec                                                                                                          | 1.44 sec: 1.02x slower                                                                                                |
| dask                          | 217 ms                                                                                                            | 222 ms: 1.02x slower                                                                                                  |
| meteor_contest                | 70.0 ms                                                                                                           | 71.5 ms: 1.02x slower                                                                                                 |
| sqlite_synth                  | 1.53 us                                                                                                           | 1.57 us: 1.02x slower                                                                                                 |
| chameleon                     | 4.31 ms                                                                                                           | 4.41 ms: 1.02x slower                                                                                                 |
| go                            | 101 ms                                                                                                            | 103 ms: 1.03x slower                                                                                                  |
| typing_runtime_protocols      | 90.5 us                                                                                                           | 93.1 us: 1.03x slower                                                                                                 |
| sympy_sum                     | 69.7 ms                                                                                                           | 71.9 ms: 1.03x slower                                                                                                 |
| scimark_monte_carlo           | 42.5 ms                                                                                                           | 44.0 ms: 1.04x slower                                                                                                 |
| async_tree_eager              | 61.1 ms                                                                                                           | 63.3 ms: 1.04x slower                                                                                                 |
| crypto_pyaes                  | 49.9 ms                                                                                                           | 51.9 ms: 1.04x slower                                                                                                 |
| gunicorn                      | 1.06 ms                                                                                                           | 1.11 ms: 1.04x slower                                                                                                 |
| aiohttp                       | 999 us                                                                                                            | 1.04 ms: 1.04x slower                                                                                                 |
| bench_thread_pool             | 459 us                                                                                                            | 478 us: 1.04x slower                                                                                                  |
| sympy_expand                  | 226 ms                                                                                                            | 236 ms: 1.04x slower                                                                                                  |
| nbody                         | 60.9 ms                                                                                                           | 63.6 ms: 1.04x slower                                                                                                 |
| scimark_sparse_mat_mult       | 2.80 ms                                                                                                           | 2.92 ms: 1.04x slower                                                                                                 |
| sympy_str                     | 131 ms                                                                                                            | 137 ms: 1.04x slower                                                                                                  |
| sympy_integrate               | 10.4 ms                                                                                                           | 10.9 ms: 1.05x slower                                                                                                 |
| docutils                      | 1.43 sec                                                                                                          | 1.50 sec: 1.05x slower                                                                                                |
| pycparser                     | 639 ms                                                                                                            | 672 ms: 1.05x slower                                                                                                  |
| dulwich_log                   | 27.5 ms                                                                                                           | 29.0 ms: 1.05x slower                                                                                                 |
| sqlglot_optimize              | 31.0 ms                                                                                                           | 32.7 ms: 1.05x slower                                                                                                 |
| async_generators              | 280 ms                                                                                                            | 296 ms: 1.06x slower                                                                                                  |
| regex_compile                 | 68.5 ms                                                                                                           | 72.7 ms: 1.06x slower                                                                                                 |
| flaskblogging                 | 3.06 ms                                                                                                           | 3.25 ms: 1.06x slower                                                                                                 |
| mypy2                         | 379 ms                                                                                                            | 404 ms: 1.06x slower                                                                                                  |
| scimark_sor                   | 94.8 ms                                                                                                           | 101 ms: 1.07x slower                                                                                                  |
| 2to3                          | 161 ms                                                                                                            | 172 ms: 1.07x slower                                                                                                  |
| hexiom                        | 4.09 ms                                                                                                           | 4.37 ms: 1.07x slower                                                                                                 |
| bench_mp_pool                 | 46.4 ms                                                                                                           | 49.9 ms: 1.08x slower                                                                                                 |
| nqueens                       | 52.4 ms                                                                                                           | 56.8 ms: 1.08x slower                                                                                                 |
| python_startup                | 14.2 ms                                                                                                           | 15.6 ms: 1.10x slower                                                                                                 |
| django_template               | 19.4 ms                                                                                                           | 21.3 ms: 1.10x slower                                                                                                 |
| raytrace                      | 149 ms                                                                                                            | 164 ms: 1.10x slower                                                                                                  |
| comprehensions                | 10.9 us                                                                                                           | 12.2 us: 1.11x slower                                                                                                 |
| sqlglot_transpile             | 897 us                                                                                                            | 1.01 ms: 1.12x slower                                                                                                 |
| chaos                         | 34.8 ms                                                                                                           | 39.1 ms: 1.12x slower                                                                                                 |
| sqlglot_parse                 | 738 us                                                                                                            | 831 us: 1.13x slower                                                                                                  |
| python_startup_no_site        | 11.2 ms                                                                                                           | 12.7 ms: 1.13x slower                                                                                                 |
| genshi_text                   | 14.0 ms                                                                                                           | 16.0 ms: 1.14x slower                                                                                                 |
| deltablue                     | 2.15 ms                                                                                                           | 2.48 ms: 1.15x slower                                                                                                 |
| scimark_lu                    | 66.8 ms                                                                                                           | 78.7 ms: 1.18x slower                                                                                                 |
| genshi_xml                    | 29.9 ms                                                                                                           | 39.5 ms: 1.32x slower                                                                                                 |
| Geometric mean                | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (27): asyncio_tcp, async_tree_io, async_tree_io_tg, async_tree_eager_io, json, logging_format, logging_simple, gc_traversal, pidigits, pickle, coverage, regex_effbot, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, richards_super, async_tree_cpu_io_mixed, pickle_list, async_tree_eager_memoization_tg, async_tree_memoization_tg, async_tree_none_tg, pathlib, async_tree_eager_io_tg, async_tree_none, async_tree_eager_memoization, async_tree_memoization, tornado_http, pylint
Ignored benchmarks (1) of results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.32x