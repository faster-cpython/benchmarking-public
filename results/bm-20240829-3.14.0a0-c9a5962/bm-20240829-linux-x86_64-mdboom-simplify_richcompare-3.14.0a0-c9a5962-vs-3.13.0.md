# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.040x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 253 ms: 1.06x faster                                                  |
| docutils       | 2.59 sec                                               | 2.64 sec: 1.02x slower                                                |
| tornado_http   | 92.4 ms                                                | 89.5 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 400 ms: 1.16x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 389 ms: 1.14x faster                                                  |
| async_tree_none           | 351 ms                                                 | 322 ms: 1.09x faster                                                  |
| async_tree_none_tg        | 321 ms                                                 | 307 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 561 ms: 1.03x faster                                                  |
| async_generators          | 436 ms                                                 | 439 ms: 1.01x slower                                                  |
| asyncio_websockets        | 552 ms                                                 | 558 ms: 1.01x slower                                                  |
| coroutines                | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                 |
| async_tree_io_tg          | 857 ms                                                 | 892 ms: 1.04x slower                                                  |
| async_tree_io             | 842 ms                                                 | 926 ms: 1.10x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 76.5 ms: 1.04x faster                                                 |
| nbody          | 87.0 ms                                                | 85.3 ms: 1.02x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.3 ms: 1.08x faster                                                 |
| regex_effbot   | 3.73 ms                                                | 3.54 ms: 1.06x faster                                                 |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 2.05 sec: 1.05x faster                                                |
| xml_etree_process    | 60.6 ms                                                | 58.8 ms: 1.03x faster                                                 |
| pickle_pure_python   | 310 us                                                 | 301 us: 1.03x faster                                                  |
| xml_etree_generate   | 86.7 ms                                                | 85.2 ms: 1.02x faster                                                 |
| json_dumps           | 10.6 ms                                                | 10.4 ms: 1.02x faster                                                 |
| unpickle_pure_python | 216 us                                                 | 212 us: 1.02x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 104 ms: 1.03x slower                                                  |
| json_loads           | 27.2 us                                                | 28.6 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                 |
| python_startup_no_site | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 21.5 ms: 1.09x faster                                                 |
| genshi_xml      | 50.9 ms                                                | 48.2 ms: 1.06x faster                                                 |
| django_template | 35.2 ms                                                | 33.7 ms: 1.04x faster                                                 |
| mako            | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| create_gc_cycles          | 2.41 ms                                                | 1.73 ms: 1.39x faster                                                 |
| deepcopy                  | 358 us                                                 | 260 us: 1.38x faster                                                  |
| deepcopy_memo             | 39.1 us                                                | 29.6 us: 1.32x faster                                                 |
| gc_traversal              | 4.37 ms                                                | 3.54 ms: 1.23x faster                                                 |
| go                        | 144 ms                                                 | 117 ms: 1.22x faster                                                  |
| deepcopy_reduce           | 3.20 us                                                | 2.66 us: 1.20x faster                                                 |
| python_startup            | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                 |
| async_tree_memoization_tg | 464 ms                                                 | 400 ms: 1.16x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 389 ms: 1.14x faster                                                  |
| pathlib                   | 17.5 ms                                                | 16.0 ms: 1.10x faster                                                 |
| genshi_text               | 23.5 ms                                                | 21.5 ms: 1.09x faster                                                 |
| mdp                       | 2.72 sec                                               | 2.50 sec: 1.09x faster                                                |
| async_tree_none           | 351 ms                                                 | 322 ms: 1.09x faster                                                  |
| regex_v8                  | 26.2 ms                                                | 24.3 ms: 1.08x faster                                                 |
| pycparser                 | 1.20 sec                                               | 1.13 sec: 1.07x faster                                                |
| richards_super            | 54.9 ms                                                | 51.6 ms: 1.06x faster                                                 |
| richards                  | 48.7 ms                                                | 45.9 ms: 1.06x faster                                                 |
| thrift                    | 809 us                                                 | 762 us: 1.06x faster                                                  |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.77 ms: 1.06x faster                                                 |
| genshi_xml                | 50.9 ms                                                | 48.2 ms: 1.06x faster                                                 |
| 2to3                      | 267 ms                                                 | 253 ms: 1.06x faster                                                  |
| regex_effbot              | 3.73 ms                                                | 3.54 ms: 1.06x faster                                                 |
| bench_thread_pool         | 822 us                                                 | 783 us: 1.05x faster                                                  |
| logging_format            | 6.40 us                                                | 6.10 us: 1.05x faster                                                 |
| tomli_loads               | 2.14 sec                                               | 2.05 sec: 1.05x faster                                                |
| generators                | 29.0 ms                                                | 27.7 ms: 1.05x faster                                                 |
| async_tree_none_tg        | 321 ms                                                 | 307 ms: 1.04x faster                                                  |
| django_template           | 35.2 ms                                                | 33.7 ms: 1.04x faster                                                 |
| pprint_pformat            | 1.49 sec                                               | 1.44 sec: 1.04x faster                                                |
| pprint_safe_repr          | 728 ms                                                 | 702 ms: 1.04x faster                                                  |
| float                     | 79.2 ms                                                | 76.5 ms: 1.04x faster                                                 |
| crypto_pyaes              | 75.3 ms                                                | 72.9 ms: 1.03x faster                                                 |
| xml_etree_process         | 60.6 ms                                                | 58.8 ms: 1.03x faster                                                 |
| tornado_http              | 92.4 ms                                                | 89.5 ms: 1.03x faster                                                 |
| pickle_pure_python        | 310 us                                                 | 301 us: 1.03x faster                                                  |
| meteor_contest            | 109 ms                                                 | 106 ms: 1.03x faster                                                  |
| sympy_str                 | 275 ms                                                 | 267 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 561 ms: 1.03x faster                                                  |
| spectral_norm             | 115 ms                                                 | 112 ms: 1.03x faster                                                  |
| regex_compile             | 132 ms                                                 | 129 ms: 1.03x faster                                                  |
| typing_runtime_protocols  | 165 us                                                 | 161 us: 1.03x faster                                                  |
| sympy_expand              | 463 ms                                                 | 452 ms: 1.03x faster                                                  |
| telco                     | 8.54 ms                                                | 8.34 ms: 1.02x faster                                                 |
| logging_simple            | 5.72 us                                                | 5.58 us: 1.02x faster                                                 |
| sympy_sum                 | 150 ms                                                 | 147 ms: 1.02x faster                                                  |
| raytrace                  | 267 ms                                                 | 261 ms: 1.02x faster                                                  |
| pyflate                   | 471 ms                                                 | 461 ms: 1.02x faster                                                  |
| sympy_integrate           | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                 |
| nbody                     | 87.0 ms                                                | 85.3 ms: 1.02x faster                                                 |
| xml_etree_generate        | 86.7 ms                                                | 85.2 ms: 1.02x faster                                                 |
| json_dumps                | 10.6 ms                                                | 10.4 ms: 1.02x faster                                                 |
| scimark_monte_carlo       | 67.4 ms                                                | 66.4 ms: 1.02x faster                                                 |
| unpickle_pure_python      | 216 us                                                 | 212 us: 1.02x faster                                                  |
| logging_silent            | 102 ns                                                 | 100 ns: 1.02x faster                                                  |
| json                      | 5.36 ms                                                | 5.31 ms: 1.01x faster                                                 |
| sqlglot_transpile         | 1.58 ms                                                | 1.57 ms: 1.01x faster                                                 |
| sqlglot_optimize          | 53.7 ms                                                | 53.5 ms: 1.01x faster                                                 |
| deltablue                 | 3.23 ms                                                | 3.22 ms: 1.00x faster                                                 |
| scimark_fft               | 364 ms                                                 | 363 ms: 1.00x faster                                                  |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| hexiom                    | 6.16 ms                                                | 6.19 ms: 1.00x slower                                                 |
| sqlglot_normalize         | 108 ms                                                 | 108 ms: 1.01x slower                                                  |
| async_generators          | 436 ms                                                 | 439 ms: 1.01x slower                                                  |
| asyncio_websockets        | 552 ms                                                 | 558 ms: 1.01x slower                                                  |
| bpe_tokeniser             | 4.75 sec                                               | 4.80 sec: 1.01x slower                                                |
| python_startup_no_site    | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                 |
| nqueens                   | 78.4 ms                                                | 79.8 ms: 1.02x slower                                                 |
| docutils                  | 2.59 sec                                               | 2.64 sec: 1.02x slower                                                |
| coverage                  | 84.0 ms                                                | 85.7 ms: 1.02x slower                                                 |
| coroutines                | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                 |
| xml_etree_iterparse       | 101 ms                                                 | 104 ms: 1.03x slower                                                  |
| mako                      | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                 |
| async_tree_io_tg          | 857 ms                                                 | 892 ms: 1.04x slower                                                  |
| json_loads                | 27.2 us                                                | 28.6 us: 1.05x slower                                                 |
| async_tree_io             | 842 ms                                                 | 926 ms: 1.10x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (12): async_tree_cpu_io_mixed_tg, fannkuch, html5lib, regex_dna, scimark_lu, bench_mp_pool, scimark_sor, xml_etree_parse, chaos, comprehensions, sqlglot_parse, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240829-3.14.0a0-c9a5962/bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.040x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x