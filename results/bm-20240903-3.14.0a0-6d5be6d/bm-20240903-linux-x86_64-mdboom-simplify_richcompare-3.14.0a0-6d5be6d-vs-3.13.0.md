# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.030x faster
- HPT reliability: 99.47%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 257 ms: 1.04x faster                                                  |
| docutils       | 2.59 sec                                               | 2.67 sec: 1.03x slower                                                |
| html5lib       | 64.2 ms                                                | 61.8 ms: 1.04x faster                                                 |
| tornado_http   | 92.4 ms                                                | 90.8 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 401 ms: 1.16x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 390 ms: 1.13x faster                                                  |
| async_tree_none           | 351 ms                                                 | 321 ms: 1.09x faster                                                  |
| async_tree_none_tg        | 321 ms                                                 | 308 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 560 ms: 1.03x faster                                                  |
| async_generators          | 436 ms                                                 | 431 ms: 1.01x faster                                                  |
| asyncio_websockets        | 552 ms                                                 | 558 ms: 1.01x slower                                                  |
| coroutines                | 22.7 ms                                                | 23.0 ms: 1.01x slower                                                 |
| async_tree_io_tg          | 857 ms                                                 | 896 ms: 1.05x slower                                                  |
| async_tree_io             | 842 ms                                                 | 928 ms: 1.10x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 77.8 ms: 1.02x faster                                                 |
| nbody          | 87.0 ms                                                | 85.8 ms: 1.01x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                  |
| regex_effbot   | 3.73 ms                                                | 3.76 ms: 1.01x slower                                                 |
| regex_v8       | 26.2 ms                                                | 26.8 ms: 1.02x slower                                                 |
| regex_dna      | 218 ms                                                 | 225 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads         | 2.14 sec                                               | 2.05 sec: 1.05x faster                                                |
| xml_etree_process   | 60.6 ms                                                | 58.8 ms: 1.03x faster                                                 |
| pickle_pure_python  | 310 us                                                 | 302 us: 1.03x faster                                                  |
| xml_etree_generate  | 86.7 ms                                                | 84.9 ms: 1.02x faster                                                 |
| xml_etree_parse     | 156 ms                                                 | 154 ms: 1.01x faster                                                  |
| xml_etree_iterparse | 101 ms                                                 | 105 ms: 1.03x slower                                                  |
| json_loads          | 27.2 us                                                | 28.6 us: 1.05x slower                                                 |
| Geometric mean      | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                 |
| python_startup_no_site | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 33.5 ms: 1.05x faster                                                 |
| genshi_text     | 23.5 ms                                                | 23.0 ms: 1.02x faster                                                 |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                 |
| genshi_xml      | 50.9 ms                                                | 51.5 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| create_gc_cycles          | 2.41 ms                                                | 1.74 ms: 1.39x faster                                                 |
| deepcopy                  | 358 us                                                 | 264 us: 1.36x faster                                                  |
| deepcopy_memo             | 39.1 us                                                | 29.8 us: 1.31x faster                                                 |
| go                        | 144 ms                                                 | 119 ms: 1.21x faster                                                  |
| python_startup            | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                 |
| deepcopy_reduce           | 3.20 us                                                | 2.75 us: 1.16x faster                                                 |
| gc_traversal              | 4.37 ms                                                | 3.78 ms: 1.16x faster                                                 |
| async_tree_memoization_tg | 464 ms                                                 | 401 ms: 1.16x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 390 ms: 1.13x faster                                                  |
| async_tree_none           | 351 ms                                                 | 321 ms: 1.09x faster                                                  |
| pathlib                   | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                 |
| richards_super            | 54.9 ms                                                | 51.7 ms: 1.06x faster                                                 |
| richards                  | 48.7 ms                                                | 46.0 ms: 1.06x faster                                                 |
| mdp                       | 2.72 sec                                               | 2.57 sec: 1.06x faster                                                |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.77 ms: 1.06x faster                                                 |
| django_template           | 35.2 ms                                                | 33.5 ms: 1.05x faster                                                 |
| tomli_loads               | 2.14 sec                                               | 2.05 sec: 1.05x faster                                                |
| bench_thread_pool         | 822 us                                                 | 787 us: 1.04x faster                                                  |
| generators                | 29.0 ms                                                | 27.8 ms: 1.04x faster                                                 |
| async_tree_none_tg        | 321 ms                                                 | 308 ms: 1.04x faster                                                  |
| 2to3                      | 267 ms                                                 | 257 ms: 1.04x faster                                                  |
| crypto_pyaes              | 75.3 ms                                                | 72.4 ms: 1.04x faster                                                 |
| thrift                    | 809 us                                                 | 778 us: 1.04x faster                                                  |
| html5lib                  | 64.2 ms                                                | 61.8 ms: 1.04x faster                                                 |
| logging_format            | 6.40 us                                                | 6.17 us: 1.04x faster                                                 |
| logging_simple            | 5.72 us                                                | 5.52 us: 1.04x faster                                                 |
| xml_etree_process         | 60.6 ms                                                | 58.8 ms: 1.03x faster                                                 |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 560 ms: 1.03x faster                                                  |
| meteor_contest            | 109 ms                                                 | 106 ms: 1.03x faster                                                  |
| telco                     | 8.54 ms                                                | 8.31 ms: 1.03x faster                                                 |
| pickle_pure_python        | 310 us                                                 | 302 us: 1.03x faster                                                  |
| spectral_norm             | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| genshi_text               | 23.5 ms                                                | 23.0 ms: 1.02x faster                                                 |
| xml_etree_generate        | 86.7 ms                                                | 84.9 ms: 1.02x faster                                                 |
| pprint_safe_repr          | 728 ms                                                 | 714 ms: 1.02x faster                                                  |
| sympy_str                 | 275 ms                                                 | 270 ms: 1.02x faster                                                  |
| pprint_pformat            | 1.49 sec                                               | 1.47 sec: 1.02x faster                                                |
| sympy_integrate           | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                 |
| tornado_http              | 92.4 ms                                                | 90.8 ms: 1.02x faster                                                 |
| regex_compile             | 132 ms                                                 | 130 ms: 1.02x faster                                                  |
| float                     | 79.2 ms                                                | 77.8 ms: 1.02x faster                                                 |
| json                      | 5.36 ms                                                | 5.27 ms: 1.02x faster                                                 |
| nbody                     | 87.0 ms                                                | 85.8 ms: 1.01x faster                                                 |
| xml_etree_parse           | 156 ms                                                 | 154 ms: 1.01x faster                                                  |
| async_generators          | 436 ms                                                 | 431 ms: 1.01x faster                                                  |
| raytrace                  | 267 ms                                                 | 264 ms: 1.01x faster                                                  |
| sympy_sum                 | 150 ms                                                 | 149 ms: 1.01x faster                                                  |
| sympy_expand              | 463 ms                                                 | 459 ms: 1.01x faster                                                  |
| deltablue                 | 3.23 ms                                                | 3.20 ms: 1.01x faster                                                 |
| sqlglot_optimize          | 53.7 ms                                                | 53.4 ms: 1.01x faster                                                 |
| pidigits                  | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| hexiom                    | 6.16 ms                                                | 6.19 ms: 1.00x slower                                                 |
| logging_silent            | 102 ns                                                 | 102 ns: 1.01x slower                                                  |
| regex_effbot              | 3.73 ms                                                | 3.76 ms: 1.01x slower                                                 |
| mako                      | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                 |
| bpe_tokeniser             | 4.75 sec                                               | 4.79 sec: 1.01x slower                                                |
| scimark_lu                | 113 ms                                                 | 114 ms: 1.01x slower                                                  |
| asyncio_websockets        | 552 ms                                                 | 558 ms: 1.01x slower                                                  |
| genshi_xml                | 50.9 ms                                                | 51.5 ms: 1.01x slower                                                 |
| coverage                  | 84.0 ms                                                | 84.9 ms: 1.01x slower                                                 |
| chaos                     | 58.1 ms                                                | 58.7 ms: 1.01x slower                                                 |
| sqlglot_parse             | 1.27 ms                                                | 1.29 ms: 1.01x slower                                                 |
| scimark_monte_carlo       | 67.4 ms                                                | 68.2 ms: 1.01x slower                                                 |
| python_startup_no_site    | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                 |
| pyflate                   | 471 ms                                                 | 478 ms: 1.01x slower                                                  |
| coroutines                | 22.7 ms                                                | 23.0 ms: 1.01x slower                                                 |
| scimark_sor               | 124 ms                                                 | 126 ms: 1.02x slower                                                  |
| regex_v8                  | 26.2 ms                                                | 26.8 ms: 1.02x slower                                                 |
| nqueens                   | 78.4 ms                                                | 80.4 ms: 1.03x slower                                                 |
| regex_dna                 | 218 ms                                                 | 225 ms: 1.03x slower                                                  |
| docutils                  | 2.59 sec                                               | 2.67 sec: 1.03x slower                                                |
| xml_etree_iterparse       | 101 ms                                                 | 105 ms: 1.03x slower                                                  |
| async_tree_io_tg          | 857 ms                                                 | 896 ms: 1.05x slower                                                  |
| json_loads                | 27.2 us                                                | 28.6 us: 1.05x slower                                                 |
| async_tree_io             | 842 ms                                                 | 928 ms: 1.10x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (12): async_tree_cpu_io_mixed_tg, json_dumps, pycparser, scimark_fft, sqlglot_normalize, sqlglot_transpile, unpickle_pure_python, comprehensions, bench_mp_pool, typing_runtime_protocols, fannkuch, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240903-3.14.0a0-6d5be6d/bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.030x faster
# HPT report

- Reliability score: 99.47% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x