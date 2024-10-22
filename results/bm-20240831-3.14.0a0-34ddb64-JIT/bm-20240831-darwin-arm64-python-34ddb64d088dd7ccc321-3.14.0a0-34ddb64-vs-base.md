# Results vs. base

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: darwin-arm64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 160 ms                                                                                                          | 180 ms: 1.12x slower                                                                                                |
| docutils       | 1.46 sec                                                                                                        | 1.61 sec: 1.10x slower                                                                                              |
| html5lib       | 30.0 ms                                                                                                         | 32.8 ms: 1.09x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.09x slower                                                                                                        |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg                 | 568 ms                                                                                                          | 553 ms: 1.03x faster                                                                                                |
| async_tree_eager_tg              | 42.2 ms                                                                                                         | 41.8 ms: 1.01x faster                                                                                               |
| async_tree_io                    | 595 ms                                                                                                          | 594 ms: 1.00x faster                                                                                                |
| async_tree_eager_cpu_io_mixed_tg | 336 ms                                                                                                          | 338 ms: 1.00x slower                                                                                                |
| async_tree_eager_cpu_io_mixed    | 361 ms                                                                                                          | 365 ms: 1.01x slower                                                                                                |
| async_tree_eager                 | 61.0 ms                                                                                                         | 63.3 ms: 1.04x slower                                                                                               |
| async_generators                 | 281 ms                                                                                                          | 294 ms: 1.05x slower                                                                                                |
| asyncio_tcp                      | 407 ms                                                                                                          | 442 ms: 1.08x slower                                                                                                |
| Geometric mean                   | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (13): asyncio_tcp_ssl, async_tree_eager_io_tg, async_tree_memoization, coroutines, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_eager_io, async_tree_none, async_tree_memoization_tg, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| float          | 48.6 ms                                                                                                         | 46.4 ms: 1.05x faster                                                                                               |
| nbody          | 59.3 ms                                                                                                         | 63.8 ms: 1.08x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 145 ms                                                                                                          | 145 ms: 1.00x faster                                                                                                |
| regex_effbot   | 2.47 ms                                                                                                         | 2.47 ms: 1.00x slower                                                                                               |
| regex_compile  | 67.7 ms                                                                                                         | 74.9 ms: 1.11x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.03x slower                                                                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                                                                        | 1.24 sec: 1.19x faster                                                                                              |
| xml_etree_process    | 37.4 ms                                                                                                         | 34.6 ms: 1.08x faster                                                                                               |
| unpickle_pure_python | 143 us                                                                                                          | 133 us: 1.08x faster                                                                                                |
| xml_etree_generate   | 53.2 ms                                                                                                         | 50.7 ms: 1.05x faster                                                                                               |
| xml_etree_iterparse  | 74.3 ms                                                                                                         | 71.9 ms: 1.03x faster                                                                                               |
| pickle_pure_python   | 181 us                                                                                                          | 177 us: 1.02x faster                                                                                                |
| json_dumps           | 6.38 ms                                                                                                         | 6.28 ms: 1.02x faster                                                                                               |
| json_loads           | 17.2 us                                                                                                         | 17.3 us: 1.01x slower                                                                                               |
| Geometric mean       | (ref)                                                                                                           | 1.05x faster                                                                                                        |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 13.9 ms                                                                                                         | 13.9 ms: 1.01x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.00x slower                                                                                                        |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.03 ms                                                                                                         | 6.47 ms: 1.09x faster                                                                                               |
| django_template | 19.8 ms                                                                                                         | 22.1 ms: 1.12x slower                                                                                               |
| genshi_text     | 13.9 ms                                                                                                         | 16.8 ms: 1.21x slower                                                                                               |
| genshi_xml      | 30.3 ms                                                                                                         | 41.2 ms: 1.36x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.14x slower                                                                                                        |

All benchmarks:
===============

| Benchmark                        | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads                      | 1.47 sec                                                                                                        | 1.24 sec: 1.19x faster                                                                                              |
| mako                             | 7.03 ms                                                                                                         | 6.47 ms: 1.09x faster                                                                                               |
| xml_etree_process                | 37.4 ms                                                                                                         | 34.6 ms: 1.08x faster                                                                                               |
| unpickle_pure_python             | 143 us                                                                                                          | 133 us: 1.08x faster                                                                                                |
| xml_etree_generate               | 53.2 ms                                                                                                         | 50.7 ms: 1.05x faster                                                                                               |
| float                            | 48.6 ms                                                                                                         | 46.4 ms: 1.05x faster                                                                                               |
| scimark_sor                      | 92.9 ms                                                                                                         | 88.7 ms: 1.05x faster                                                                                               |
| deepcopy_memo                    | 16.7 us                                                                                                         | 16.1 us: 1.04x faster                                                                                               |
| xml_etree_iterparse              | 74.3 ms                                                                                                         | 71.9 ms: 1.03x faster                                                                                               |
| async_tree_io_tg                 | 568 ms                                                                                                          | 553 ms: 1.03x faster                                                                                                |
| pathlib                          | 24.2 ms                                                                                                         | 23.6 ms: 1.02x faster                                                                                               |
| pickle_pure_python               | 181 us                                                                                                          | 177 us: 1.02x faster                                                                                                |
| logging_simple                   | 3.10 us                                                                                                         | 3.03 us: 1.02x faster                                                                                               |
| logging_format                   | 3.40 us                                                                                                         | 3.34 us: 1.02x faster                                                                                               |
| deepcopy_reduce                  | 1.52 us                                                                                                         | 1.49 us: 1.02x faster                                                                                               |
| json_dumps                       | 6.38 ms                                                                                                         | 6.28 ms: 1.02x faster                                                                                               |
| scimark_lu                       | 66.6 ms                                                                                                         | 65.7 ms: 1.01x faster                                                                                               |
| async_tree_eager_tg              | 42.2 ms                                                                                                         | 41.8 ms: 1.01x faster                                                                                               |
| async_tree_io                    | 595 ms                                                                                                          | 594 ms: 1.00x faster                                                                                                |
| regex_dna                        | 145 ms                                                                                                          | 145 ms: 1.00x faster                                                                                                |
| regex_effbot                     | 2.47 ms                                                                                                         | 2.47 ms: 1.00x slower                                                                                               |
| async_tree_eager_cpu_io_mixed_tg | 336 ms                                                                                                          | 338 ms: 1.00x slower                                                                                                |
| coverage                         | 44.9 ms                                                                                                         | 45.2 ms: 1.01x slower                                                                                               |
| python_startup_no_site           | 13.9 ms                                                                                                         | 13.9 ms: 1.01x slower                                                                                               |
| json_loads                       | 17.2 us                                                                                                         | 17.3 us: 1.01x slower                                                                                               |
| create_gc_cycles                 | 896 us                                                                                                          | 904 us: 1.01x slower                                                                                                |
| thrift                           | 424 us                                                                                                          | 427 us: 1.01x slower                                                                                                |
| fannkuch                         | 261 ms                                                                                                          | 264 ms: 1.01x slower                                                                                                |
| async_tree_eager_cpu_io_mixed    | 361 ms                                                                                                          | 365 ms: 1.01x slower                                                                                                |
| telco                            | 4.79 ms                                                                                                         | 4.85 ms: 1.01x slower                                                                                               |
| spectral_norm                    | 67.1 ms                                                                                                         | 68.3 ms: 1.02x slower                                                                                               |
| pyflate                          | 321 ms                                                                                                          | 328 ms: 1.02x slower                                                                                                |
| meteor_contest                   | 72.2 ms                                                                                                         | 73.8 ms: 1.02x slower                                                                                               |
| logging_silent                   | 60.9 ns                                                                                                         | 62.4 ns: 1.02x slower                                                                                               |
| crypto_pyaes                     | 50.6 ms                                                                                                         | 52.1 ms: 1.03x slower                                                                                               |
| scimark_fft                      | 185 ms                                                                                                          | 191 ms: 1.04x slower                                                                                                |
| async_tree_eager                 | 61.0 ms                                                                                                         | 63.3 ms: 1.04x slower                                                                                               |
| typing_runtime_protocols         | 90.9 us                                                                                                         | 95.0 us: 1.05x slower                                                                                               |
| async_generators                 | 281 ms                                                                                                          | 294 ms: 1.05x slower                                                                                                |
| deepcopy                         | 146 us                                                                                                          | 154 us: 1.06x slower                                                                                                |
| pycparser                        | 642 ms                                                                                                          | 681 ms: 1.06x slower                                                                                                |
| bench_mp_pool                    | 48.6 ms                                                                                                         | 51.6 ms: 1.06x slower                                                                                               |
| dulwich_log                      | 27.4 ms                                                                                                         | 29.1 ms: 1.06x slower                                                                                               |
| nbody                            | 59.3 ms                                                                                                         | 63.8 ms: 1.08x slower                                                                                               |
| asyncio_tcp                      | 407 ms                                                                                                          | 442 ms: 1.08x slower                                                                                                |
| bench_thread_pool                | 437 us                                                                                                          | 474 us: 1.09x slower                                                                                                |
| html5lib                         | 30.0 ms                                                                                                         | 32.8 ms: 1.09x slower                                                                                               |
| deltablue                        | 2.18 ms                                                                                                         | 2.39 ms: 1.10x slower                                                                                               |
| docutils                         | 1.46 sec                                                                                                        | 1.61 sec: 1.10x slower                                                                                              |
| scimark_sparse_mat_mult          | 2.79 ms                                                                                                         | 3.07 ms: 1.10x slower                                                                                               |
| mdp                              | 1.42 sec                                                                                                        | 1.57 sec: 1.10x slower                                                                                              |
| sympy_str                        | 132 ms                                                                                                          | 145 ms: 1.10x slower                                                                                                |
| sympy_expand                     | 227 ms                                                                                                          | 250 ms: 1.11x slower                                                                                                |
| sympy_sum                        | 69.1 ms                                                                                                         | 76.4 ms: 1.11x slower                                                                                               |
| sqlglot_normalize                | 167 ms                                                                                                          | 184 ms: 1.11x slower                                                                                                |
| regex_compile                    | 67.7 ms                                                                                                         | 74.9 ms: 1.11x slower                                                                                               |
| pprint_pformat                   | 930 ms                                                                                                          | 1.04 sec: 1.12x slower                                                                                              |
| django_template                  | 19.8 ms                                                                                                         | 22.1 ms: 1.12x slower                                                                                               |
| nqueens                          | 53.2 ms                                                                                                         | 59.5 ms: 1.12x slower                                                                                               |
| 2to3                             | 160 ms                                                                                                          | 180 ms: 1.12x slower                                                                                                |
| pprint_safe_repr                 | 456 ms                                                                                                          | 511 ms: 1.12x slower                                                                                                |
| scimark_monte_carlo              | 43.2 ms                                                                                                         | 48.6 ms: 1.12x slower                                                                                               |
| chaos                            | 35.7 ms                                                                                                         | 40.4 ms: 1.13x slower                                                                                               |
| pylint                           | 182 ms                                                                                                          | 207 ms: 1.14x slower                                                                                                |
| sympy_integrate                  | 10.3 ms                                                                                                         | 11.9 ms: 1.15x slower                                                                                               |
| sqlglot_parse                    | 739 us                                                                                                          | 857 us: 1.16x slower                                                                                                |
| raytrace                         | 149 ms                                                                                                          | 174 ms: 1.17x slower                                                                                                |
| sqlglot_optimize                 | 31.0 ms                                                                                                         | 36.2 ms: 1.17x slower                                                                                               |
| sqlglot_transpile                | 898 us                                                                                                          | 1.05 ms: 1.17x slower                                                                                               |
| hexiom                           | 4.06 ms                                                                                                         | 4.78 ms: 1.18x slower                                                                                               |
| generators                       | 20.4 ms                                                                                                         | 24.6 ms: 1.20x slower                                                                                               |
| genshi_text                      | 13.9 ms                                                                                                         | 16.8 ms: 1.21x slower                                                                                               |
| comprehensions                   | 9.96 us                                                                                                         | 12.8 us: 1.28x slower                                                                                               |
| go                               | 79.0 ms                                                                                                         | 102 ms: 1.29x slower                                                                                                |
| genshi_xml                       | 30.3 ms                                                                                                         | 41.2 ms: 1.36x slower                                                                                               |
| richards_super                   | 35.3 ms                                                                                                         | 49.7 ms: 1.41x slower                                                                                               |
| richards                         | 31.6 ms                                                                                                         | 47.7 ms: 1.51x slower                                                                                               |
| Geometric mean                   | (ref)                                                                                                           | 1.05x slower                                                                                                        |

Benchmark hidden because not significant (21): bpe_tokeniser, asyncio_tcp_ssl, async_tree_eager_io_tg, json, async_tree_memoization, coroutines, asyncio_websockets, pidigits, gc_traversal, async_tree_cpu_io_mixed, python_startup, async_tree_none_tg, async_tree_eager_io, regex_v8, async_tree_none, async_tree_memoization_tg, async_tree_eager_memoization_tg, xml_etree_parse, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization, tornado_http

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x