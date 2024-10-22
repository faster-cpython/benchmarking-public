# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.01x faster
- HPT reliability: 62.47%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 257 ms: 1.03x faster                                                  |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                |
| html5lib       | 64.5 ms                                                | 63.5 ms: 1.02x faster                                                 |
| tornado_http   | 91.5 ms                                                | 90.7 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 405 ms: 1.15x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 394 ms: 1.12x faster                                                  |
| async_tree_none           | 354 ms                                                 | 327 ms: 1.08x faster                                                  |
| async_tree_none_tg        | 320 ms                                                 | 313 ms: 1.02x faster                                                  |
| asyncio_tcp               | 488 ms                                                 | 479 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 567 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                |
| asyncio_websockets        | 555 ms                                                 | 559 ms: 1.01x slower                                                  |
| async_generators          | 433 ms                                                 | 445 ms: 1.03x slower                                                  |
| async_tree_io_tg          | 825 ms                                                 | 908 ms: 1.10x slower                                                  |
| async_tree_io             | 843 ms                                                 | 937 ms: 1.11x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): coroutines, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 77.5 ms: 1.01x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.77 ms: 1.03x faster                                                 |
| regex_compile  | 131 ms                                                 | 131 ms: 1.00x faster                                                  |
| regex_dna      | 220 ms                                                 | 222 ms: 1.01x slower                                                  |
| regex_v8       | 25.3 ms                                                | 26.1 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 59.4 ms: 1.02x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 210 us: 1.02x faster                                                  |
| xml_etree_generate   | 87.0 ms                                                | 86.0 ms: 1.01x faster                                                 |
| tomli_loads          | 2.11 sec                                               | 2.10 sec: 1.00x faster                                                |
| pickle_pure_python   | 300 us                                                 | 301 us: 1.00x slower                                                  |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                 |
| xml_etree_iterparse  | 102 ms                                                 | 106 ms: 1.04x slower                                                  |
| json_loads           | 27.0 us                                                | 28.7 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 34.0 ms: 1.01x faster                                                 |
| genshi_text     | 22.9 ms                                                | 23.1 ms: 1.01x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 50.9 ms: 1.01x slower                                                 |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 260 us: 1.35x faster                                                  |
| deepcopy_memo             | 38.0 us                                                | 30.3 us: 1.25x faster                                                 |
| deepcopy_reduce           | 3.17 us                                                | 2.65 us: 1.19x faster                                                 |
| go                        | 142 ms                                                 | 119 ms: 1.19x faster                                                  |
| async_tree_memoization_tg | 465 ms                                                 | 405 ms: 1.15x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 394 ms: 1.12x faster                                                  |
| async_tree_none           | 354 ms                                                 | 327 ms: 1.08x faster                                                  |
| pathlib                   | 17.1 ms                                                | 16.0 ms: 1.06x faster                                                 |
| spectral_norm             | 115 ms                                                 | 108 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.74 ms: 1.06x faster                                                 |
| richards                  | 48.1 ms                                                | 45.7 ms: 1.05x faster                                                 |
| richards_super            | 54.4 ms                                                | 51.8 ms: 1.05x faster                                                 |
| generators                | 28.8 ms                                                | 27.7 ms: 1.04x faster                                                 |
| pprint_safe_repr          | 744 ms                                                 | 717 ms: 1.04x faster                                                  |
| mdp                       | 2.74 sec                                               | 2.64 sec: 1.04x faster                                                |
| bench_thread_pool         | 815 us                                                 | 787 us: 1.04x faster                                                  |
| thrift                    | 796 us                                                 | 771 us: 1.03x faster                                                  |
| 2to3                      | 265 ms                                                 | 257 ms: 1.03x faster                                                  |
| regex_effbot              | 3.88 ms                                                | 3.77 ms: 1.03x faster                                                 |
| logging_simple            | 5.66 us                                                | 5.51 us: 1.03x faster                                                 |
| pprint_pformat            | 1.51 sec                                               | 1.47 sec: 1.03x faster                                                |
| scimark_fft               | 369 ms                                                 | 360 ms: 1.02x faster                                                  |
| logging_format            | 6.25 us                                                | 6.11 us: 1.02x faster                                                 |
| async_tree_none_tg        | 320 ms                                                 | 313 ms: 1.02x faster                                                  |
| gc_traversal              | 3.81 ms                                                | 3.72 ms: 1.02x faster                                                 |
| asyncio_tcp               | 488 ms                                                 | 479 ms: 1.02x faster                                                  |
| xml_etree_process         | 60.4 ms                                                | 59.4 ms: 1.02x faster                                                 |
| html5lib                  | 64.5 ms                                                | 63.5 ms: 1.02x faster                                                 |
| sympy_integrate           | 19.9 ms                                                | 19.6 ms: 1.02x faster                                                 |
| unpickle_pure_python      | 213 us                                                 | 210 us: 1.02x faster                                                  |
| sympy_str                 | 274 ms                                                 | 270 ms: 1.02x faster                                                  |
| telco                     | 8.45 ms                                                | 8.34 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 567 ms: 1.01x faster                                                  |
| float                     | 78.5 ms                                                | 77.5 ms: 1.01x faster                                                 |
| django_template           | 34.4 ms                                                | 34.0 ms: 1.01x faster                                                 |
| xml_etree_generate        | 87.0 ms                                                | 86.0 ms: 1.01x faster                                                 |
| sympy_sum                 | 150 ms                                                 | 148 ms: 1.01x faster                                                  |
| tornado_http              | 91.5 ms                                                | 90.7 ms: 1.01x faster                                                 |
| pycparser                 | 1.19 sec                                               | 1.18 sec: 1.01x faster                                                |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| tomli_loads               | 2.11 sec                                               | 2.10 sec: 1.00x faster                                                |
| regex_compile             | 131 ms                                                 | 131 ms: 1.00x faster                                                  |
| sqlglot_optimize          | 53.9 ms                                                | 53.8 ms: 1.00x faster                                                 |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                |
| meteor_contest            | 108 ms                                                 | 108 ms: 1.00x slower                                                  |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| pickle_pure_python        | 300 us                                                 | 301 us: 1.00x slower                                                  |
| chaos                     | 58.4 ms                                                | 58.7 ms: 1.00x slower                                                 |
| sqlglot_transpile         | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                 |
| raytrace                  | 262 ms                                                 | 263 ms: 1.01x slower                                                  |
| asyncio_websockets        | 555 ms                                                 | 559 ms: 1.01x slower                                                  |
| json_dumps                | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                 |
| crypto_pyaes              | 73.0 ms                                                | 73.6 ms: 1.01x slower                                                 |
| genshi_text               | 22.9 ms                                                | 23.1 ms: 1.01x slower                                                 |
| genshi_xml                | 50.3 ms                                                | 50.9 ms: 1.01x slower                                                 |
| python_startup_no_site    | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                 |
| regex_dna                 | 220 ms                                                 | 222 ms: 1.01x slower                                                  |
| mako                      | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                 |
| typing_runtime_protocols  | 159 us                                                 | 161 us: 1.01x slower                                                  |
| sqlglot_normalize         | 107 ms                                                 | 109 ms: 1.01x slower                                                  |
| deltablue                 | 3.15 ms                                                | 3.21 ms: 1.02x slower                                                 |
| comprehensions            | 16.4 us                                                | 16.7 us: 1.02x slower                                                 |
| sqlglot_parse             | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                 |
| json                      | 5.20 ms                                                | 5.32 ms: 1.02x slower                                                 |
| coverage                  | 83.7 ms                                                | 85.7 ms: 1.02x slower                                                 |
| pyflate                   | 460 ms                                                 | 471 ms: 1.02x slower                                                  |
| hexiom                    | 6.13 ms                                                | 6.29 ms: 1.03x slower                                                 |
| async_generators          | 433 ms                                                 | 445 ms: 1.03x slower                                                  |
| scimark_sor               | 122 ms                                                 | 126 ms: 1.03x slower                                                  |
| docutils                  | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                |
| regex_v8                  | 25.3 ms                                                | 26.1 ms: 1.03x slower                                                 |
| bpe_tokeniser             | 4.69 sec                                               | 4.86 sec: 1.04x slower                                                |
| scimark_monte_carlo       | 66.3 ms                                                | 68.7 ms: 1.04x slower                                                 |
| xml_etree_iterparse       | 102 ms                                                 | 106 ms: 1.04x slower                                                  |
| fannkuch                  | 381 ms                                                 | 403 ms: 1.06x slower                                                  |
| json_loads                | 27.0 us                                                | 28.7 us: 1.06x slower                                                 |
| create_gc_cycles          | 1.61 ms                                                | 1.76 ms: 1.09x slower                                                 |
| async_tree_io_tg          | 825 ms                                                 | 908 ms: 1.10x slower                                                  |
| async_tree_io             | 843 ms                                                 | 937 ms: 1.11x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (10): logging_silent, xml_etree_parse, sympy_expand, bench_mp_pool, nqueens, scimark_lu, nbody, coroutines, async_tree_cpu_io_mixed_tg, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 62.47% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x