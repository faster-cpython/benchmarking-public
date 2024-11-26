# Results vs. base

- fork: mdboom
- ref: unicode_check_exact
- machine: linux-x86_64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.001x faster
- HPT reliability: 83.08%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| html5lib       | 71.5 ms                                                                     | 72.7 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (3): 2to3, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 559 ms                                                                      | 545 ms: 1.03x faster                                                       |
| asyncio_tcp_ssl            | 1.57 sec                                                                    | 1.57 sec: 1.00x slower                                                     |
| coroutines                 | 21.3 ms                                                                     | 21.5 ms: 1.01x slower                                                      |
| async_tree_io_tg           | 778 ms                                                                      | 787 ms: 1.01x slower                                                       |
| async_generators           | 350 ms                                                                      | 354 ms: 1.01x slower                                                       |
| asyncio_websockets         | 384 ms                                                                      | 389 ms: 1.01x slower                                                       |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (7): async_tree_none_tg, asyncio_tcp, async_tree_memoization_tg, async_tree_io, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 87.6 ms                                                                     | 84.9 ms: 1.03x faster                                                      |
| pidigits       | 251 ms                                                                      | 253 ms: 1.01x slower                                                       |
| float          | 79.7 ms                                                                     | 80.7 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                                     | 26.7 ms: 1.02x slower                                                      |
| regex_effbot   | 3.57 ms                                                                     | 3.66 ms: 1.03x slower                                                      |
| regex_dna      | 243 ms                                                                      | 254 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.57 sec                                                                    | 2.51 sec: 1.02x faster                                                     |
| pickle_dict          | 29.9 us                                                                     | 29.6 us: 1.01x faster                                                      |
| xml_etree_iterparse  | 102 ms                                                                      | 101 ms: 1.01x faster                                                       |
| json_dumps           | 10.7 ms                                                                     | 10.7 ms: 1.00x slower                                                      |
| unpickle             | 15.2 us                                                                     | 15.3 us: 1.01x slower                                                      |
| xml_etree_generate   | 83.7 ms                                                                     | 84.4 ms: 1.01x slower                                                      |
| xml_etree_parse      | 144 ms                                                                      | 145 ms: 1.01x slower                                                       |
| unpickle_pure_python | 214 us                                                                      | 216 us: 1.01x slower                                                       |
| json_loads           | 24.8 us                                                                     | 25.1 us: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (5): xml_etree_process, pickle, pickle_pure_python, unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 13.4 ms                                                                     | 13.4 ms: 1.00x faster                                                      |
| python_startup_no_site | 8.96 ms                                                                     | 8.95 ms: 1.00x faster                                                      |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 24.8 ms                                                                     | 24.1 ms: 1.03x faster                                                      |
| django_template | 39.6 ms                                                                     | 38.6 ms: 1.03x faster                                                      |
| genshi_xml      | 53.8 ms                                                                     | 53.0 ms: 1.01x faster                                                      |
| Geometric mean  | (ref)                                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| telco                      | 8.54 ms                                                                     | 8.24 ms: 1.04x faster                                                      |
| nbody                      | 87.6 ms                                                                     | 84.9 ms: 1.03x faster                                                      |
| scimark_fft                | 305 ms                                                                      | 295 ms: 1.03x faster                                                       |
| genshi_text                | 24.8 ms                                                                     | 24.1 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult    | 4.24 ms                                                                     | 4.12 ms: 1.03x faster                                                      |
| logging_simple             | 6.39 us                                                                     | 6.21 us: 1.03x faster                                                      |
| fannkuch                   | 367 ms                                                                      | 356 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 559 ms                                                                      | 545 ms: 1.03x faster                                                       |
| django_template            | 39.6 ms                                                                     | 38.6 ms: 1.03x faster                                                      |
| scimark_monte_carlo        | 67.8 ms                                                                     | 66.2 ms: 1.02x faster                                                      |
| pycparser                  | 1.25 sec                                                                    | 1.22 sec: 1.02x faster                                                     |
| tomli_loads                | 2.57 sec                                                                    | 2.51 sec: 1.02x faster                                                     |
| pprint_safe_repr           | 822 ms                                                                      | 804 ms: 1.02x faster                                                       |
| deepcopy                   | 286 us                                                                      | 280 us: 1.02x faster                                                       |
| raytrace                   | 275 ms                                                                      | 269 ms: 1.02x faster                                                       |
| sqlglot_parse              | 1.44 ms                                                                     | 1.41 ms: 1.02x faster                                                      |
| chaos                      | 62.3 ms                                                                     | 61.2 ms: 1.02x faster                                                      |
| richards                   | 50.4 ms                                                                     | 49.6 ms: 1.02x faster                                                      |
| logging_format             | 6.92 us                                                                     | 6.82 us: 1.02x faster                                                      |
| pprint_pformat             | 1.67 sec                                                                    | 1.65 sec: 1.01x faster                                                     |
| deepcopy_memo              | 30.1 us                                                                     | 29.7 us: 1.01x faster                                                      |
| genshi_xml                 | 53.8 ms                                                                     | 53.0 ms: 1.01x faster                                                      |
| crypto_pyaes               | 72.7 ms                                                                     | 71.8 ms: 1.01x faster                                                      |
| pickle_dict                | 29.9 us                                                                     | 29.6 us: 1.01x faster                                                      |
| dulwich_log                | 67.3 ms                                                                     | 66.6 ms: 1.01x faster                                                      |
| sqlglot_transpile          | 1.82 ms                                                                     | 1.80 ms: 1.01x faster                                                      |
| deepcopy_reduce            | 2.89 us                                                                     | 2.86 us: 1.01x faster                                                      |
| xml_etree_iterparse        | 102 ms                                                                      | 101 ms: 1.01x faster                                                       |
| pathlib                    | 15.7 ms                                                                     | 15.6 ms: 1.01x faster                                                      |
| hexiom                     | 6.31 ms                                                                     | 6.29 ms: 1.00x faster                                                      |
| python_startup             | 13.4 ms                                                                     | 13.4 ms: 1.00x faster                                                      |
| python_startup_no_site     | 8.96 ms                                                                     | 8.95 ms: 1.00x faster                                                      |
| asyncio_tcp_ssl            | 1.57 sec                                                                    | 1.57 sec: 1.00x slower                                                     |
| sympy_str                  | 291 ms                                                                      | 292 ms: 1.00x slower                                                       |
| json_dumps                 | 10.7 ms                                                                     | 10.7 ms: 1.00x slower                                                      |
| sympy_integrate            | 23.0 ms                                                                     | 23.0 ms: 1.00x slower                                                      |
| nqueens                    | 88.2 ms                                                                     | 88.6 ms: 1.00x slower                                                      |
| scimark_lu                 | 94.7 ms                                                                     | 95.2 ms: 1.00x slower                                                      |
| bpe_tokeniser              | 4.89 sec                                                                    | 4.92 sec: 1.01x slower                                                     |
| pidigits                   | 251 ms                                                                      | 253 ms: 1.01x slower                                                       |
| sqlite_synth               | 2.72 us                                                                     | 2.74 us: 1.01x slower                                                      |
| sympy_sum                  | 151 ms                                                                      | 152 ms: 1.01x slower                                                       |
| unpickle                   | 15.2 us                                                                     | 15.3 us: 1.01x slower                                                      |
| sympy_expand               | 496 ms                                                                      | 500 ms: 1.01x slower                                                       |
| xml_etree_generate         | 83.7 ms                                                                     | 84.4 ms: 1.01x slower                                                      |
| sqlglot_normalize          | 118 ms                                                                      | 119 ms: 1.01x slower                                                       |
| thrift                     | 846 us                                                                      | 853 us: 1.01x slower                                                       |
| xml_etree_parse            | 144 ms                                                                      | 145 ms: 1.01x slower                                                       |
| coroutines                 | 21.3 ms                                                                     | 21.5 ms: 1.01x slower                                                      |
| unpickle_pure_python       | 214 us                                                                      | 216 us: 1.01x slower                                                       |
| async_tree_io_tg           | 778 ms                                                                      | 787 ms: 1.01x slower                                                       |
| float                      | 79.7 ms                                                                     | 80.7 ms: 1.01x slower                                                      |
| json_loads                 | 24.8 us                                                                     | 25.1 us: 1.01x slower                                                      |
| async_generators           | 350 ms                                                                      | 354 ms: 1.01x slower                                                       |
| spectral_norm              | 95.2 ms                                                                     | 96.4 ms: 1.01x slower                                                      |
| asyncio_websockets         | 384 ms                                                                      | 389 ms: 1.01x slower                                                       |
| html5lib                   | 71.5 ms                                                                     | 72.7 ms: 1.02x slower                                                      |
| create_gc_cycles           | 1.96 ms                                                                     | 1.99 ms: 1.02x slower                                                      |
| bench_thread_pool          | 856 us                                                                      | 874 us: 1.02x slower                                                       |
| regex_v8                   | 26.1 ms                                                                     | 26.7 ms: 1.02x slower                                                      |
| regex_effbot               | 3.57 ms                                                                     | 3.66 ms: 1.03x slower                                                      |
| pyflate                    | 483 ms                                                                      | 497 ms: 1.03x slower                                                       |
| regex_dna                  | 243 ms                                                                      | 254 ms: 1.05x slower                                                       |
| scimark_sor                | 111 ms                                                                      | 118 ms: 1.06x slower                                                       |
| coverage                   | 79.7 ms                                                                     | 85.2 ms: 1.07x slower                                                      |
| unpack_sequence            | 46.1 ns                                                                     | 51.6 ns: 1.12x slower                                                      |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (31): bench_mp_pool, tornado_http, xml_etree_process, typing_runtime_protocols, async_tree_none_tg, pylint, pickle, regex_compile, json, mdp, logging_silent, meteor_contest, 2to3, pickle_pure_python, richards_super, comprehensions, asyncio_tcp, sqlglot_optimize, docutils, async_tree_memoization_tg, gc_traversal, generators, async_tree_io, unpickle_list, async_tree_memoization, go, pickle_list, deltablue, async_tree_none, mako, async_tree_cpu_io_mixed

- Geometric mean (including insignificant results): 1.001x faster
# HPT report

- Reliability score: 83.08% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x