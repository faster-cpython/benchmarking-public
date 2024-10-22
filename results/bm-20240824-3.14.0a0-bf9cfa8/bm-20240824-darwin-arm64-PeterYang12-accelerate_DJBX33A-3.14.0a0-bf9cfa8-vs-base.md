# Results vs. base

- fork: PeterYang12
- ref: accelerate_DJBX33A
- machine: darwin-arm64
- commit hash: bf9cfa8
- commit date: 2024-08-24
- overall geometric mean: 1.00x faster
- HPT reliability: 58.33%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240825-darwin-arm64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-darwin-arm64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 185 ms                                                                | 159 ms: 1.17x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                             |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240825-darwin-arm64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-darwin-arm64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_generators                 | 284 ms                                                                | 281 ms: 1.01x faster                                                     |
| async_tree_io                    | 596 ms                                                                | 593 ms: 1.00x faster                                                     |
| asyncio_websockets               | 408 ms                                                                | 408 ms: 1.00x slower                                                     |
| async_tree_eager_cpu_io_mixed_tg | 335 ms                                                                | 336 ms: 1.00x slower                                                     |
| async_tree_eager                 | 60.2 ms                                                               | 60.6 ms: 1.01x slower                                                    |
| async_tree_eager_tg              | 41.5 ms                                                               | 41.8 ms: 1.01x slower                                                    |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (15): async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_eager_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, coroutines, async_tree_eager_io, async_tree_eager_memoization_tg, asyncio_tcp_ssl, async_tree_eager_memoization, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240825-darwin-arm64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-darwin-arm64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 59.5 ms                                                               | 59.4 ms: 1.00x faster                                                    |
| pidigits       | 281 ms                                                                | 282 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240825-darwin-arm64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-darwin-arm64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 67.8 ms                                                               | 66.7 ms: 1.02x faster                                                    |
| regex_v8       | 16.6 ms                                                               | 16.6 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240825-darwin-arm64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-darwin-arm64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate  | 53.5 ms                                                               | 52.4 ms: 1.02x faster                                                    |
| xml_etree_parse     | 111 ms                                                                | 109 ms: 1.02x faster                                                     |
| xml_etree_iterparse | 74.5 ms                                                               | 73.7 ms: 1.01x faster                                                    |
| xml_etree_process   | 37.4 ms                                                               | 37.1 ms: 1.01x faster                                                    |
| pickle_pure_python  | 181 us                                                                | 182 us: 1.00x slower                                                     |
| Geometric mean      | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (4): tomli_loads, json_loads, unpickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240825-darwin-arm64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-darwin-arm64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 12.6 ms                                                               | 12.5 ms: 1.01x faster                                                    |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240825-darwin-arm64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-darwin-arm64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 13.9 ms                                                               | 13.8 ms: 1.01x faster                                                    |
| genshi_xml     | 30.0 ms                                                               | 30.2 ms: 1.00x slower                                                    |
| mako           | 6.94 ms                                                               | 7.09 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                        | bm-20240825-darwin-arm64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-darwin-arm64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3                             | 185 ms                                                                | 159 ms: 1.17x faster                                                     |
| xml_etree_generate               | 53.5 ms                                                               | 52.4 ms: 1.02x faster                                                    |
| xml_etree_parse                  | 111 ms                                                                | 109 ms: 1.02x faster                                                     |
| typing_runtime_protocols         | 91.9 us                                                               | 90.3 us: 1.02x faster                                                    |
| regex_compile                    | 67.8 ms                                                               | 66.7 ms: 1.02x faster                                                    |
| richards_super                   | 33.5 ms                                                               | 33.0 ms: 1.02x faster                                                    |
| go                               | 106 ms                                                                | 104 ms: 1.01x faster                                                     |
| async_generators                 | 284 ms                                                                | 281 ms: 1.01x faster                                                     |
| sqlglot_transpile                | 905 us                                                                | 896 us: 1.01x faster                                                     |
| xml_etree_iterparse              | 74.5 ms                                                               | 73.7 ms: 1.01x faster                                                    |
| sqlglot_parse                    | 749 us                                                                | 742 us: 1.01x faster                                                     |
| pprint_safe_repr                 | 454 ms                                                                | 449 ms: 1.01x faster                                                     |
| xml_etree_process                | 37.4 ms                                                               | 37.1 ms: 1.01x faster                                                    |
| genshi_text                      | 13.9 ms                                                               | 13.8 ms: 1.01x faster                                                    |
| sympy_sum                        | 69.4 ms                                                               | 68.9 ms: 1.01x faster                                                    |
| thrift                           | 423 us                                                                | 420 us: 1.01x faster                                                     |
| create_gc_cycles                 | 900 us                                                                | 894 us: 1.01x faster                                                     |
| python_startup_no_site           | 12.6 ms                                                               | 12.5 ms: 1.01x faster                                                    |
| async_tree_io                    | 596 ms                                                                | 593 ms: 1.00x faster                                                     |
| scimark_monte_carlo              | 43.4 ms                                                               | 43.2 ms: 1.00x faster                                                    |
| crypto_pyaes                     | 50.7 ms                                                               | 50.5 ms: 1.00x faster                                                    |
| logging_silent                   | 61.1 ns                                                               | 60.9 ns: 1.00x faster                                                    |
| raytrace                         | 149 ms                                                                | 148 ms: 1.00x faster                                                     |
| nbody                            | 59.5 ms                                                               | 59.4 ms: 1.00x faster                                                    |
| regex_v8                         | 16.6 ms                                                               | 16.6 ms: 1.00x slower                                                    |
| asyncio_websockets               | 408 ms                                                                | 408 ms: 1.00x slower                                                     |
| pidigits                         | 281 ms                                                                | 282 ms: 1.00x slower                                                     |
| generators                       | 20.4 ms                                                               | 20.5 ms: 1.00x slower                                                    |
| dulwich_log                      | 26.9 ms                                                               | 27.0 ms: 1.00x slower                                                    |
| hexiom                           | 4.05 ms                                                               | 4.06 ms: 1.00x slower                                                    |
| gc_traversal                     | 2.45 ms                                                               | 2.46 ms: 1.00x slower                                                    |
| sqlglot_normalize                | 167 ms                                                                | 168 ms: 1.00x slower                                                     |
| meteor_contest                   | 71.9 ms                                                               | 72.1 ms: 1.00x slower                                                    |
| async_tree_eager_cpu_io_mixed_tg | 335 ms                                                                | 336 ms: 1.00x slower                                                     |
| sympy_integrate                  | 10.3 ms                                                               | 10.4 ms: 1.00x slower                                                    |
| deepcopy_reduce                  | 1.50 us                                                               | 1.51 us: 1.00x slower                                                    |
| bpe_tokeniser                    | 3.12 sec                                                              | 3.13 sec: 1.00x slower                                                   |
| deltablue                        | 2.12 ms                                                               | 2.13 ms: 1.00x slower                                                    |
| genshi_xml                       | 30.0 ms                                                               | 30.2 ms: 1.00x slower                                                    |
| deepcopy                         | 144 us                                                                | 144 us: 1.00x slower                                                     |
| sqlglot_optimize                 | 31.1 ms                                                               | 31.2 ms: 1.00x slower                                                    |
| pickle_pure_python               | 181 us                                                                | 182 us: 1.00x slower                                                     |
| telco                            | 4.77 ms                                                               | 4.79 ms: 1.01x slower                                                    |
| scimark_sor                      | 93.0 ms                                                               | 93.6 ms: 1.01x slower                                                    |
| nqueens                          | 53.2 ms                                                               | 53.5 ms: 1.01x slower                                                    |
| async_tree_eager                 | 60.2 ms                                                               | 60.6 ms: 1.01x slower                                                    |
| logging_format                   | 3.37 us                                                               | 3.39 us: 1.01x slower                                                    |
| async_tree_eager_tg              | 41.5 ms                                                               | 41.8 ms: 1.01x slower                                                    |
| comprehensions                   | 9.91 us                                                               | 9.99 us: 1.01x slower                                                    |
| sympy_str                        | 132 ms                                                                | 133 ms: 1.01x slower                                                     |
| mdp                              | 1.42 sec                                                              | 1.44 sec: 1.01x slower                                                   |
| pathlib                          | 23.3 ms                                                               | 23.6 ms: 1.01x slower                                                    |
| mako                             | 6.94 ms                                                               | 7.09 ms: 1.02x slower                                                    |
| bench_thread_pool                | 434 us                                                                | 449 us: 1.04x slower                                                     |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (44): async_tree_none, async_tree_none_tg, pycparser, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_eager_io_tg, async_tree_memoization, tomli_loads, docutils, richards, async_tree_memoization_tg, regex_effbot, async_tree_cpu_io_mixed_tg, async_tree_io_tg, json_loads, float, pprint_pformat, scimark_sparse_mat_mult, django_template, chaos, coverage, json, logging_simple, coroutines, python_startup, regex_dna, sympy_expand, fannkuch, spectral_norm, scimark_fft, pylint, async_tree_eager_io, scimark_lu, unpickle_pure_python, json_dumps, deepcopy_memo, pyflate, async_tree_eager_memoization_tg, html5lib, asyncio_tcp_ssl, bench_mp_pool, async_tree_eager_memoization, asyncio_tcp, tornado_http

# HPT report

- Reliability score: 58.33% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x