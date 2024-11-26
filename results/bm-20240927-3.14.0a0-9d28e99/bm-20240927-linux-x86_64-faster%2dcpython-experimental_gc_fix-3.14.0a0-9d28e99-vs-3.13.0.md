# Results vs. 3.13.0

- fork: faster-cpython
- ref: experimental_gc_fix
- machine: linux-x86_64
- commit hash: 9d28e99
- commit date: 2024-09-27
- overall geometric mean: 1.006x slower
- HPT reliability: 97.38%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 272 ms: 1.02x slower                                                           |
| docutils       | 2.59 sec                                               | 2.77 sec: 1.07x slower                                                         |
| html5lib       | 64.2 ms                                                | 68.1 ms: 1.06x slower                                                          |
| tornado_http   | 92.4 ms                                                | 91.5 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                           |
| coroutines                 | 22.7 ms                                                | 23.6 ms: 1.04x slower                                                          |
| async_generators           | 436 ms                                                 | 459 ms: 1.05x slower                                                           |
| async_tree_memoization_tg  | 464 ms                                                 | 498 ms: 1.08x slower                                                           |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 638 ms: 1.11x slower                                                           |
| async_tree_memoization     | 442 ms                                                 | 489 ms: 1.11x slower                                                           |
| async_tree_io_tg           | 857 ms                                                 | 966 ms: 1.13x slower                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 635 ms: 1.16x slower                                                           |
| async_tree_io              | 842 ms                                                 | 995 ms: 1.18x slower                                                           |
| async_tree_none            | 351 ms                                                 | 424 ms: 1.21x slower                                                           |
| async_tree_none_tg         | 321 ms                                                 | 390 ms: 1.22x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.11x slower                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                           |
| nbody          | 87.0 ms                                                | 87.7 ms: 1.01x slower                                                          |
| float          | 79.2 ms                                                | 97.0 ms: 1.23x slower                                                          |
| Geometric mean | (ref)                                                  | 1.08x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.5 ms: 1.07x faster                                                          |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                           |
| regex_effbot   | 3.73 ms                                                | 3.67 ms: 1.02x faster                                                          |
| regex_dna      | 218 ms                                                 | 223 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 2.09 sec: 1.02x faster                                                         |
| pickle_pure_python   | 310 us                                                 | 305 us: 1.02x faster                                                           |
| json_dumps           | 10.6 ms                                                | 10.4 ms: 1.01x faster                                                          |
| json_loads           | 27.2 us                                                | 27.1 us: 1.01x faster                                                          |
| unpickle_pure_python | 216 us                                                 | 215 us: 1.00x faster                                                           |
| xml_etree_generate   | 86.7 ms                                                | 93.0 ms: 1.07x slower                                                          |
| xml_etree_process    | 60.6 ms                                                | 65.1 ms: 1.07x slower                                                          |
| xml_etree_parse      | 156 ms                                                 | 184 ms: 1.18x slower                                                           |
| xml_etree_iterparse  | 101 ms                                                 | 150 ms: 1.48x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.17x faster                                                          |
| python_startup_no_site | 6.96 ms                                                | 7.00 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text    | 23.5 ms                                                | 22.3 ms: 1.06x faster                                                          |
| mako           | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                          |
| genshi_xml     | 50.9 ms                                                | 54.4 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.68 ms: 1.43x faster                                                          |
| deepcopy                   | 358 us                                                 | 261 us: 1.37x faster                                                           |
| deepcopy_memo              | 39.1 us                                                | 30.6 us: 1.28x faster                                                          |
| go                         | 144 ms                                                 | 119 ms: 1.21x faster                                                           |
| deepcopy_reduce            | 3.20 us                                                | 2.71 us: 1.18x faster                                                          |
| pylint                     | 313 ms                                                 | 266 ms: 1.18x faster                                                           |
| python_startup             | 12.5 ms                                                | 10.6 ms: 1.17x faster                                                          |
| gc_traversal               | 4.37 ms                                                | 3.77 ms: 1.16x faster                                                          |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                          |
| regex_v8                   | 26.2 ms                                                | 24.5 ms: 1.07x faster                                                          |
| genshi_text                | 23.5 ms                                                | 22.3 ms: 1.06x faster                                                          |
| richards                   | 48.7 ms                                                | 46.4 ms: 1.05x faster                                                          |
| typing_runtime_protocols   | 165 us                                                 | 157 us: 1.05x faster                                                           |
| richards_super             | 54.9 ms                                                | 52.4 ms: 1.05x faster                                                          |
| json                       | 5.36 ms                                                | 5.13 ms: 1.04x faster                                                          |
| thrift                     | 809 us                                                 | 776 us: 1.04x faster                                                           |
| bench_thread_pool          | 822 us                                                 | 790 us: 1.04x faster                                                           |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.88 ms: 1.03x faster                                                          |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.03x faster                                                           |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                           |
| crypto_pyaes               | 75.3 ms                                                | 73.4 ms: 1.03x faster                                                          |
| tomli_loads                | 2.14 sec                                               | 2.09 sec: 1.02x faster                                                         |
| generators                 | 29.0 ms                                                | 28.3 ms: 1.02x faster                                                          |
| sympy_str                  | 275 ms                                                 | 269 ms: 1.02x faster                                                           |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                           |
| pickle_pure_python         | 310 us                                                 | 305 us: 1.02x faster                                                           |
| pprint_pformat             | 1.49 sec                                               | 1.47 sec: 1.02x faster                                                         |
| regex_effbot               | 3.73 ms                                                | 3.67 ms: 1.02x faster                                                          |
| pprint_safe_repr           | 728 ms                                                 | 717 ms: 1.01x faster                                                           |
| telco                      | 8.54 ms                                                | 8.42 ms: 1.01x faster                                                          |
| json_dumps                 | 10.6 ms                                                | 10.4 ms: 1.01x faster                                                          |
| sympy_integrate            | 19.9 ms                                                | 19.6 ms: 1.01x faster                                                          |
| sympy_expand               | 463 ms                                                 | 458 ms: 1.01x faster                                                           |
| raytrace                   | 267 ms                                                 | 264 ms: 1.01x faster                                                           |
| tornado_http               | 92.4 ms                                                | 91.5 ms: 1.01x faster                                                          |
| logging_format             | 6.40 us                                                | 6.34 us: 1.01x faster                                                          |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                                           |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                                           |
| logging_simple             | 5.72 us                                                | 5.68 us: 1.01x faster                                                          |
| json_loads                 | 27.2 us                                                | 27.1 us: 1.01x faster                                                          |
| unpickle_pure_python       | 216 us                                                 | 215 us: 1.00x faster                                                           |
| mdp                        | 2.72 sec                                               | 2.73 sec: 1.00x slower                                                         |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                           |
| comprehensions             | 16.5 us                                                | 16.6 us: 1.00x slower                                                          |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                           |
| python_startup_no_site     | 6.96 ms                                                | 7.00 ms: 1.01x slower                                                          |
| dulwich_log                | 64.3 ms                                                | 64.8 ms: 1.01x slower                                                          |
| pyflate                    | 471 ms                                                 | 474 ms: 1.01x slower                                                           |
| scimark_monte_carlo        | 67.4 ms                                                | 68.0 ms: 1.01x slower                                                          |
| nbody                      | 87.0 ms                                                | 87.7 ms: 1.01x slower                                                          |
| scimark_fft                | 364 ms                                                 | 368 ms: 1.01x slower                                                           |
| scimark_sor                | 124 ms                                                 | 125 ms: 1.01x slower                                                           |
| sqlglot_optimize           | 53.7 ms                                                | 54.3 ms: 1.01x slower                                                          |
| pycparser                  | 1.20 sec                                               | 1.22 sec: 1.02x slower                                                         |
| nqueens                    | 78.4 ms                                                | 79.6 ms: 1.02x slower                                                          |
| 2to3                       | 267 ms                                                 | 272 ms: 1.02x slower                                                           |
| regex_dna                  | 218 ms                                                 | 223 ms: 1.02x slower                                                           |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                          |
| chaos                      | 58.1 ms                                                | 59.2 ms: 1.02x slower                                                          |
| hexiom                     | 6.16 ms                                                | 6.31 ms: 1.02x slower                                                          |
| scimark_lu                 | 113 ms                                                 | 116 ms: 1.03x slower                                                           |
| coverage                   | 84.0 ms                                                | 86.6 ms: 1.03x slower                                                          |
| logging_silent             | 102 ns                                                 | 105 ns: 1.03x slower                                                           |
| coroutines                 | 22.7 ms                                                | 23.6 ms: 1.04x slower                                                          |
| async_generators           | 436 ms                                                 | 459 ms: 1.05x slower                                                           |
| sqlglot_transpile          | 1.58 ms                                                | 1.67 ms: 1.06x slower                                                          |
| html5lib                   | 64.2 ms                                                | 68.1 ms: 1.06x slower                                                          |
| genshi_xml                 | 50.9 ms                                                | 54.4 ms: 1.07x slower                                                          |
| docutils                   | 2.59 sec                                               | 2.77 sec: 1.07x slower                                                         |
| xml_etree_generate         | 86.7 ms                                                | 93.0 ms: 1.07x slower                                                          |
| xml_etree_process          | 60.6 ms                                                | 65.1 ms: 1.07x slower                                                          |
| async_tree_memoization_tg  | 464 ms                                                 | 498 ms: 1.08x slower                                                           |
| deltablue                  | 3.23 ms                                                | 3.55 ms: 1.10x slower                                                          |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 638 ms: 1.11x slower                                                           |
| sqlglot_parse              | 1.27 ms                                                | 1.41 ms: 1.11x slower                                                          |
| async_tree_memoization     | 442 ms                                                 | 489 ms: 1.11x slower                                                           |
| async_tree_io_tg           | 857 ms                                                 | 966 ms: 1.13x slower                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 635 ms: 1.16x slower                                                           |
| async_tree_io              | 842 ms                                                 | 995 ms: 1.18x slower                                                           |
| xml_etree_parse            | 156 ms                                                 | 184 ms: 1.18x slower                                                           |
| bpe_tokeniser              | 4.75 sec                                               | 5.67 sec: 1.20x slower                                                         |
| async_tree_none            | 351 ms                                                 | 424 ms: 1.21x slower                                                           |
| async_tree_none_tg         | 321 ms                                                 | 390 ms: 1.22x slower                                                           |
| float                      | 79.2 ms                                                | 97.0 ms: 1.23x slower                                                          |
| xml_etree_iterparse        | 101 ms                                                 | 150 ms: 1.48x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                                   |

Benchmark hidden because not significant (3): bench_mp_pool, fannkuch, django_template
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240927-3.14.0a0-9d28e99/bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.006x slower
# HPT report

- Reliability score: 97.38% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.90x