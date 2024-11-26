# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: 971feb9
- commit date: 2024-10-01
- overall geometric mean: 1.043x faster
- HPT reliability: 98.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 277 ms: 1.04x slower                                                        |
| html5lib       | 64.2 ms                                                | 62.7 ms: 1.02x faster                                                       |
| tornado_http   | 92.4 ms                                                | 94.1 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 393 ms: 1.18x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 405 ms: 1.09x faster                                                        |
| async_tree_none            | 351 ms                                                 | 325 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 569 ms: 1.01x faster                                                        |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                        |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 558 ms: 1.02x slower                                                        |
| async_tree_io_tg           | 857 ms                                                 | 883 ms: 1.03x slower                                                        |
| async_generators           | 436 ms                                                 | 461 ms: 1.06x slower                                                        |
| async_tree_io              | 842 ms                                                 | 892 ms: 1.06x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 71.4 ms: 1.11x faster                                                       |
| nbody          | 87.0 ms                                                | 82.8 ms: 1.05x faster                                                       |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.1 ms: 1.04x faster                                                       |
| regex_effbot   | 3.73 ms                                                | 3.61 ms: 1.03x faster                                                       |
| regex_dna      | 218 ms                                                 | 217 ms: 1.01x faster                                                        |
| regex_compile  | 132 ms                                                 | 140 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.88 sec: 1.14x faster                                                      |
| xml_etree_generate   | 86.7 ms                                                | 76.7 ms: 1.13x faster                                                       |
| xml_etree_process    | 60.6 ms                                                | 54.1 ms: 1.12x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.06x faster                                                        |
| json_dumps           | 10.6 ms                                                | 10.1 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 101 ms                                                 | 98.7 ms: 1.03x faster                                                       |
| json_loads           | 27.2 us                                                | 26.8 us: 1.02x faster                                                       |
| pickle_pure_python   | 310 us                                                 | 307 us: 1.01x faster                                                        |
| unpickle_pure_python | 216 us                                                 | 213 us: 1.01x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                       |
| python_startup_no_site | 6.96 ms                                                | 7.09 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako           | 11.1 ms                                                | 9.79 ms: 1.13x faster                                                       |
| genshi_text    | 23.5 ms                                                | 25.0 ms: 1.06x slower                                                       |
| genshi_xml     | 50.9 ms                                                | 57.7 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| richards                   | 48.7 ms                                                | 32.7 ms: 1.49x faster                                                       |
| deepcopy_memo              | 39.1 us                                                | 26.8 us: 1.46x faster                                                       |
| richards_super             | 54.9 ms                                                | 38.5 ms: 1.43x faster                                                       |
| create_gc_cycles           | 2.41 ms                                                | 1.73 ms: 1.39x faster                                                       |
| deepcopy                   | 358 us                                                 | 261 us: 1.37x faster                                                        |
| deepcopy_reduce            | 3.20 us                                                | 2.66 us: 1.20x faster                                                       |
| scimark_fft                | 364 ms                                                 | 307 ms: 1.19x faster                                                        |
| python_startup             | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 393 ms: 1.18x faster                                                        |
| crypto_pyaes               | 75.3 ms                                                | 64.9 ms: 1.16x faster                                                       |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.40 ms: 1.15x faster                                                       |
| tomli_loads                | 2.14 sec                                               | 1.88 sec: 1.14x faster                                                      |
| mako                       | 11.1 ms                                                | 9.79 ms: 1.13x faster                                                       |
| xml_etree_generate         | 86.7 ms                                                | 76.7 ms: 1.13x faster                                                       |
| go                         | 144 ms                                                 | 127 ms: 1.13x faster                                                        |
| gc_traversal               | 4.37 ms                                                | 3.88 ms: 1.13x faster                                                       |
| pathlib                    | 17.5 ms                                                | 15.6 ms: 1.12x faster                                                       |
| xml_etree_process          | 60.6 ms                                                | 54.1 ms: 1.12x faster                                                       |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                        |
| telco                      | 8.54 ms                                                | 7.63 ms: 1.12x faster                                                       |
| float                      | 79.2 ms                                                | 71.4 ms: 1.11x faster                                                       |
| fannkuch                   | 404 ms                                                 | 366 ms: 1.10x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 405 ms: 1.09x faster                                                        |
| scimark_monte_carlo        | 67.4 ms                                                | 62.2 ms: 1.08x faster                                                       |
| bpe_tokeniser              | 4.75 sec                                               | 4.39 sec: 1.08x faster                                                      |
| async_tree_none            | 351 ms                                                 | 325 ms: 1.08x faster                                                        |
| mdp                        | 2.72 sec                                               | 2.53 sec: 1.08x faster                                                      |
| pyflate                    | 471 ms                                                 | 441 ms: 1.07x faster                                                        |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.06x faster                                                        |
| pprint_safe_repr           | 728 ms                                                 | 691 ms: 1.05x faster                                                        |
| scimark_sor                | 124 ms                                                 | 117 ms: 1.05x faster                                                        |
| json                       | 5.36 ms                                                | 5.10 ms: 1.05x faster                                                       |
| nbody                      | 87.0 ms                                                | 82.8 ms: 1.05x faster                                                       |
| json_dumps                 | 10.6 ms                                                | 10.1 ms: 1.05x faster                                                       |
| logging_format             | 6.40 us                                                | 6.11 us: 1.05x faster                                                       |
| regex_v8                   | 26.2 ms                                                | 25.1 ms: 1.04x faster                                                       |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                                      |
| pprint_pformat             | 1.49 sec                                               | 1.44 sec: 1.04x faster                                                      |
| meteor_contest             | 109 ms                                                 | 105 ms: 1.04x faster                                                        |
| regex_effbot               | 3.73 ms                                                | 3.61 ms: 1.03x faster                                                       |
| deltablue                  | 3.23 ms                                                | 3.13 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 101 ms                                                 | 98.7 ms: 1.03x faster                                                       |
| html5lib                   | 64.2 ms                                                | 62.7 ms: 1.02x faster                                                       |
| thrift                     | 809 us                                                 | 791 us: 1.02x faster                                                        |
| comprehensions             | 16.5 us                                                | 16.2 us: 1.02x faster                                                       |
| logging_simple             | 5.72 us                                                | 5.62 us: 1.02x faster                                                       |
| json_loads                 | 27.2 us                                                | 26.8 us: 1.02x faster                                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 569 ms: 1.01x faster                                                        |
| pickle_pure_python         | 310 us                                                 | 307 us: 1.01x faster                                                        |
| unpickle_pure_python       | 216 us                                                 | 213 us: 1.01x faster                                                        |
| regex_dna                  | 218 ms                                                 | 217 ms: 1.01x faster                                                        |
| pidigits                   | 186 ms                                                 | 185 ms: 1.01x faster                                                        |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                        |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.01x slower                                                       |
| tornado_http               | 92.4 ms                                                | 94.1 ms: 1.02x slower                                                       |
| python_startup_no_site     | 6.96 ms                                                | 7.09 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 558 ms: 1.02x slower                                                        |
| chaos                      | 58.1 ms                                                | 59.3 ms: 1.02x slower                                                       |
| coverage                   | 84.0 ms                                                | 85.9 ms: 1.02x slower                                                       |
| raytrace                   | 267 ms                                                 | 274 ms: 1.03x slower                                                        |
| sqlglot_parse              | 1.27 ms                                                | 1.31 ms: 1.03x slower                                                       |
| logging_silent             | 102 ns                                                 | 105 ns: 1.03x slower                                                        |
| async_tree_io_tg           | 857 ms                                                 | 883 ms: 1.03x slower                                                        |
| 2to3                       | 267 ms                                                 | 277 ms: 1.04x slower                                                        |
| sqlglot_transpile          | 1.58 ms                                                | 1.65 ms: 1.04x slower                                                       |
| sqlglot_normalize          | 108 ms                                                 | 113 ms: 1.05x slower                                                        |
| dulwich_log                | 64.3 ms                                                | 67.6 ms: 1.05x slower                                                       |
| regex_compile              | 132 ms                                                 | 140 ms: 1.06x slower                                                        |
| async_generators           | 436 ms                                                 | 461 ms: 1.06x slower                                                        |
| async_tree_io              | 842 ms                                                 | 892 ms: 1.06x slower                                                        |
| genshi_text                | 23.5 ms                                                | 25.0 ms: 1.06x slower                                                       |
| sympy_expand               | 463 ms                                                 | 500 ms: 1.08x slower                                                        |
| hexiom                     | 6.16 ms                                                | 6.67 ms: 1.08x slower                                                       |
| sympy_str                  | 275 ms                                                 | 298 ms: 1.08x slower                                                        |
| bench_thread_pool          | 822 us                                                 | 891 us: 1.08x slower                                                        |
| genshi_xml                 | 50.9 ms                                                | 57.7 ms: 1.13x slower                                                       |
| sympy_integrate            | 19.9 ms                                                | 22.6 ms: 1.14x slower                                                       |
| nqueens                    | 78.4 ms                                                | 89.6 ms: 1.14x slower                                                       |
| pylint                     | 313 ms                                                 | 364 ms: 1.16x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 177 ms: 1.18x slower                                                        |
| generators                 | 29.0 ms                                                | 34.1 ms: 1.18x slower                                                       |
| bench_mp_pool              | 24.0 ms                                                | 60.8 ms: 2.53x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (4): async_tree_none_tg, scimark_lu, typing_runtime_protocols, django_template
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, docutils, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_optimize
Ignored benchmarks (9) of results/bm-20241001-3.14.0a0-971feb9-JIT/bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.043x faster
# HPT report

- Reliability score: 98.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.96x