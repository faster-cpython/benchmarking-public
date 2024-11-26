# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_unlikely
- machine: linux-x86_64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.008x faster
- HPT reliability: 62.13%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 278 ms: 1.04x slower                                                    |
| docutils       | 2.59 sec                                               | 2.92 sec: 1.13x slower                                                  |
| html5lib       | 64.2 ms                                                | 63.4 ms: 1.01x faster                                                   |
| sphinx         | 1.03 sec                                               | 1.16 sec: 1.12x slower                                                  |
| tornado_http   | 92.4 ms                                                | 95.4 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 374 ms: 1.24x faster                                                    |
| async_tree_none            | 351 ms                                                 | 328 ms: 1.07x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                                    |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                    |
| async_tree_io              | 842 ms                                                 | 859 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 559 ms: 1.02x slower                                                    |
| async_generators           | 436 ms                                                 | 461 ms: 1.06x slower                                                    |
| async_tree_io_tg           | 857 ms                                                 | 974 ms: 1.14x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_cpu_io_mixed, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 80.9 ms: 1.08x faster                                                   |
| float          | 79.2 ms                                                | 75.3 ms: 1.05x faster                                                   |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.5 ms: 1.07x faster                                                   |
| regex_dna      | 218 ms                                                 | 216 ms: 1.01x faster                                                    |
| regex_effbot   | 3.73 ms                                                | 3.78 ms: 1.01x slower                                                   |
| regex_compile  | 132 ms                                                 | 141 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                  | 1.00x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|---------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.14 sec                                               | 1.91 sec: 1.12x faster                                                  |
| xml_etree_generate  | 86.7 ms                                                | 78.5 ms: 1.10x faster                                                   |
| xml_etree_process   | 60.6 ms                                                | 55.0 ms: 1.10x faster                                                   |
| xml_etree_parse     | 156 ms                                                 | 146 ms: 1.06x faster                                                    |
| json_loads          | 27.2 us                                                | 26.6 us: 1.02x faster                                                   |
| xml_etree_iterparse | 101 ms                                                 | 99.1 ms: 1.02x faster                                                   |
| pickle_pure_python  | 310 us                                                 | 309 us: 1.01x faster                                                    |
| json_dumps          | 10.6 ms                                                | 10.9 ms: 1.03x slower                                                   |
| Geometric mean      | (ref)                                                  | 1.04x faster                                                            |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.9 ms: 1.05x faster                                                   |
| python_startup_no_site | 6.96 ms                                                | 7.09 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.93 ms: 1.12x faster                                                   |
| django_template | 35.2 ms                                                | 36.9 ms: 1.05x slower                                                   |
| genshi_text     | 23.5 ms                                                | 25.5 ms: 1.08x slower                                                   |
| genshi_xml      | 50.9 ms                                                | 59.7 ms: 1.17x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 29.3 us: 1.33x faster                                                   |
| deepcopy                   | 358 us                                                 | 270 us: 1.33x faster                                                    |
| async_tree_memoization_tg  | 464 ms                                                 | 374 ms: 1.24x faster                                                    |
| richards                   | 48.7 ms                                                | 41.1 ms: 1.18x faster                                                   |
| deepcopy_reduce            | 3.20 us                                                | 2.71 us: 1.18x faster                                                   |
| richards_super             | 54.9 ms                                                | 47.0 ms: 1.17x faster                                                   |
| scimark_fft                | 364 ms                                                 | 317 ms: 1.15x faster                                                    |
| crypto_pyaes               | 75.3 ms                                                | 66.4 ms: 1.13x faster                                                   |
| tomli_loads                | 2.14 sec                                               | 1.91 sec: 1.12x faster                                                  |
| mako                       | 11.1 ms                                                | 9.93 ms: 1.12x faster                                                   |
| xml_etree_generate         | 86.7 ms                                                | 78.5 ms: 1.10x faster                                                   |
| xml_etree_process          | 60.6 ms                                                | 55.0 ms: 1.10x faster                                                   |
| telco                      | 8.54 ms                                                | 7.79 ms: 1.10x faster                                                   |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.62 ms: 1.09x faster                                                   |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                   |
| json                       | 5.36 ms                                                | 4.92 ms: 1.09x faster                                                   |
| go                         | 144 ms                                                 | 132 ms: 1.09x faster                                                    |
| nbody                      | 87.0 ms                                                | 80.9 ms: 1.08x faster                                                   |
| mdp                        | 2.72 sec                                               | 2.54 sec: 1.07x faster                                                  |
| regex_v8                   | 26.2 ms                                                | 24.5 ms: 1.07x faster                                                   |
| async_tree_none            | 351 ms                                                 | 328 ms: 1.07x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                                    |
| bpe_tokeniser              | 4.75 sec                                               | 4.45 sec: 1.07x faster                                                  |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.06x faster                                                    |
| scimark_monte_carlo        | 67.4 ms                                                | 64.1 ms: 1.05x faster                                                   |
| float                      | 79.2 ms                                                | 75.3 ms: 1.05x faster                                                   |
| python_startup             | 12.5 ms                                                | 11.9 ms: 1.05x faster                                                   |
| logging_format             | 6.40 us                                                | 6.12 us: 1.04x faster                                                   |
| scimark_sor                | 124 ms                                                 | 118 ms: 1.04x faster                                                    |
| pyflate                    | 471 ms                                                 | 452 ms: 1.04x faster                                                    |
| thrift                     | 809 us                                                 | 783 us: 1.03x faster                                                    |
| fannkuch                   | 404 ms                                                 | 395 ms: 1.02x faster                                                    |
| json_loads                 | 27.2 us                                                | 26.6 us: 1.02x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                  |
| logging_simple             | 5.72 us                                                | 5.59 us: 1.02x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 99.1 ms: 1.02x faster                                                   |
| logging_silent             | 102 ns                                                 | 100 ns: 1.02x faster                                                    |
| regex_dna                  | 218 ms                                                 | 216 ms: 1.01x faster                                                    |
| html5lib                   | 64.2 ms                                                | 63.4 ms: 1.01x faster                                                   |
| pickle_pure_python         | 310 us                                                 | 309 us: 1.01x faster                                                    |
| meteor_contest             | 109 ms                                                 | 109 ms: 1.00x faster                                                    |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                    |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                    |
| deltablue                  | 3.23 ms                                                | 3.26 ms: 1.01x slower                                                   |
| regex_effbot               | 3.73 ms                                                | 3.78 ms: 1.01x slower                                                   |
| spectral_norm              | 115 ms                                                 | 117 ms: 1.02x slower                                                    |
| python_startup_no_site     | 6.96 ms                                                | 7.09 ms: 1.02x slower                                                   |
| gc_traversal               | 4.37 ms                                                | 4.45 ms: 1.02x slower                                                   |
| async_tree_io              | 842 ms                                                 | 859 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 559 ms: 1.02x slower                                                    |
| comprehensions             | 16.5 us                                                | 16.9 us: 1.02x slower                                                   |
| tornado_http               | 92.4 ms                                                | 95.4 ms: 1.03x slower                                                   |
| json_dumps                 | 10.6 ms                                                | 10.9 ms: 1.03x slower                                                   |
| raytrace                   | 267 ms                                                 | 276 ms: 1.04x slower                                                    |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                                   |
| 2to3                       | 267 ms                                                 | 278 ms: 1.04x slower                                                    |
| dulwich_log                | 64.3 ms                                                | 67.0 ms: 1.04x slower                                                   |
| django_template            | 35.2 ms                                                | 36.9 ms: 1.05x slower                                                   |
| async_generators           | 436 ms                                                 | 461 ms: 1.06x slower                                                    |
| sqlglot_transpile          | 1.58 ms                                                | 1.68 ms: 1.06x slower                                                   |
| sqlglot_normalize          | 108 ms                                                 | 115 ms: 1.07x slower                                                    |
| bench_thread_pool          | 822 us                                                 | 878 us: 1.07x slower                                                    |
| regex_compile              | 132 ms                                                 | 141 ms: 1.07x slower                                                    |
| sympy_expand               | 463 ms                                                 | 499 ms: 1.08x slower                                                    |
| genshi_text                | 23.5 ms                                                | 25.5 ms: 1.08x slower                                                   |
| sympy_str                  | 275 ms                                                 | 301 ms: 1.10x slower                                                    |
| create_gc_cycles           | 2.41 ms                                                | 2.67 ms: 1.11x slower                                                   |
| sqlglot_optimize           | 53.7 ms                                                | 59.9 ms: 1.12x slower                                                   |
| sphinx                     | 1.03 sec                                               | 1.16 sec: 1.12x slower                                                  |
| docutils                   | 2.59 sec                                               | 2.92 sec: 1.13x slower                                                  |
| nqueens                    | 78.4 ms                                                | 88.4 ms: 1.13x slower                                                   |
| hexiom                     | 6.16 ms                                                | 6.98 ms: 1.13x slower                                                   |
| async_tree_io_tg           | 857 ms                                                 | 974 ms: 1.14x slower                                                    |
| genshi_xml                 | 50.9 ms                                                | 59.7 ms: 1.17x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 177 ms: 1.18x slower                                                    |
| sympy_integrate            | 19.9 ms                                                | 23.5 ms: 1.18x slower                                                   |
| pylint                     | 313 ms                                                 | 376 ms: 1.20x slower                                                    |
| generators                 | 29.0 ms                                                | 35.3 ms: 1.22x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 84.2 ms: 3.51x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (10): pprint_safe_repr, async_tree_none_tg, async_tree_cpu_io_mixed, chaos, unpickle_pure_python, coverage, coroutines, scimark_lu, typing_runtime_protocols, pprint_pformat
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.008x faster
# HPT report

- Reliability score: 62.13% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x