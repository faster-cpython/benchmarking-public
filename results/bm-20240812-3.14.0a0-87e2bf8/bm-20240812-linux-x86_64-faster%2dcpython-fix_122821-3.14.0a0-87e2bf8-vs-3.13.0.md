# Results vs. 3.13.0

- fork: faster-cpython
- ref: fix_122821
- machine: linux-x86_64
- commit hash: 87e2bf8
- commit date: 2024-08-12
- overall geometric mean: 1.01x faster
- HPT reliability: 75.64%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 263 ms: 1.01x faster                                                  |
| docutils       | 2.58 sec                                               | 2.73 sec: 1.06x slower                                                |
| html5lib       | 64.5 ms                                                | 65.0 ms: 1.01x slower                                                 |
| tornado_http   | 91.5 ms                                                | 90.8 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 389 ms: 1.19x faster                                                  |
| async_tree_none            | 354 ms                                                 | 322 ms: 1.10x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 298 ms: 1.07x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 421 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 530 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 563 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                |
| asyncio_tcp                | 488 ms                                                 | 492 ms: 1.01x slower                                                  |
| asyncio_websockets         | 555 ms                                                 | 560 ms: 1.01x slower                                                  |
| async_generators           | 433 ms                                                 | 443 ms: 1.02x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 877 ms: 1.06x slower                                                  |
| async_tree_io              | 843 ms                                                 | 897 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 78.9 ms: 1.01x slower                                                 |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                  |
| nbody          | 85.7 ms                                                | 87.7 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.87 ms: 1.00x faster                                                 |
| regex_compile  | 131 ms                                                 | 132 ms: 1.01x slower                                                  |
| regex_dna      | 220 ms                                                 | 227 ms: 1.03x slower                                                  |
| regex_v8       | 25.3 ms                                                | 26.2 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process   | 60.4 ms                                                | 59.5 ms: 1.02x faster                                                 |
| xml_etree_generate  | 87.0 ms                                                | 85.9 ms: 1.01x faster                                                 |
| pickle_pure_python  | 300 us                                                 | 305 us: 1.02x slower                                                  |
| xml_etree_iterparse | 102 ms                                                 | 104 ms: 1.02x slower                                                  |
| json_loads          | 27.0 us                                                | 28.2 us: 1.04x slower                                                 |
| Geometric mean      | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (4): json_dumps, tomli_loads, xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako           | 11.1 ms                                                | 11.0 ms: 1.01x faster                                                 |
| genshi_text    | 22.9 ms                                                | 23.8 ms: 1.04x slower                                                 |
| genshi_xml     | 50.3 ms                                                | 52.8 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 266 us: 1.33x faster                                                  |
| deepcopy_memo              | 38.0 us                                                | 30.1 us: 1.26x faster                                                 |
| async_tree_memoization_tg  | 465 ms                                                 | 389 ms: 1.19x faster                                                  |
| deepcopy_reduce            | 3.17 us                                                | 2.77 us: 1.14x faster                                                 |
| async_tree_none            | 354 ms                                                 | 322 ms: 1.10x faster                                                  |
| pathlib                    | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                 |
| gc_traversal               | 3.81 ms                                                | 3.54 ms: 1.08x faster                                                 |
| async_tree_none_tg         | 320 ms                                                 | 298 ms: 1.07x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.76 ms: 1.06x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 421 ms: 1.05x faster                                                  |
| richards_super             | 54.4 ms                                                | 52.3 ms: 1.04x faster                                                 |
| richards                   | 48.1 ms                                                | 46.4 ms: 1.04x faster                                                 |
| bench_thread_pool          | 815 us                                                 | 791 us: 1.03x faster                                                  |
| generators                 | 28.8 ms                                                | 28.0 ms: 1.03x faster                                                 |
| logging_silent             | 102 ns                                                 | 99.2 ns: 1.03x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 530 ms: 1.03x faster                                                  |
| telco                      | 8.45 ms                                                | 8.26 ms: 1.02x faster                                                 |
| json                       | 5.20 ms                                                | 5.09 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 563 ms: 1.02x faster                                                  |
| xml_etree_process          | 60.4 ms                                                | 59.5 ms: 1.02x faster                                                 |
| raytrace                   | 262 ms                                                 | 258 ms: 1.01x faster                                                  |
| mdp                        | 2.74 sec                                               | 2.71 sec: 1.01x faster                                                |
| xml_etree_generate         | 87.0 ms                                                | 85.9 ms: 1.01x faster                                                 |
| thrift                     | 796 us                                                 | 787 us: 1.01x faster                                                  |
| nqueens                    | 80.6 ms                                                | 79.7 ms: 1.01x faster                                                 |
| logging_simple             | 5.66 us                                                | 5.60 us: 1.01x faster                                                 |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| scimark_lu                 | 115 ms                                                 | 114 ms: 1.01x faster                                                  |
| mako                       | 11.1 ms                                                | 11.0 ms: 1.01x faster                                                 |
| 2to3                       | 265 ms                                                 | 263 ms: 1.01x faster                                                  |
| tornado_http               | 91.5 ms                                                | 90.8 ms: 1.01x faster                                                 |
| pycparser                  | 1.19 sec                                               | 1.18 sec: 1.01x faster                                                |
| go                         | 142 ms                                                 | 141 ms: 1.01x faster                                                  |
| hexiom                     | 6.13 ms                                                | 6.10 ms: 1.00x faster                                                 |
| regex_effbot               | 3.88 ms                                                | 3.87 ms: 1.00x faster                                                 |
| sympy_integrate            | 19.9 ms                                                | 19.8 ms: 1.00x faster                                                 |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                |
| sqlglot_normalize          | 107 ms                                                 | 108 ms: 1.01x slower                                                  |
| float                      | 78.5 ms                                                | 78.9 ms: 1.01x slower                                                 |
| html5lib                   | 64.5 ms                                                | 65.0 ms: 1.01x slower                                                 |
| chaos                      | 58.4 ms                                                | 58.8 ms: 1.01x slower                                                 |
| regex_compile              | 131 ms                                                 | 132 ms: 1.01x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                 |
| asyncio_tcp                | 488 ms                                                 | 492 ms: 1.01x slower                                                  |
| asyncio_websockets         | 555 ms                                                 | 560 ms: 1.01x slower                                                  |
| python_startup_no_site     | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                 |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                  |
| pprint_safe_repr           | 744 ms                                                 | 751 ms: 1.01x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.01x slower                                                  |
| pickle_pure_python         | 300 us                                                 | 305 us: 1.02x slower                                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                 |
| scimark_sor                | 122 ms                                                 | 125 ms: 1.02x slower                                                  |
| nbody                      | 85.7 ms                                                | 87.7 ms: 1.02x slower                                                 |
| comprehensions             | 16.4 us                                                | 16.8 us: 1.02x slower                                                 |
| xml_etree_iterparse        | 102 ms                                                 | 104 ms: 1.02x slower                                                  |
| async_generators           | 433 ms                                                 | 443 ms: 1.02x slower                                                  |
| pprint_pformat             | 1.51 sec                                               | 1.55 sec: 1.03x slower                                                |
| scimark_monte_carlo        | 66.3 ms                                                | 68.3 ms: 1.03x slower                                                 |
| typing_runtime_protocols   | 159 us                                                 | 164 us: 1.03x slower                                                  |
| regex_dna                  | 220 ms                                                 | 227 ms: 1.03x slower                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.85 sec: 1.03x slower                                                |
| regex_v8                   | 25.3 ms                                                | 26.2 ms: 1.04x slower                                                 |
| genshi_text                | 22.9 ms                                                | 23.8 ms: 1.04x slower                                                 |
| pyflate                    | 460 ms                                                 | 478 ms: 1.04x slower                                                  |
| deltablue                  | 3.15 ms                                                | 3.28 ms: 1.04x slower                                                 |
| json_loads                 | 27.0 us                                                | 28.2 us: 1.04x slower                                                 |
| genshi_xml                 | 50.3 ms                                                | 52.8 ms: 1.05x slower                                                 |
| fannkuch                   | 381 ms                                                 | 400 ms: 1.05x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.73 sec: 1.06x slower                                                |
| async_tree_io_tg           | 825 ms                                                 | 877 ms: 1.06x slower                                                  |
| create_gc_cycles           | 1.61 ms                                                | 1.71 ms: 1.06x slower                                                 |
| async_tree_io              | 843 ms                                                 | 897 ms: 1.06x slower                                                  |
| coverage                   | 83.7 ms                                                | 90.8 ms: 1.08x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (15): sympy_expand, scimark_fft, sympy_str, django_template, coroutines, sqlglot_optimize, spectral_norm, json_dumps, crypto_pyaes, bench_mp_pool, tomli_loads, logging_format, xml_etree_parse, unpickle_pure_python, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 75.64% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x