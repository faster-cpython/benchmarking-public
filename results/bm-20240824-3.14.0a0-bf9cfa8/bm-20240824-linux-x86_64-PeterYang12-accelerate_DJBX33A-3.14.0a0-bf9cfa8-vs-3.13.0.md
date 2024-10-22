# Results vs. 3.13.0

- fork: PeterYang12
- ref: accelerate_DJBX33A
- machine: linux-x86_64
- commit hash: bf9cfa8
- commit date: 2024-08-24
- overall geometric mean: 1.02x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 254 ms: 1.04x faster                                                     |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                   |
| tornado_http   | 91.5 ms                                                | 90.2 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|---------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 401 ms: 1.16x faster                                                     |
| async_tree_memoization    | 442 ms                                                 | 388 ms: 1.14x faster                                                     |
| async_tree_none           | 354 ms                                                 | 321 ms: 1.10x faster                                                     |
| async_tree_none_tg        | 320 ms                                                 | 306 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 556 ms: 1.03x faster                                                     |
| asyncio_tcp               | 488 ms                                                 | 479 ms: 1.02x faster                                                     |
| async_generators          | 433 ms                                                 | 431 ms: 1.00x faster                                                     |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                   |
| asyncio_websockets        | 555 ms                                                 | 559 ms: 1.01x slower                                                     |
| coroutines                | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                    |
| async_tree_io_tg          | 825 ms                                                 | 896 ms: 1.09x slower                                                     |
| async_tree_io             | 843 ms                                                 | 926 ms: 1.10x slower                                                     |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                             |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 76.9 ms: 1.02x faster                                                    |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.48 ms: 1.12x faster                                                    |
| regex_compile  | 131 ms                                                 | 126 ms: 1.04x faster                                                     |
| regex_v8       | 25.3 ms                                                | 25.0 ms: 1.01x faster                                                    |
| regex_dna      | 220 ms                                                 | 219 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 58.3 ms: 1.04x faster                                                    |
| xml_etree_generate   | 87.0 ms                                                | 84.6 ms: 1.03x faster                                                    |
| tomli_loads          | 2.11 sec                                               | 2.07 sec: 1.02x faster                                                   |
| unpickle_pure_python | 213 us                                                 | 211 us: 1.01x faster                                                     |
| pickle_pure_python   | 300 us                                                 | 298 us: 1.01x faster                                                     |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.03x slower                                                     |
| json_loads           | 27.0 us                                                | 28.6 us: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                    |
| python_startup_no_site | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 21.5 ms: 1.06x faster                                                    |
| genshi_xml      | 50.3 ms                                                | 48.6 ms: 1.04x faster                                                    |
| django_template | 34.4 ms                                                | 33.8 ms: 1.02x faster                                                    |
| mako            | 11.1 ms                                                | 11.4 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                             |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|---------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 261 us: 1.35x faster                                                     |
| deepcopy_memo             | 38.0 us                                                | 29.0 us: 1.31x faster                                                    |
| deepcopy_reduce           | 3.17 us                                                | 2.72 us: 1.16x faster                                                    |
| async_tree_memoization_tg | 465 ms                                                 | 401 ms: 1.16x faster                                                     |
| async_tree_memoization    | 442 ms                                                 | 388 ms: 1.14x faster                                                     |
| regex_effbot              | 3.88 ms                                                | 3.48 ms: 1.12x faster                                                    |
| async_tree_none           | 354 ms                                                 | 321 ms: 1.10x faster                                                     |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.55 ms: 1.10x faster                                                    |
| logging_silent            | 102 ns                                                 | 94.5 ns: 1.08x faster                                                    |
| pathlib                   | 17.1 ms                                                | 15.9 ms: 1.08x faster                                                    |
| genshi_text               | 22.9 ms                                                | 21.5 ms: 1.06x faster                                                    |
| richards_super            | 54.4 ms                                                | 51.7 ms: 1.05x faster                                                    |
| richards                  | 48.1 ms                                                | 45.8 ms: 1.05x faster                                                    |
| async_tree_none_tg        | 320 ms                                                 | 306 ms: 1.05x faster                                                     |
| spectral_norm             | 115 ms                                                 | 110 ms: 1.05x faster                                                     |
| bench_thread_pool         | 815 us                                                 | 780 us: 1.04x faster                                                     |
| pprint_safe_repr          | 744 ms                                                 | 714 ms: 1.04x faster                                                     |
| pycparser                 | 1.19 sec                                               | 1.14 sec: 1.04x faster                                                   |
| 2to3                      | 265 ms                                                 | 254 ms: 1.04x faster                                                     |
| regex_compile             | 131 ms                                                 | 126 ms: 1.04x faster                                                     |
| pprint_pformat            | 1.51 sec                                               | 1.46 sec: 1.04x faster                                                   |
| thrift                    | 796 us                                                 | 768 us: 1.04x faster                                                     |
| genshi_xml                | 50.3 ms                                                | 48.6 ms: 1.04x faster                                                    |
| xml_etree_process         | 60.4 ms                                                | 58.3 ms: 1.04x faster                                                    |
| mdp                       | 2.74 sec                                               | 2.65 sec: 1.04x faster                                                   |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 556 ms: 1.03x faster                                                     |
| generators                | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                    |
| xml_etree_generate        | 87.0 ms                                                | 84.6 ms: 1.03x faster                                                    |
| scimark_fft               | 369 ms                                                 | 359 ms: 1.03x faster                                                     |
| sympy_str                 | 274 ms                                                 | 267 ms: 1.03x faster                                                     |
| gc_traversal              | 3.81 ms                                                | 3.72 ms: 1.02x faster                                                    |
| sympy_integrate           | 19.9 ms                                                | 19.4 ms: 1.02x faster                                                    |
| scimark_lu                | 115 ms                                                 | 113 ms: 1.02x faster                                                     |
| tomli_loads               | 2.11 sec                                               | 2.07 sec: 1.02x faster                                                   |
| float                     | 78.5 ms                                                | 76.9 ms: 1.02x faster                                                    |
| asyncio_tcp               | 488 ms                                                 | 479 ms: 1.02x faster                                                     |
| django_template           | 34.4 ms                                                | 33.8 ms: 1.02x faster                                                    |
| sympy_sum                 | 150 ms                                                 | 147 ms: 1.02x faster                                                     |
| sqlglot_optimize          | 53.9 ms                                                | 53.1 ms: 1.02x faster                                                    |
| sympy_expand              | 462 ms                                                 | 455 ms: 1.02x faster                                                     |
| tornado_http              | 91.5 ms                                                | 90.2 ms: 1.01x faster                                                    |
| telco                     | 8.45 ms                                                | 8.34 ms: 1.01x faster                                                    |
| pyflate                   | 460 ms                                                 | 454 ms: 1.01x faster                                                     |
| unpickle_pure_python      | 213 us                                                 | 211 us: 1.01x faster                                                     |
| nqueens                   | 80.6 ms                                                | 79.7 ms: 1.01x faster                                                    |
| sqlglot_normalize         | 107 ms                                                 | 106 ms: 1.01x faster                                                     |
| regex_v8                  | 25.3 ms                                                | 25.0 ms: 1.01x faster                                                    |
| raytrace                  | 262 ms                                                 | 259 ms: 1.01x faster                                                     |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                    |
| pickle_pure_python        | 300 us                                                 | 298 us: 1.01x faster                                                     |
| crypto_pyaes              | 73.0 ms                                                | 72.4 ms: 1.01x faster                                                    |
| sqlglot_transpile         | 1.57 ms                                                | 1.56 ms: 1.01x faster                                                    |
| meteor_contest            | 108 ms                                                 | 107 ms: 1.01x faster                                                     |
| chaos                     | 58.4 ms                                                | 58.0 ms: 1.01x faster                                                    |
| logging_simple            | 5.66 us                                                | 5.62 us: 1.01x faster                                                    |
| async_generators          | 433 ms                                                 | 431 ms: 1.00x faster                                                     |
| regex_dna                 | 220 ms                                                 | 219 ms: 1.00x faster                                                     |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                   |
| pidigits                  | 186 ms                                                 | 187 ms: 1.00x slower                                                     |
| sqlglot_parse             | 1.27 ms                                                | 1.27 ms: 1.01x slower                                                    |
| asyncio_websockets        | 555 ms                                                 | 559 ms: 1.01x slower                                                     |
| scimark_sor               | 122 ms                                                 | 123 ms: 1.01x slower                                                     |
| deltablue                 | 3.15 ms                                                | 3.17 ms: 1.01x slower                                                    |
| comprehensions            | 16.4 us                                                | 16.5 us: 1.01x slower                                                    |
| python_startup_no_site    | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                    |
| json                      | 5.20 ms                                                | 5.26 ms: 1.01x slower                                                    |
| coverage                  | 83.7 ms                                                | 85.3 ms: 1.02x slower                                                    |
| mako                      | 11.1 ms                                                | 11.4 ms: 1.02x slower                                                    |
| bpe_tokeniser             | 4.69 sec                                               | 4.82 sec: 1.03x slower                                                   |
| xml_etree_iterparse       | 102 ms                                                 | 105 ms: 1.03x slower                                                     |
| coroutines                | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                    |
| scimark_monte_carlo       | 66.3 ms                                                | 68.7 ms: 1.04x slower                                                    |
| docutils                  | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                   |
| fannkuch                  | 381 ms                                                 | 399 ms: 1.05x slower                                                     |
| json_loads                | 27.0 us                                                | 28.6 us: 1.06x slower                                                    |
| create_gc_cycles          | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                    |
| async_tree_io_tg          | 825 ms                                                 | 896 ms: 1.09x slower                                                     |
| async_tree_io             | 843 ms                                                 | 926 ms: 1.10x slower                                                     |
| go                        | 142 ms                                                 | 159 ms: 1.13x slower                                                     |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                             |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed_tg, logging_format, json_dumps, hexiom, typing_runtime_protocols, bench_mp_pool, nbody, html5lib, xml_etree_parse, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x