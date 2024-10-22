# Results vs. base

- fork: savannahostrowski
- ref: remove_ghccc
- machine: linux-x86_64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.00x slower
- HPT reliability: 82.97%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 278 ms                                                                 | 278 ms: 1.00x faster                                                      |
| docutils       | 2.93 sec                                                               | 2.91 sec: 1.01x faster                                                    |
| html5lib       | 65.0 ms                                                                | 65.5 ms: 1.01x slower                                                     |
| tornado_http   | 94.0 ms                                                                | 93.2 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| coroutines                 | 23.1 ms                                                                | 22.8 ms: 1.01x faster                                                     |
| async_generators           | 461 ms                                                                 | 458 ms: 1.01x faster                                                      |
| asyncio_tcp_ssl            | 1.80 sec                                                               | 1.79 sec: 1.00x faster                                                    |
| async_tree_io_tg           | 963 ms                                                                 | 976 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg | 551 ms                                                                 | 561 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed    | 565 ms                                                                 | 577 ms: 1.02x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (7): asyncio_websockets, async_tree_none, asyncio_tcp, async_tree_memoization_tg, async_tree_io, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 192 ms                                                                 | 186 ms: 1.03x faster                                                      |
| float          | 75.6 ms                                                                | 75.9 ms: 1.00x slower                                                     |
| nbody          | 80.6 ms                                                                | 82.1 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                                | 24.1 ms: 1.08x faster                                                     |
| regex_dna      | 222 ms                                                                 | 208 ms: 1.07x faster                                                      |
| regex_effbot   | 3.66 ms                                                                | 3.62 ms: 1.01x faster                                                     |
| regex_compile  | 140 ms                                                                 | 141 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                                 | 99.8 ms: 1.02x faster                                                     |
| pickle_dict          | 35.9 us                                                                | 35.9 us: 1.00x slower                                                     |
| unpickle_pure_python | 215 us                                                                 | 217 us: 1.01x slower                                                      |
| pickle               | 11.9 us                                                                | 12.0 us: 1.01x slower                                                     |
| pickle_list          | 5.15 us                                                                | 5.28 us: 1.02x slower                                                     |
| json_dumps           | 10.9 ms                                                                | 11.1 ms: 1.03x slower                                                     |
| tomli_loads          | 1.90 sec                                                               | 1.95 sec: 1.03x slower                                                    |
| unpickle             | 14.1 us                                                                | 14.7 us: 1.04x slower                                                     |
| unpickle_list        | 5.13 us                                                                | 5.47 us: 1.07x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (5): xml_etree_process, xml_etree_generate, json_loads, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.09 ms                                                                | 7.06 ms: 1.00x faster                                                     |
| python_startup         | 11.9 ms                                                                | 11.9 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml     | 60.3 ms                                                                | 61.7 ms: 1.02x slower                                                     |
| mako           | 10.1 ms                                                                | 10.3 ms: 1.02x slower                                                     |
| genshi_text    | 25.3 ms                                                                | 26.1 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8                   | 26.1 ms                                                                | 24.1 ms: 1.08x faster                                                     |
| regex_dna                  | 222 ms                                                                 | 208 ms: 1.07x faster                                                      |
| pycparser                  | 1.22 sec                                                               | 1.16 sec: 1.05x faster                                                    |
| logging_simple             | 5.67 us                                                                | 5.51 us: 1.03x faster                                                     |
| pidigits                   | 192 ms                                                                 | 186 ms: 1.03x faster                                                      |
| scimark_lu                 | 114 ms                                                                 | 111 ms: 1.02x faster                                                      |
| chaos                      | 60.1 ms                                                                | 58.9 ms: 1.02x faster                                                     |
| logging_format             | 6.19 us                                                                | 6.09 us: 1.02x faster                                                     |
| xml_etree_iterparse        | 101 ms                                                                 | 99.8 ms: 1.02x faster                                                     |
| coroutines                 | 23.1 ms                                                                | 22.8 ms: 1.01x faster                                                     |
| sqlglot_transpile          | 1.69 ms                                                                | 1.67 ms: 1.01x faster                                                     |
| regex_effbot               | 3.66 ms                                                                | 3.62 ms: 1.01x faster                                                     |
| sqlglot_parse              | 1.33 ms                                                                | 1.32 ms: 1.01x faster                                                     |
| sqlglot_optimize           | 60.3 ms                                                                | 59.7 ms: 1.01x faster                                                     |
| sympy_expand               | 502 ms                                                                 | 498 ms: 1.01x faster                                                      |
| docutils                   | 2.93 sec                                                               | 2.91 sec: 1.01x faster                                                    |
| tornado_http               | 94.0 ms                                                                | 93.2 ms: 1.01x faster                                                     |
| async_generators           | 461 ms                                                                 | 458 ms: 1.01x faster                                                      |
| bench_mp_pool              | 84.2 ms                                                                | 83.8 ms: 1.01x faster                                                     |
| python_startup_no_site     | 7.09 ms                                                                | 7.06 ms: 1.00x faster                                                     |
| raytrace                   | 284 ms                                                                 | 283 ms: 1.00x faster                                                      |
| sqlglot_normalize          | 115 ms                                                                 | 114 ms: 1.00x faster                                                      |
| dulwich_log                | 66.8 ms                                                                | 66.6 ms: 1.00x faster                                                     |
| asyncio_tcp_ssl            | 1.80 sec                                                               | 1.79 sec: 1.00x faster                                                    |
| python_startup             | 11.9 ms                                                                | 11.9 ms: 1.00x faster                                                     |
| 2to3                       | 278 ms                                                                 | 278 ms: 1.00x faster                                                      |
| create_gc_cycles           | 2.68 ms                                                                | 2.68 ms: 1.00x faster                                                     |
| bench_thread_pool          | 875 us                                                                 | 877 us: 1.00x slower                                                      |
| pickle_dict                | 35.9 us                                                                | 35.9 us: 1.00x slower                                                     |
| gc_traversal               | 4.79 ms                                                                | 4.80 ms: 1.00x slower                                                     |
| float                      | 75.6 ms                                                                | 75.9 ms: 1.00x slower                                                     |
| hexiom                     | 7.03 ms                                                                | 7.06 ms: 1.00x slower                                                     |
| bpe_tokeniser              | 4.44 sec                                                               | 4.46 sec: 1.00x slower                                                    |
| regex_compile              | 140 ms                                                                 | 141 ms: 1.01x slower                                                      |
| html5lib                   | 65.0 ms                                                                | 65.5 ms: 1.01x slower                                                     |
| unpickle_pure_python       | 215 us                                                                 | 217 us: 1.01x slower                                                      |
| pickle                     | 11.9 us                                                                | 12.0 us: 1.01x slower                                                     |
| richards                   | 40.8 ms                                                                | 41.2 ms: 1.01x slower                                                     |
| scimark_sor                | 118 ms                                                                 | 119 ms: 1.01x slower                                                      |
| meteor_contest             | 108 ms                                                                 | 110 ms: 1.01x slower                                                      |
| typing_runtime_protocols   | 165 us                                                                 | 167 us: 1.01x slower                                                      |
| coverage                   | 83.4 ms                                                                | 84.5 ms: 1.01x slower                                                     |
| async_tree_io_tg           | 963 ms                                                                 | 976 ms: 1.01x slower                                                      |
| scimark_sparse_mat_mult    | 4.54 ms                                                                | 4.61 ms: 1.01x slower                                                     |
| richards_super             | 46.8 ms                                                                | 47.5 ms: 1.01x slower                                                     |
| pprint_pformat             | 1.47 sec                                                               | 1.50 sec: 1.02x slower                                                    |
| mdp                        | 2.55 sec                                                               | 2.59 sec: 1.02x slower                                                    |
| nbody                      | 80.6 ms                                                                | 82.1 ms: 1.02x slower                                                     |
| pprint_safe_repr           | 726 ms                                                                 | 739 ms: 1.02x slower                                                      |
| thrift                     | 784 us                                                                 | 799 us: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 551 ms                                                                 | 561 ms: 1.02x slower                                                      |
| deepcopy_memo              | 29.2 us                                                                | 29.8 us: 1.02x slower                                                     |
| async_tree_cpu_io_mixed    | 565 ms                                                                 | 577 ms: 1.02x slower                                                      |
| comprehensions             | 16.9 us                                                                | 17.3 us: 1.02x slower                                                     |
| scimark_monte_carlo        | 63.7 ms                                                                | 65.1 ms: 1.02x slower                                                     |
| genshi_xml                 | 60.3 ms                                                                | 61.7 ms: 1.02x slower                                                     |
| mako                       | 10.1 ms                                                                | 10.3 ms: 1.02x slower                                                     |
| pickle_list                | 5.15 us                                                                | 5.28 us: 1.02x slower                                                     |
| json_dumps                 | 10.9 ms                                                                | 11.1 ms: 1.03x slower                                                     |
| tomli_loads                | 1.90 sec                                                               | 1.95 sec: 1.03x slower                                                    |
| nqueens                    | 88.3 ms                                                                | 90.7 ms: 1.03x slower                                                     |
| genshi_text                | 25.3 ms                                                                | 26.1 ms: 1.03x slower                                                     |
| spectral_norm              | 112 ms                                                                 | 115 ms: 1.03x slower                                                      |
| pyflate                    | 434 ms                                                                 | 449 ms: 1.03x slower                                                      |
| unpickle                   | 14.1 us                                                                | 14.7 us: 1.04x slower                                                     |
| unpack_sequence            | 105 ns                                                                 | 110 ns: 1.04x slower                                                      |
| unpickle_list              | 5.13 us                                                                | 5.47 us: 1.07x slower                                                     |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (31): deepcopy_reduce, sphinx, xml_etree_process, crypto_pyaes, telco, xml_etree_generate, scimark_fft, pylint, asyncio_websockets, async_tree_none, go, pathlib, sympy_str, logging_silent, asyncio_tcp, async_tree_memoization_tg, sympy_integrate, django_template, async_tree_io, sqlite_synth, json, json_loads, sympy_sum, async_tree_none_tg, pickle_pure_python, deepcopy, generators, deltablue, fannkuch, async_tree_memoization, xml_etree_parse

# HPT report

- Reliability score: 82.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x