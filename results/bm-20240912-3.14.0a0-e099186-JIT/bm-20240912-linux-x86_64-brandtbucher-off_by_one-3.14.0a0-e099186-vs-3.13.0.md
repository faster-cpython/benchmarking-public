# Results vs. 3.13.0

- fork: brandtbucher
- ref: off_by_one
- machine: linux-x86_64
- commit hash: e099186
- commit date: 2024-09-12
- overall geometric mean: 1.036x faster
- HPT reliability: 97.59%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 276 ms: 1.04x slower                                              |
| docutils       | 2.59 sec                                               | 2.93 sec: 1.13x slower                                            |
| html5lib       | 64.2 ms                                                | 62.2 ms: 1.03x faster                                             |
| tornado_http   | 92.4 ms                                                | 93.5 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                  | 1.03x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 389 ms: 1.19x faster                                              |
| async_tree_memoization     | 442 ms                                                 | 395 ms: 1.12x faster                                              |
| async_tree_none            | 351 ms                                                 | 315 ms: 1.11x faster                                              |
| async_tree_none_tg         | 321 ms                                                 | 309 ms: 1.04x faster                                              |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 567 ms: 1.02x faster                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 552 ms: 1.01x slower                                              |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                              |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.01x slower                                             |
| async_tree_io              | 842 ms                                                 | 861 ms: 1.02x slower                                              |
| async_tree_io_tg           | 857 ms                                                 | 879 ms: 1.03x slower                                              |
| async_generators           | 436 ms                                                 | 460 ms: 1.06x slower                                              |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 79.2 ms                                                | 69.7 ms: 1.14x faster                                             |
| nbody          | 87.0 ms                                                | 79.0 ms: 1.10x faster                                             |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.08x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.50 ms: 1.06x faster                                             |
| regex_v8       | 26.2 ms                                                | 25.1 ms: 1.05x faster                                             |
| regex_dna      | 218 ms                                                 | 217 ms: 1.01x faster                                              |
| regex_compile  | 132 ms                                                 | 139 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.93 sec: 1.11x faster                                            |
| xml_etree_process    | 60.6 ms                                                | 54.9 ms: 1.11x faster                                             |
| xml_etree_generate   | 86.7 ms                                                | 79.4 ms: 1.09x faster                                             |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.06x faster                                              |
| json_dumps           | 10.6 ms                                                | 9.99 ms: 1.06x faster                                             |
| xml_etree_iterparse  | 101 ms                                                 | 98.7 ms: 1.03x faster                                             |
| unpickle_pure_python | 216 us                                                 | 214 us: 1.01x faster                                              |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                      |

Benchmark hidden because not significant (2): json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                             |
| python_startup_no_site | 6.96 ms                                                | 7.05 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.77 ms: 1.13x faster                                             |
| django_template | 35.2 ms                                                | 36.5 ms: 1.04x slower                                             |
| genshi_text     | 23.5 ms                                                | 25.4 ms: 1.08x slower                                             |
| genshi_xml      | 50.9 ms                                                | 58.6 ms: 1.15x slower                                             |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 26.6 us: 1.47x faster                                             |
| deepcopy                   | 358 us                                                 | 260 us: 1.38x faster                                              |
| create_gc_cycles           | 2.41 ms                                                | 1.75 ms: 1.38x faster                                             |
| richards                   | 48.7 ms                                                | 38.9 ms: 1.25x faster                                             |
| richards_super             | 54.9 ms                                                | 44.2 ms: 1.24x faster                                             |
| deepcopy_reduce            | 3.20 us                                                | 2.65 us: 1.21x faster                                             |
| scimark_fft                | 364 ms                                                 | 304 ms: 1.20x faster                                              |
| async_tree_memoization_tg  | 464 ms                                                 | 389 ms: 1.19x faster                                              |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.19x faster                                             |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.27 ms: 1.18x faster                                             |
| spectral_norm              | 115 ms                                                 | 98.2 ms: 1.17x faster                                             |
| crypto_pyaes               | 75.3 ms                                                | 65.9 ms: 1.14x faster                                             |
| float                      | 79.2 ms                                                | 69.7 ms: 1.14x faster                                             |
| mako                       | 11.1 ms                                                | 9.77 ms: 1.13x faster                                             |
| async_tree_memoization     | 442 ms                                                 | 395 ms: 1.12x faster                                              |
| pathlib                    | 17.5 ms                                                | 15.7 ms: 1.12x faster                                             |
| async_tree_none            | 351 ms                                                 | 315 ms: 1.11x faster                                              |
| tomli_loads                | 2.14 sec                                               | 1.93 sec: 1.11x faster                                            |
| go                         | 144 ms                                                 | 130 ms: 1.11x faster                                              |
| gc_traversal               | 4.37 ms                                                | 3.94 ms: 1.11x faster                                             |
| xml_etree_process          | 60.6 ms                                                | 54.9 ms: 1.11x faster                                             |
| nbody                      | 87.0 ms                                                | 79.0 ms: 1.10x faster                                             |
| pyflate                    | 471 ms                                                 | 430 ms: 1.10x faster                                              |
| xml_etree_generate         | 86.7 ms                                                | 79.4 ms: 1.09x faster                                             |
| telco                      | 8.54 ms                                                | 7.87 ms: 1.09x faster                                             |
| fannkuch                   | 404 ms                                                 | 372 ms: 1.09x faster                                              |
| scimark_monte_carlo        | 67.4 ms                                                | 62.3 ms: 1.08x faster                                             |
| mdp                        | 2.72 sec                                               | 2.54 sec: 1.07x faster                                            |
| scimark_sor                | 124 ms                                                 | 116 ms: 1.07x faster                                              |
| bpe_tokeniser              | 4.75 sec                                               | 4.45 sec: 1.07x faster                                            |
| regex_effbot               | 3.73 ms                                                | 3.50 ms: 1.06x faster                                             |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.06x faster                                              |
| json_dumps                 | 10.6 ms                                                | 9.99 ms: 1.06x faster                                             |
| regex_v8                   | 26.2 ms                                                | 25.1 ms: 1.05x faster                                             |
| logging_format             | 6.40 us                                                | 6.13 us: 1.04x faster                                             |
| json                       | 5.36 ms                                                | 5.14 ms: 1.04x faster                                             |
| async_tree_none_tg         | 321 ms                                                 | 309 ms: 1.04x faster                                              |
| html5lib                   | 64.2 ms                                                | 62.2 ms: 1.03x faster                                             |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.03x faster                                              |
| xml_etree_iterparse        | 101 ms                                                 | 98.7 ms: 1.03x faster                                             |
| pprint_safe_repr           | 728 ms                                                 | 714 ms: 1.02x faster                                              |
| scimark_lu                 | 113 ms                                                 | 111 ms: 1.02x faster                                              |
| logging_simple             | 5.72 us                                                | 5.62 us: 1.02x faster                                             |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 567 ms: 1.02x faster                                              |
| thrift                     | 809 us                                                 | 797 us: 1.02x faster                                              |
| deltablue                  | 3.23 ms                                                | 3.18 ms: 1.01x faster                                             |
| unpickle_pure_python       | 216 us                                                 | 214 us: 1.01x faster                                              |
| regex_dna                  | 218 ms                                                 | 217 ms: 1.01x faster                                              |
| pprint_pformat             | 1.49 sec                                               | 1.48 sec: 1.01x faster                                            |
| chaos                      | 58.1 ms                                                | 57.7 ms: 1.01x faster                                             |
| pidigits                   | 186 ms                                                 | 185 ms: 1.01x faster                                              |
| comprehensions             | 16.5 us                                                | 16.6 us: 1.00x slower                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 552 ms: 1.01x slower                                              |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                              |
| tornado_http               | 92.4 ms                                                | 93.5 ms: 1.01x slower                                             |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.01x slower                                             |
| raytrace                   | 267 ms                                                 | 271 ms: 1.01x slower                                              |
| python_startup_no_site     | 6.96 ms                                                | 7.05 ms: 1.01x slower                                             |
| bench_thread_pool          | 822 us                                                 | 836 us: 1.02x slower                                              |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                              |
| coverage                   | 84.0 ms                                                | 85.7 ms: 1.02x slower                                             |
| async_tree_io              | 842 ms                                                 | 861 ms: 1.02x slower                                              |
| async_tree_io_tg           | 857 ms                                                 | 879 ms: 1.03x slower                                              |
| 2to3                       | 267 ms                                                 | 276 ms: 1.04x slower                                              |
| django_template            | 35.2 ms                                                | 36.5 ms: 1.04x slower                                             |
| sqlglot_normalize          | 108 ms                                                 | 112 ms: 1.04x slower                                              |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.05x slower                                             |
| dulwich_log                | 64.3 ms                                                | 67.6 ms: 1.05x slower                                             |
| regex_compile              | 132 ms                                                 | 139 ms: 1.05x slower                                              |
| async_generators           | 436 ms                                                 | 460 ms: 1.06x slower                                              |
| sqlglot_transpile          | 1.58 ms                                                | 1.68 ms: 1.06x slower                                             |
| sqlglot_optimize           | 53.7 ms                                                | 58.0 ms: 1.08x slower                                             |
| genshi_text                | 23.5 ms                                                | 25.4 ms: 1.08x slower                                             |
| nqueens                    | 78.4 ms                                                | 85.0 ms: 1.09x slower                                             |
| sympy_str                  | 275 ms                                                 | 299 ms: 1.09x slower                                              |
| sympy_expand               | 463 ms                                                 | 505 ms: 1.09x slower                                              |
| hexiom                     | 6.16 ms                                                | 6.88 ms: 1.12x slower                                             |
| docutils                   | 2.59 sec                                               | 2.93 sec: 1.13x slower                                            |
| sympy_integrate            | 19.9 ms                                                | 22.7 ms: 1.14x slower                                             |
| sympy_sum                  | 150 ms                                                 | 172 ms: 1.14x slower                                              |
| genshi_xml                 | 50.9 ms                                                | 58.6 ms: 1.15x slower                                             |
| generators                 | 29.0 ms                                                | 33.5 ms: 1.16x slower                                             |
| pylint                     | 313 ms                                                 | 375 ms: 1.20x slower                                              |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                      |

Benchmark hidden because not significant (5): json_loads, typing_runtime_protocols, pickle_pure_python, pycparser, bench_mp_pool
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240912-3.14.0a0-e099186-JIT/bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.036x faster
# HPT report

- Reliability score: 97.59% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x