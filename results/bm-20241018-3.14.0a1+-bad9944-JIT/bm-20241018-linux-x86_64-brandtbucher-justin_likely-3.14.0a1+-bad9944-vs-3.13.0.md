# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_likely
- machine: linux-x86_64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.001x faster
- HPT reliability: 79.43%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 278 ms: 1.04x slower                                                  |
| docutils       | 2.59 sec                                               | 2.92 sec: 1.13x slower                                                |
| sphinx         | 1.03 sec                                               | 1.17 sec: 1.13x slower                                                |
| tornado_http   | 92.4 ms                                                | 95.0 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 375 ms: 1.24x faster                                                  |
| async_tree_none            | 351 ms                                                 | 329 ms: 1.07x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 420 ms: 1.05x faster                                                  |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                  |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 556 ms: 1.02x slower                                                  |
| async_generators           | 436 ms                                                 | 454 ms: 1.04x slower                                                  |
| async_tree_io_tg           | 857 ms                                                 | 971 ms: 1.13x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 76.0 ms: 1.04x faster                                                 |
| nbody          | 87.0 ms                                                | 84.5 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                 |
| regex_effbot   | 3.73 ms                                                | 3.68 ms: 1.01x faster                                                 |
| regex_dna      | 218 ms                                                 | 216 ms: 1.01x faster                                                  |
| regex_compile  | 132 ms                                                 | 143 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.93 sec: 1.11x faster                                                |
| xml_etree_generate   | 86.7 ms                                                | 78.8 ms: 1.10x faster                                                 |
| xml_etree_process    | 60.6 ms                                                | 55.5 ms: 1.09x faster                                                 |
| xml_etree_parse      | 156 ms                                                 | 149 ms: 1.04x faster                                                  |
| json_loads           | 27.2 us                                                | 26.5 us: 1.03x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 99.7 ms: 1.02x faster                                                 |
| pickle_pure_python   | 310 us                                                 | 313 us: 1.01x slower                                                  |
| unpickle_pure_python | 216 us                                                 | 218 us: 1.01x slower                                                  |
| json_dumps           | 10.6 ms                                                | 11.2 ms: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.9 ms: 1.05x faster                                                 |
| python_startup_no_site | 6.96 ms                                                | 7.09 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.1 ms: 1.10x faster                                                 |
| django_template | 35.2 ms                                                | 36.7 ms: 1.04x slower                                                 |
| genshi_text     | 23.5 ms                                                | 25.2 ms: 1.07x slower                                                 |
| genshi_xml      | 50.9 ms                                                | 61.9 ms: 1.21x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 29.8 us: 1.31x faster                                                 |
| deepcopy                   | 358 us                                                 | 274 us: 1.31x faster                                                  |
| async_tree_memoization_tg  | 464 ms                                                 | 375 ms: 1.24x faster                                                  |
| richards                   | 48.7 ms                                                | 41.4 ms: 1.18x faster                                                 |
| richards_super             | 54.9 ms                                                | 47.2 ms: 1.16x faster                                                 |
| deepcopy_reduce            | 3.20 us                                                | 2.81 us: 1.14x faster                                                 |
| scimark_fft                | 364 ms                                                 | 323 ms: 1.13x faster                                                  |
| crypto_pyaes               | 75.3 ms                                                | 67.7 ms: 1.11x faster                                                 |
| telco                      | 8.54 ms                                                | 7.69 ms: 1.11x faster                                                 |
| tomli_loads                | 2.14 sec                                               | 1.93 sec: 1.11x faster                                                |
| xml_etree_generate         | 86.7 ms                                                | 78.8 ms: 1.10x faster                                                 |
| json                       | 5.36 ms                                                | 4.88 ms: 1.10x faster                                                 |
| mako                       | 11.1 ms                                                | 10.1 ms: 1.10x faster                                                 |
| xml_etree_process          | 60.6 ms                                                | 55.5 ms: 1.09x faster                                                 |
| pathlib                    | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                 |
| go                         | 144 ms                                                 | 134 ms: 1.07x faster                                                  |
| bpe_tokeniser              | 4.75 sec                                               | 4.44 sec: 1.07x faster                                                |
| async_tree_none            | 351 ms                                                 | 329 ms: 1.07x faster                                                  |
| regex_v8                   | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                 |
| scimark_monte_carlo        | 67.4 ms                                                | 63.9 ms: 1.06x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 420 ms: 1.05x faster                                                  |
| scimark_sor                | 124 ms                                                 | 118 ms: 1.05x faster                                                  |
| python_startup             | 12.5 ms                                                | 11.9 ms: 1.05x faster                                                 |
| logging_format             | 6.40 us                                                | 6.11 us: 1.05x faster                                                 |
| xml_etree_parse            | 156 ms                                                 | 149 ms: 1.04x faster                                                  |
| float                      | 79.2 ms                                                | 76.0 ms: 1.04x faster                                                 |
| pyflate                    | 471 ms                                                 | 455 ms: 1.04x faster                                                  |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.90 ms: 1.03x faster                                                 |
| nbody                      | 87.0 ms                                                | 84.5 ms: 1.03x faster                                                 |
| logging_silent             | 102 ns                                                 | 98.8 ns: 1.03x faster                                                 |
| json_loads                 | 27.2 us                                                | 26.5 us: 1.03x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| thrift                     | 809 us                                                 | 794 us: 1.02x faster                                                  |
| logging_simple             | 5.72 us                                                | 5.62 us: 1.02x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 99.7 ms: 1.02x faster                                                 |
| regex_effbot               | 3.73 ms                                                | 3.68 ms: 1.01x faster                                                 |
| regex_dna                  | 218 ms                                                 | 216 ms: 1.01x faster                                                  |
| meteor_contest             | 109 ms                                                 | 109 ms: 1.00x faster                                                  |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                  |
| coverage                   | 84.0 ms                                                | 84.6 ms: 1.01x slower                                                 |
| pickle_pure_python         | 310 us                                                 | 313 us: 1.01x slower                                                  |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                 |
| typing_runtime_protocols   | 165 us                                                 | 166 us: 1.01x slower                                                  |
| deltablue                  | 3.23 ms                                                | 3.27 ms: 1.01x slower                                                 |
| mdp                        | 2.72 sec                                               | 2.75 sec: 1.01x slower                                                |
| unpickle_pure_python       | 216 us                                                 | 218 us: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 556 ms: 1.02x slower                                                  |
| python_startup_no_site     | 6.96 ms                                                | 7.09 ms: 1.02x slower                                                 |
| pprint_safe_repr           | 728 ms                                                 | 742 ms: 1.02x slower                                                  |
| chaos                      | 58.1 ms                                                | 59.4 ms: 1.02x slower                                                 |
| tornado_http               | 92.4 ms                                                | 95.0 ms: 1.03x slower                                                 |
| gc_traversal               | 4.37 ms                                                | 4.52 ms: 1.03x slower                                                 |
| dulwich_log                | 64.3 ms                                                | 66.7 ms: 1.04x slower                                                 |
| raytrace                   | 267 ms                                                 | 278 ms: 1.04x slower                                                  |
| async_generators           | 436 ms                                                 | 454 ms: 1.04x slower                                                  |
| pprint_pformat             | 1.49 sec                                               | 1.56 sec: 1.04x slower                                                |
| 2to3                       | 267 ms                                                 | 278 ms: 1.04x slower                                                  |
| django_template            | 35.2 ms                                                | 36.7 ms: 1.04x slower                                                 |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.05x slower                                                 |
| comprehensions             | 16.5 us                                                | 17.4 us: 1.06x slower                                                 |
| json_dumps                 | 10.6 ms                                                | 11.2 ms: 1.06x slower                                                 |
| sqlglot_normalize          | 108 ms                                                 | 115 ms: 1.07x slower                                                  |
| sqlglot_transpile          | 1.58 ms                                                | 1.69 ms: 1.07x slower                                                 |
| bench_thread_pool          | 822 us                                                 | 878 us: 1.07x slower                                                  |
| genshi_text                | 23.5 ms                                                | 25.2 ms: 1.07x slower                                                 |
| regex_compile              | 132 ms                                                 | 143 ms: 1.08x slower                                                  |
| sympy_expand               | 463 ms                                                 | 505 ms: 1.09x slower                                                  |
| sympy_str                  | 275 ms                                                 | 303 ms: 1.10x slower                                                  |
| create_gc_cycles           | 2.41 ms                                                | 2.68 ms: 1.11x slower                                                 |
| docutils                   | 2.59 sec                                               | 2.92 sec: 1.13x slower                                                |
| sqlglot_optimize           | 53.7 ms                                                | 60.6 ms: 1.13x slower                                                 |
| sphinx                     | 1.03 sec                                               | 1.17 sec: 1.13x slower                                                |
| nqueens                    | 78.4 ms                                                | 88.6 ms: 1.13x slower                                                 |
| async_tree_io_tg           | 857 ms                                                 | 971 ms: 1.13x slower                                                  |
| hexiom                     | 6.16 ms                                                | 7.07 ms: 1.15x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 175 ms: 1.16x slower                                                  |
| sympy_integrate            | 19.9 ms                                                | 23.6 ms: 1.19x slower                                                 |
| pylint                     | 313 ms                                                 | 377 ms: 1.21x slower                                                  |
| genshi_xml                 | 50.9 ms                                                | 61.9 ms: 1.21x slower                                                 |
| generators                 | 29.0 ms                                                | 35.2 ms: 1.22x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 84.0 ms: 3.50x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (7): fannkuch, async_tree_cpu_io_mixed, html5lib, async_tree_none_tg, scimark_lu, pidigits, async_tree_io
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.001x faster
# HPT report

- Reliability score: 79.43% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x