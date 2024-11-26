# Results vs. 3.13.0

- fork: mdboom
- ref: mimalloc
- machine: linux-x86_64
- commit hash: f46688b
- commit date: 2024-08-29
- overall geometric mean: 1.046x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 251 ms: 1.06x faster                                      |
| docutils       | 2.59 sec                                               | 2.67 sec: 1.03x slower                                    |
| html5lib       | 64.2 ms                                                | 61.9 ms: 1.04x faster                                     |
| tornado_http   | 92.4 ms                                                | 86.9 ms: 1.06x faster                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 407 ms: 1.14x faster                                      |
| async_tree_none            | 351 ms                                                 | 328 ms: 1.07x faster                                      |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.07x faster                                      |
| async_tree_none_tg         | 321 ms                                                 | 304 ms: 1.06x faster                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 534 ms: 1.02x faster                                      |
| asyncio_websockets         | 552 ms                                                 | 542 ms: 1.02x faster                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 569 ms: 1.01x faster                                      |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.01x slower                                     |
| async_tree_io_tg           | 857 ms                                                 | 948 ms: 1.11x slower                                      |
| async_tree_io              | 842 ms                                                 | 1.00 sec: 1.19x slower                                    |
| Geometric mean             | (ref)                                                  | 1.01x faster                                              |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| float          | 79.2 ms                                                | 75.7 ms: 1.05x faster                                     |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                      |
| nbody          | 87.0 ms                                                | 89.7 ms: 1.03x slower                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 23.3 ms: 1.12x faster                                     |
| regex_effbot   | 3.73 ms                                                | 3.34 ms: 1.12x faster                                     |
| regex_dna      | 218 ms                                                 | 208 ms: 1.05x faster                                      |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 2.01 sec: 1.06x faster                                    |
| pickle_pure_python   | 310 us                                                 | 296 us: 1.05x faster                                      |
| json_dumps           | 10.6 ms                                                | 10.1 ms: 1.04x faster                                     |
| xml_etree_process    | 60.6 ms                                                | 58.9 ms: 1.03x faster                                     |
| xml_etree_generate   | 86.7 ms                                                | 84.7 ms: 1.02x faster                                     |
| xml_etree_parse      | 156 ms                                                 | 153 ms: 1.02x faster                                      |
| unpickle_pure_python | 216 us                                                 | 214 us: 1.01x faster                                      |
| json_loads           | 27.2 us                                                | 27.5 us: 1.01x slower                                     |
| xml_etree_iterparse  | 101 ms                                                 | 103 ms: 1.02x slower                                      |
| Geometric mean       | (ref)                                                  | 1.02x faster                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.4 ms: 1.19x faster                                     |
| python_startup_no_site | 6.96 ms                                                | 7.05 ms: 1.01x slower                                     |
| Geometric mean         | (ref)                                                  | 1.09x faster                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.4 ms: 1.07x faster                                     |
| django_template | 35.2 ms                                                | 33.2 ms: 1.06x faster                                     |
| genshi_xml      | 50.9 ms                                                | 49.1 ms: 1.04x faster                                     |
| genshi_text     | 23.5 ms                                                | 22.8 ms: 1.03x faster                                     |
| Geometric mean  | (ref)                                                  | 1.05x faster                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 253 us: 1.41x faster                                      |
| create_gc_cycles           | 2.41 ms                                                | 1.74 ms: 1.38x faster                                     |
| deepcopy_memo              | 39.1 us                                                | 29.3 us: 1.33x faster                                     |
| go                         | 144 ms                                                 | 116 ms: 1.24x faster                                      |
| deepcopy_reduce            | 3.20 us                                                | 2.61 us: 1.22x faster                                     |
| gc_traversal               | 4.37 ms                                                | 3.62 ms: 1.21x faster                                     |
| python_startup             | 12.5 ms                                                | 10.4 ms: 1.19x faster                                     |
| pathlib                    | 17.5 ms                                                | 15.2 ms: 1.15x faster                                     |
| async_tree_memoization_tg  | 464 ms                                                 | 407 ms: 1.14x faster                                      |
| regex_v8                   | 26.2 ms                                                | 23.3 ms: 1.12x faster                                     |
| regex_effbot               | 3.73 ms                                                | 3.34 ms: 1.12x faster                                     |
| pycparser                  | 1.20 sec                                               | 1.08 sec: 1.11x faster                                    |
| thrift                     | 809 us                                                 | 747 us: 1.08x faster                                      |
| mdp                        | 2.72 sec                                               | 2.52 sec: 1.08x faster                                    |
| json                       | 5.36 ms                                                | 4.97 ms: 1.08x faster                                     |
| crypto_pyaes               | 75.3 ms                                                | 69.9 ms: 1.08x faster                                     |
| async_tree_none            | 351 ms                                                 | 328 ms: 1.07x faster                                      |
| mako                       | 11.1 ms                                                | 10.4 ms: 1.07x faster                                     |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.07x faster                                      |
| pyflate                    | 471 ms                                                 | 442 ms: 1.07x faster                                      |
| spectral_norm              | 115 ms                                                 | 108 ms: 1.07x faster                                      |
| tornado_http               | 92.4 ms                                                | 86.9 ms: 1.06x faster                                     |
| tomli_loads                | 2.14 sec                                               | 2.01 sec: 1.06x faster                                    |
| 2to3                       | 267 ms                                                 | 251 ms: 1.06x faster                                      |
| django_template            | 35.2 ms                                                | 33.2 ms: 1.06x faster                                     |
| async_tree_none_tg         | 321 ms                                                 | 304 ms: 1.06x faster                                      |
| typing_runtime_protocols   | 165 us                                                 | 157 us: 1.05x faster                                      |
| pickle_pure_python         | 310 us                                                 | 296 us: 1.05x faster                                      |
| regex_dna                  | 218 ms                                                 | 208 ms: 1.05x faster                                      |
| float                      | 79.2 ms                                                | 75.7 ms: 1.05x faster                                     |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                      |
| pprint_safe_repr           | 728 ms                                                 | 697 ms: 1.04x faster                                      |
| sympy_str                  | 275 ms                                                 | 263 ms: 1.04x faster                                      |
| logging_format             | 6.40 us                                                | 6.13 us: 1.04x faster                                     |
| json_dumps                 | 10.6 ms                                                | 10.1 ms: 1.04x faster                                     |
| scimark_fft                | 364 ms                                                 | 350 ms: 1.04x faster                                      |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.84 ms: 1.04x faster                                     |
| sqlglot_normalize          | 108 ms                                                 | 104 ms: 1.04x faster                                      |
| genshi_xml                 | 50.9 ms                                                | 49.1 ms: 1.04x faster                                     |
| html5lib                   | 64.2 ms                                                | 61.9 ms: 1.04x faster                                     |
| richards                   | 48.7 ms                                                | 47.0 ms: 1.04x faster                                     |
| sympy_expand               | 463 ms                                                 | 447 ms: 1.04x faster                                      |
| pprint_pformat             | 1.49 sec                                               | 1.44 sec: 1.03x faster                                    |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                      |
| genshi_text                | 23.5 ms                                                | 22.8 ms: 1.03x faster                                     |
| logging_silent             | 102 ns                                                 | 98.5 ns: 1.03x faster                                     |
| sqlglot_optimize           | 53.7 ms                                                | 52.1 ms: 1.03x faster                                     |
| xml_etree_process          | 60.6 ms                                                | 58.9 ms: 1.03x faster                                     |
| generators                 | 29.0 ms                                                | 28.2 ms: 1.03x faster                                     |
| richards_super             | 54.9 ms                                                | 53.5 ms: 1.02x faster                                     |
| xml_etree_generate         | 86.7 ms                                                | 84.7 ms: 1.02x faster                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 534 ms: 1.02x faster                                      |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.02x faster                                      |
| sympy_integrate            | 19.9 ms                                                | 19.5 ms: 1.02x faster                                     |
| scimark_monte_carlo        | 67.4 ms                                                | 66.1 ms: 1.02x faster                                     |
| asyncio_websockets         | 552 ms                                                 | 542 ms: 1.02x faster                                      |
| scimark_lu                 | 113 ms                                                 | 111 ms: 1.02x faster                                      |
| xml_etree_parse            | 156 ms                                                 | 153 ms: 1.02x faster                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 569 ms: 1.01x faster                                      |
| scimark_sor                | 124 ms                                                 | 122 ms: 1.01x faster                                      |
| raytrace                   | 267 ms                                                 | 264 ms: 1.01x faster                                      |
| deltablue                  | 3.23 ms                                                | 3.19 ms: 1.01x faster                                     |
| sqlglot_transpile          | 1.58 ms                                                | 1.57 ms: 1.01x faster                                     |
| unpickle_pure_python       | 216 us                                                 | 214 us: 1.01x faster                                      |
| telco                      | 8.54 ms                                                | 8.47 ms: 1.01x faster                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.26 ms: 1.01x faster                                     |
| nqueens                    | 78.4 ms                                                | 77.9 ms: 1.01x faster                                     |
| pidigits                   | 186 ms                                                 | 185 ms: 1.01x faster                                      |
| hexiom                     | 6.16 ms                                                | 6.19 ms: 1.00x slower                                     |
| chaos                      | 58.1 ms                                                | 58.5 ms: 1.01x slower                                     |
| comprehensions             | 16.5 us                                                | 16.6 us: 1.01x slower                                     |
| json_loads                 | 27.2 us                                                | 27.5 us: 1.01x slower                                     |
| python_startup_no_site     | 6.96 ms                                                | 7.05 ms: 1.01x slower                                     |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.01x slower                                     |
| xml_etree_iterparse        | 101 ms                                                 | 103 ms: 1.02x slower                                      |
| docutils                   | 2.59 sec                                               | 2.67 sec: 1.03x slower                                    |
| nbody                      | 87.0 ms                                                | 89.7 ms: 1.03x slower                                     |
| bpe_tokeniser              | 4.75 sec                                               | 4.96 sec: 1.04x slower                                    |
| coverage                   | 84.0 ms                                                | 89.3 ms: 1.06x slower                                     |
| async_tree_io_tg           | 857 ms                                                 | 948 ms: 1.11x slower                                      |
| async_tree_io              | 842 ms                                                 | 1.00 sec: 1.19x slower                                    |
| bench_thread_pool          | 822 us                                                 | 1.24 ms: 1.52x slower                                     |
| Geometric mean             | (ref)                                                  | 1.04x faster                                              |

Benchmark hidden because not significant (5): logging_simple, fannkuch, bench_mp_pool, async_generators, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240829-3.14.0a0-f46688b/bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.046x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.00x