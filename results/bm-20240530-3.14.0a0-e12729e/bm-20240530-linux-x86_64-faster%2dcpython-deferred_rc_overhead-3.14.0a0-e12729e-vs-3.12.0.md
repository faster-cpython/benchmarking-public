# Results vs. 3.12.0

- fork: faster-cpython
- ref: deferred_rc_overhead
- machine: linux-x86_64
- commit hash: e12729e
- commit date: 2024-05-30
- overall geometric mean: 1.02x faster
- HPT reliability: 92.79%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 274 ms: 1.00x faster                                                            |
| docutils       | 2.77 sec                                               | 2.81 sec: 1.02x slower                                                          |
| tornado_http   | 103 ms                                                 | 94.3 ms: 1.09x faster                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 356 ms: 1.26x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 457 ms: 1.26x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 593 ms: 1.22x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 951 ms: 1.22x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 973 ms: 1.22x faster                                                            |
| async_tree_none            | 472 ms                                                 | 389 ms: 1.21x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 480 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 622 ms: 1.17x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 79.6 ms: 1.06x faster                                                           |
| nbody          | 97.0 ms                                                | 92.4 ms: 1.05x faster                                                           |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 137 ms: 1.08x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.80 ms: 1.05x slower                                                           |
| regex_dna      | 212 ms                                                 | 226 ms: 1.06x slower                                                            |
| regex_v8       | 23.1 ms                                                | 24.6 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.22 sec: 1.05x faster                                                          |
| unpickle             | 15.9 us                                                | 15.3 us: 1.04x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 313 us: 1.03x faster                                                            |
| unpickle_pure_python | 230 us                                                 | 225 us: 1.02x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 88.3 ms: 1.01x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 61.3 ms: 1.01x faster                                                           |
| pickle_dict          | 35.5 us                                                | 35.3 us: 1.01x faster                                                           |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 108 ms: 1.01x slower                                                            |
| pickle_list          | 5.08 us                                                | 5.14 us: 1.01x slower                                                           |
| json_loads           | 28.5 us                                                | 28.9 us: 1.02x slower                                                           |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                           |
| unpickle_list        | 5.29 us                                                | 5.43 us: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.4 ms: 1.05x faster                                                           |
| django_template | 34.6 ms                                                | 35.8 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                           |
| async_tree_none_tg         | 450 ms                                                 | 356 ms: 1.26x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 457 ms: 1.26x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 593 ms: 1.22x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 951 ms: 1.22x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 973 ms: 1.22x faster                                                            |
| async_tree_none            | 472 ms                                                 | 389 ms: 1.21x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 480 ms: 1.20x faster                                                            |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 622 ms: 1.17x faster                                                            |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                            |
| logging_format             | 7.23 us                                                | 6.47 us: 1.12x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.33 ms: 1.12x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.80 us: 1.11x faster                                                           |
| tornado_http               | 103 ms                                                 | 94.3 ms: 1.09x faster                                                           |
| regex_compile              | 148 ms                                                 | 137 ms: 1.08x faster                                                            |
| sympy_sum                  | 169 ms                                                 | 157 ms: 1.08x faster                                                            |
| chaos                      | 67.0 ms                                                | 62.6 ms: 1.07x faster                                                           |
| float                      | 84.7 ms                                                | 79.6 ms: 1.06x faster                                                           |
| sympy_str                  | 300 ms                                                 | 284 ms: 1.05x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 78.0 ms: 1.05x faster                                                           |
| nbody                      | 97.0 ms                                                | 92.4 ms: 1.05x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.22 sec: 1.05x faster                                                          |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.05x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 71.9 ms: 1.05x faster                                                           |
| generators                 | 31.2 ms                                                | 29.9 ms: 1.05x faster                                                           |
| unpickle                   | 15.9 us                                                | 15.3 us: 1.04x faster                                                           |
| sympy_integrate            | 21.4 ms                                                | 20.7 ms: 1.04x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 313 us: 1.03x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 66.6 ms: 1.03x faster                                                           |
| fannkuch                   | 417 ms                                                 | 406 ms: 1.03x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 225 us: 1.02x faster                                                            |
| async_generators           | 463 ms                                                 | 452 ms: 1.02x faster                                                            |
| gc_traversal               | 3.79 ms                                                | 3.72 ms: 1.02x faster                                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.65 ms: 1.02x faster                                                           |
| mdp                        | 2.63 sec                                               | 2.59 sec: 1.02x faster                                                          |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                          |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                            |
| scimark_sor                | 129 ms                                                 | 128 ms: 1.01x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 88.3 ms: 1.01x faster                                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.35 ms: 1.01x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 61.3 ms: 1.01x faster                                                           |
| pickle_dict                | 35.5 us                                                | 35.3 us: 1.01x faster                                                           |
| bench_thread_pool          | 842 us                                                 | 836 us: 1.01x faster                                                            |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.00x faster                                                           |
| meteor_contest             | 112 ms                                                 | 112 ms: 1.00x faster                                                            |
| 2to3                       | 274 ms                                                 | 274 ms: 1.00x faster                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.57 sec: 1.00x slower                                                          |
| scimark_fft                | 382 ms                                                 | 384 ms: 1.01x slower                                                            |
| deepcopy                   | 371 us                                                 | 374 us: 1.01x slower                                                            |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                           |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 108 ms: 1.01x slower                                                            |
| pyflate                    | 482 ms                                                 | 488 ms: 1.01x slower                                                            |
| pickle_list                | 5.08 us                                                | 5.14 us: 1.01x slower                                                           |
| json_loads                 | 28.5 us                                                | 28.9 us: 1.02x slower                                                           |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                            |
| docutils                   | 2.77 sec                                               | 2.81 sec: 1.02x slower                                                          |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.02x slower                                                            |
| deepcopy_memo              | 40.7 us                                                | 41.5 us: 1.02x slower                                                           |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                           |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                           |
| coroutines                 | 23.2 ms                                                | 23.7 ms: 1.02x slower                                                           |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.02x slower                                                            |
| asyncio_websockets         | 551 ms                                                 | 566 ms: 1.03x slower                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 56.3 ms: 1.03x slower                                                           |
| unpickle_list              | 5.29 us                                                | 5.43 us: 1.03x slower                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.03x slower                                                          |
| django_template            | 34.6 ms                                                | 35.8 ms: 1.04x slower                                                           |
| asyncio_tcp                | 491 ms                                                 | 508 ms: 1.04x slower                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.25 ms: 1.04x slower                                                           |
| sqlite_synth               | 2.83 us                                                | 2.98 us: 1.05x slower                                                           |
| regex_effbot               | 3.61 ms                                                | 3.80 ms: 1.05x slower                                                           |
| go                         | 139 ms                                                 | 147 ms: 1.06x slower                                                            |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.06x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 24.6 ms: 1.06x slower                                                           |
| richards                   | 45.8 ms                                                | 49.8 ms: 1.09x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                                            |
| richards_super             | 51.5 ms                                                | 56.2 ms: 1.09x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                           |
| telco                      | 7.10 ms                                                | 8.60 ms: 1.21x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.79 ms: 1.21x slower                                                           |
| coverage                   | 72.7 ms                                                | 93.6 ms: 1.29x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (8): dask, pprint_safe_repr, sympy_expand, nqueens, xml_etree_parse, hexiom, deepcopy_reduce, json
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240530-3.14.0a0-e12729e/bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 92.79% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x