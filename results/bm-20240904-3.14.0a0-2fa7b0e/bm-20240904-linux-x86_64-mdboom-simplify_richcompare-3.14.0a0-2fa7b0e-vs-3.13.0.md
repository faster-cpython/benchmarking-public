# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.028x faster
- HPT reliability: 99.24%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 257 ms: 1.04x faster                                                  |
| docutils       | 2.59 sec                                               | 2.66 sec: 1.03x slower                                                |
| html5lib       | 64.2 ms                                                | 63.5 ms: 1.01x faster                                                 |
| tornado_http   | 92.4 ms                                                | 90.7 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 405 ms: 1.14x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 394 ms: 1.12x faster                                                  |
| async_tree_none           | 351 ms                                                 | 327 ms: 1.07x faster                                                  |
| async_tree_none_tg        | 321 ms                                                 | 313 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 567 ms: 1.02x faster                                                  |
| asyncio_websockets        | 552 ms                                                 | 559 ms: 1.01x slower                                                  |
| async_generators          | 436 ms                                                 | 445 ms: 1.02x slower                                                  |
| async_tree_io_tg          | 857 ms                                                 | 908 ms: 1.06x slower                                                  |
| async_tree_io             | 842 ms                                                 | 937 ms: 1.11x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): coroutines, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 77.5 ms: 1.02x faster                                                 |
| nbody          | 87.0 ms                                                | 86.0 ms: 1.01x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 132 ms                                                 | 131 ms: 1.01x faster                                                  |
| regex_v8       | 26.2 ms                                                | 26.1 ms: 1.01x faster                                                 |
| regex_effbot   | 3.73 ms                                                | 3.77 ms: 1.01x slower                                                 |
| regex_dna      | 218 ms                                                 | 222 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 310 us                                                 | 301 us: 1.03x faster                                                  |
| unpickle_pure_python | 216 us                                                 | 210 us: 1.03x faster                                                  |
| xml_etree_process    | 60.6 ms                                                | 59.4 ms: 1.02x faster                                                 |
| tomli_loads          | 2.14 sec                                               | 2.10 sec: 1.02x faster                                                |
| xml_etree_generate   | 86.7 ms                                                | 86.0 ms: 1.01x faster                                                 |
| json_dumps           | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 106 ms: 1.05x slower                                                  |
| json_loads           | 27.2 us                                                | 28.7 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                 |
| python_startup_no_site | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 34.0 ms: 1.03x faster                                                 |
| genshi_text     | 23.5 ms                                                | 23.1 ms: 1.02x faster                                                 |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                  | 358 us                                                 | 260 us: 1.38x faster                                                  |
| create_gc_cycles          | 2.41 ms                                                | 1.76 ms: 1.37x faster                                                 |
| deepcopy_memo             | 39.1 us                                                | 30.3 us: 1.29x faster                                                 |
| go                        | 144 ms                                                 | 119 ms: 1.21x faster                                                  |
| deepcopy_reduce           | 3.20 us                                                | 2.65 us: 1.21x faster                                                 |
| python_startup            | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                 |
| gc_traversal              | 4.37 ms                                                | 3.72 ms: 1.17x faster                                                 |
| async_tree_memoization_tg | 464 ms                                                 | 405 ms: 1.14x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 394 ms: 1.12x faster                                                  |
| pathlib                   | 17.5 ms                                                | 16.0 ms: 1.09x faster                                                 |
| async_tree_none           | 351 ms                                                 | 327 ms: 1.07x faster                                                  |
| spectral_norm             | 115 ms                                                 | 108 ms: 1.07x faster                                                  |
| richards                  | 48.7 ms                                                | 45.7 ms: 1.07x faster                                                 |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.74 ms: 1.06x faster                                                 |
| richards_super            | 54.9 ms                                                | 51.8 ms: 1.06x faster                                                 |
| thrift                    | 809 us                                                 | 771 us: 1.05x faster                                                  |
| generators                | 29.0 ms                                                | 27.7 ms: 1.05x faster                                                 |
| logging_format            | 6.40 us                                                | 6.11 us: 1.05x faster                                                 |
| bench_thread_pool         | 822 us                                                 | 787 us: 1.04x faster                                                  |
| 2to3                      | 267 ms                                                 | 257 ms: 1.04x faster                                                  |
| logging_simple            | 5.72 us                                                | 5.51 us: 1.04x faster                                                 |
| django_template           | 35.2 ms                                                | 34.0 ms: 1.03x faster                                                 |
| pickle_pure_python        | 310 us                                                 | 301 us: 1.03x faster                                                  |
| mdp                       | 2.72 sec                                               | 2.64 sec: 1.03x faster                                                |
| unpickle_pure_python      | 216 us                                                 | 210 us: 1.03x faster                                                  |
| async_tree_none_tg        | 321 ms                                                 | 313 ms: 1.02x faster                                                  |
| telco                     | 8.54 ms                                                | 8.34 ms: 1.02x faster                                                 |
| crypto_pyaes              | 75.3 ms                                                | 73.6 ms: 1.02x faster                                                 |
| float                     | 79.2 ms                                                | 77.5 ms: 1.02x faster                                                 |
| xml_etree_process         | 60.6 ms                                                | 59.4 ms: 1.02x faster                                                 |
| typing_runtime_protocols  | 165 us                                                 | 161 us: 1.02x faster                                                  |
| sympy_str                 | 275 ms                                                 | 270 ms: 1.02x faster                                                  |
| genshi_text               | 23.5 ms                                                | 23.1 ms: 1.02x faster                                                 |
| tornado_http              | 92.4 ms                                                | 90.7 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 567 ms: 1.02x faster                                                  |
| tomli_loads               | 2.14 sec                                               | 2.10 sec: 1.02x faster                                                |
| sympy_integrate           | 19.9 ms                                                | 19.6 ms: 1.02x faster                                                 |
| pprint_safe_repr          | 728 ms                                                 | 717 ms: 1.02x faster                                                  |
| pycparser                 | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                |
| pprint_pformat            | 1.49 sec                                               | 1.47 sec: 1.02x faster                                                |
| sympy_sum                 | 150 ms                                                 | 148 ms: 1.01x faster                                                  |
| raytrace                  | 267 ms                                                 | 263 ms: 1.01x faster                                                  |
| scimark_fft               | 364 ms                                                 | 360 ms: 1.01x faster                                                  |
| regex_compile             | 132 ms                                                 | 131 ms: 1.01x faster                                                  |
| html5lib                  | 64.2 ms                                                | 63.5 ms: 1.01x faster                                                 |
| nbody                     | 87.0 ms                                                | 86.0 ms: 1.01x faster                                                 |
| meteor_contest            | 109 ms                                                 | 108 ms: 1.01x faster                                                  |
| xml_etree_generate        | 86.7 ms                                                | 86.0 ms: 1.01x faster                                                 |
| deltablue                 | 3.23 ms                                                | 3.21 ms: 1.01x faster                                                 |
| json_dumps                | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| regex_v8                  | 26.2 ms                                                | 26.1 ms: 1.01x faster                                                 |
| logging_silent            | 102 ns                                                 | 101 ns: 1.00x faster                                                  |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| regex_effbot              | 3.73 ms                                                | 3.77 ms: 1.01x slower                                                 |
| chaos                     | 58.1 ms                                                | 58.7 ms: 1.01x slower                                                 |
| sqlglot_normalize         | 108 ms                                                 | 109 ms: 1.01x slower                                                  |
| sqlglot_parse             | 1.27 ms                                                | 1.29 ms: 1.01x slower                                                 |
| asyncio_websockets        | 552 ms                                                 | 559 ms: 1.01x slower                                                  |
| comprehensions            | 16.5 us                                                | 16.7 us: 1.01x slower                                                 |
| mako                      | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                 |
| python_startup_no_site    | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                 |
| regex_dna                 | 218 ms                                                 | 222 ms: 1.02x slower                                                  |
| scimark_monte_carlo       | 67.4 ms                                                | 68.7 ms: 1.02x slower                                                 |
| scimark_sor               | 124 ms                                                 | 126 ms: 1.02x slower                                                  |
| coverage                  | 84.0 ms                                                | 85.7 ms: 1.02x slower                                                 |
| hexiom                    | 6.16 ms                                                | 6.29 ms: 1.02x slower                                                 |
| async_generators          | 436 ms                                                 | 445 ms: 1.02x slower                                                  |
| scimark_lu                | 113 ms                                                 | 115 ms: 1.02x slower                                                  |
| bpe_tokeniser             | 4.75 sec                                               | 4.86 sec: 1.02x slower                                                |
| docutils                  | 2.59 sec                                               | 2.66 sec: 1.03x slower                                                |
| nqueens                   | 78.4 ms                                                | 80.7 ms: 1.03x slower                                                 |
| xml_etree_iterparse       | 101 ms                                                 | 106 ms: 1.05x slower                                                  |
| json_loads                | 27.2 us                                                | 28.7 us: 1.05x slower                                                 |
| async_tree_io_tg          | 857 ms                                                 | 908 ms: 1.06x slower                                                  |
| async_tree_io             | 842 ms                                                 | 937 ms: 1.11x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (12): json, sympy_expand, fannkuch, xml_etree_parse, genshi_xml, coroutines, sqlglot_transpile, pyflate, sqlglot_optimize, bench_mp_pool, async_tree_cpu_io_mixed_tg, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240904-3.14.0a0-2fa7b0e/bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.028x faster
# HPT report

- Reliability score: 99.24% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x