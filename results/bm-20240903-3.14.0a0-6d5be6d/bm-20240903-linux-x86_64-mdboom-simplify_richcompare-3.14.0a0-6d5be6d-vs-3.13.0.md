# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.01x faster
- HPT reliability: 92.04%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 257 ms: 1.03x faster                                                  |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                |
| html5lib       | 64.5 ms                                                | 61.8 ms: 1.04x faster                                                 |
| tornado_http   | 91.5 ms                                                | 90.8 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 401 ms: 1.16x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 390 ms: 1.13x faster                                                  |
| async_tree_none           | 354 ms                                                 | 321 ms: 1.10x faster                                                  |
| async_tree_none_tg        | 320 ms                                                 | 308 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 560 ms: 1.03x faster                                                  |
| asyncio_tcp               | 488 ms                                                 | 482 ms: 1.01x faster                                                  |
| async_generators          | 433 ms                                                 | 431 ms: 1.00x faster                                                  |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                  |
| coroutines                | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                 |
| async_tree_io_tg          | 825 ms                                                 | 896 ms: 1.09x slower                                                  |
| async_tree_io             | 843 ms                                                 | 928 ms: 1.10x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 77.8 ms: 1.01x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.76 ms: 1.03x faster                                                 |
| regex_compile  | 131 ms                                                 | 130 ms: 1.01x faster                                                  |
| regex_dna      | 220 ms                                                 | 225 ms: 1.02x slower                                                  |
| regex_v8       | 25.3 ms                                                | 26.8 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 2.05 sec: 1.03x faster                                                |
| xml_etree_process    | 60.4 ms                                                | 58.8 ms: 1.03x faster                                                 |
| xml_etree_generate   | 87.0 ms                                                | 84.9 ms: 1.02x faster                                                 |
| xml_etree_parse      | 156 ms                                                 | 154 ms: 1.01x faster                                                  |
| pickle_pure_python   | 300 us                                                 | 302 us: 1.01x slower                                                  |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                 |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                  |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.03x slower                                                  |
| json_loads           | 27.0 us                                                | 28.6 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 33.5 ms: 1.03x faster                                                 |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 51.5 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 264 us: 1.34x faster                                                  |
| deepcopy_memo             | 38.0 us                                                | 29.8 us: 1.28x faster                                                 |
| go                        | 142 ms                                                 | 119 ms: 1.19x faster                                                  |
| async_tree_memoization_tg | 465 ms                                                 | 401 ms: 1.16x faster                                                  |
| deepcopy_reduce           | 3.17 us                                                | 2.75 us: 1.15x faster                                                 |
| async_tree_memoization    | 442 ms                                                 | 390 ms: 1.13x faster                                                  |
| async_tree_none           | 354 ms                                                 | 321 ms: 1.10x faster                                                  |
| mdp                       | 2.74 sec                                               | 2.57 sec: 1.07x faster                                                |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.77 ms: 1.05x faster                                                 |
| richards_super            | 54.4 ms                                                | 51.7 ms: 1.05x faster                                                 |
| pathlib                   | 17.1 ms                                                | 16.2 ms: 1.05x faster                                                 |
| richards                  | 48.1 ms                                                | 46.0 ms: 1.05x faster                                                 |
| html5lib                  | 64.5 ms                                                | 61.8 ms: 1.04x faster                                                 |
| pprint_safe_repr          | 744 ms                                                 | 714 ms: 1.04x faster                                                  |
| async_tree_none_tg        | 320 ms                                                 | 308 ms: 1.04x faster                                                  |
| generators                | 28.8 ms                                                | 27.8 ms: 1.04x faster                                                 |
| bench_thread_pool         | 815 us                                                 | 787 us: 1.04x faster                                                  |
| 2to3                      | 265 ms                                                 | 257 ms: 1.03x faster                                                  |
| regex_effbot              | 3.88 ms                                                | 3.76 ms: 1.03x faster                                                 |
| tomli_loads               | 2.11 sec                                               | 2.05 sec: 1.03x faster                                                |
| pprint_pformat            | 1.51 sec                                               | 1.47 sec: 1.03x faster                                                |
| xml_etree_process         | 60.4 ms                                                | 58.8 ms: 1.03x faster                                                 |
| django_template           | 34.4 ms                                                | 33.5 ms: 1.03x faster                                                 |
| logging_simple            | 5.66 us                                                | 5.52 us: 1.03x faster                                                 |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 560 ms: 1.03x faster                                                  |
| xml_etree_generate        | 87.0 ms                                                | 84.9 ms: 1.02x faster                                                 |
| thrift                    | 796 us                                                 | 778 us: 1.02x faster                                                  |
| spectral_norm             | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| sympy_integrate           | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                 |
| telco                     | 8.45 ms                                                | 8.31 ms: 1.02x faster                                                 |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| scimark_fft               | 369 ms                                                 | 363 ms: 1.01x faster                                                  |
| xml_etree_parse           | 156 ms                                                 | 154 ms: 1.01x faster                                                  |
| sympy_str                 | 274 ms                                                 | 270 ms: 1.01x faster                                                  |
| logging_format            | 6.25 us                                                | 6.17 us: 1.01x faster                                                 |
| asyncio_tcp               | 488 ms                                                 | 482 ms: 1.01x faster                                                  |
| sqlglot_optimize          | 53.9 ms                                                | 53.4 ms: 1.01x faster                                                 |
| regex_compile             | 131 ms                                                 | 130 ms: 1.01x faster                                                  |
| scimark_lu                | 115 ms                                                 | 114 ms: 1.01x faster                                                  |
| float                     | 78.5 ms                                                | 77.8 ms: 1.01x faster                                                 |
| tornado_http              | 91.5 ms                                                | 90.8 ms: 1.01x faster                                                 |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| gc_traversal              | 3.81 ms                                                | 3.78 ms: 1.01x faster                                                 |
| crypto_pyaes              | 73.0 ms                                                | 72.4 ms: 1.01x faster                                                 |
| sympy_sum                 | 150 ms                                                 | 149 ms: 1.01x faster                                                  |
| async_generators          | 433 ms                                                 | 431 ms: 1.00x faster                                                  |
| nqueens                   | 80.6 ms                                                | 80.4 ms: 1.00x faster                                                 |
| pidigits                  | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                  |
| chaos                     | 58.4 ms                                                | 58.7 ms: 1.01x slower                                                 |
| comprehensions            | 16.4 us                                                | 16.5 us: 1.01x slower                                                 |
| sqlglot_transpile         | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                 |
| mako                      | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                 |
| pickle_pure_python        | 300 us                                                 | 302 us: 1.01x slower                                                  |
| python_startup_no_site    | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                 |
| raytrace                  | 262 ms                                                 | 264 ms: 1.01x slower                                                  |
| json_dumps                | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                 |
| hexiom                    | 6.13 ms                                                | 6.19 ms: 1.01x slower                                                 |
| unpickle_pure_python      | 213 us                                                 | 216 us: 1.01x slower                                                  |
| json                      | 5.20 ms                                                | 5.27 ms: 1.01x slower                                                 |
| coverage                  | 83.7 ms                                                | 84.9 ms: 1.01x slower                                                 |
| deltablue                 | 3.15 ms                                                | 3.20 ms: 1.02x slower                                                 |
| sqlglot_parse             | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                 |
| bpe_tokeniser             | 4.69 sec                                               | 4.79 sec: 1.02x slower                                                |
| regex_dna                 | 220 ms                                                 | 225 ms: 1.02x slower                                                  |
| coroutines                | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                 |
| genshi_xml                | 50.3 ms                                                | 51.5 ms: 1.02x slower                                                 |
| xml_etree_iterparse       | 102 ms                                                 | 105 ms: 1.03x slower                                                  |
| scimark_sor               | 122 ms                                                 | 126 ms: 1.03x slower                                                  |
| scimark_monte_carlo       | 66.3 ms                                                | 68.2 ms: 1.03x slower                                                 |
| docutils                  | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                |
| typing_runtime_protocols  | 159 us                                                 | 165 us: 1.04x slower                                                  |
| pyflate                   | 460 ms                                                 | 478 ms: 1.04x slower                                                  |
| json_loads                | 27.0 us                                                | 28.6 us: 1.06x slower                                                 |
| regex_v8                  | 25.3 ms                                                | 26.8 ms: 1.06x slower                                                 |
| fannkuch                  | 381 ms                                                 | 407 ms: 1.07x slower                                                  |
| create_gc_cycles          | 1.61 ms                                                | 1.74 ms: 1.08x slower                                                 |
| async_tree_io_tg          | 825 ms                                                 | 896 ms: 1.09x slower                                                  |
| async_tree_io             | 843 ms                                                 | 928 ms: 1.10x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (10): sympy_expand, async_tree_cpu_io_mixed_tg, bench_mp_pool, nbody, asyncio_tcp_ssl, sqlglot_normalize, logging_silent, pycparser, genshi_text, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 92.04% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x