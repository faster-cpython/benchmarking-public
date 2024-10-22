# Results vs. 3.13.0

- fork: faster-cpython
- ref: mark_load_fast_defer
- machine: linux-x86_64
- commit hash: 9992ab7
- commit date: 2024-10-09
- overall geometric mean: 1.02x faster
- HPT reliability: 99.23%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 256 ms: 1.04x faster                                                            |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                          |
| html5lib       | 64.5 ms                                                | 63.2 ms: 1.02x faster                                                           |
| tornado_http   | 91.5 ms                                                | 90.8 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 388 ms: 1.20x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 393 ms: 1.13x faster                                                            |
| async_tree_none            | 354 ms                                                 | 315 ms: 1.12x faster                                                            |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                            |
| asyncio_tcp                | 488 ms                                                 | 479 ms: 1.02x faster                                                            |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                            |
| async_generators           | 433 ms                                                 | 435 ms: 1.00x slower                                                            |
| coroutines                 | 22.5 ms                                                | 22.7 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 556 ms: 1.02x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 868 ms: 1.05x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_tcp_ssl, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 76.6 ms: 1.02x faster                                                           |
| nbody          | 85.7 ms                                                | 84.1 ms: 1.02x faster                                                           |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.63 ms: 1.07x faster                                                           |
| regex_v8       | 25.3 ms                                                | 24.3 ms: 1.04x faster                                                           |
| regex_compile  | 131 ms                                                 | 129 ms: 1.02x faster                                                            |
| regex_dna      | 220 ms                                                 | 221 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process   | 60.4 ms                                                | 58.2 ms: 1.04x faster                                                           |
| xml_etree_generate  | 87.0 ms                                                | 84.3 ms: 1.03x faster                                                           |
| xml_etree_parse     | 156 ms                                                 | 154 ms: 1.01x faster                                                            |
| pickle              | 11.6 us                                                | 11.4 us: 1.01x faster                                                           |
| json_dumps          | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| pickle_pure_python  | 300 us                                                 | 303 us: 1.01x slower                                                            |
| xml_etree_iterparse | 102 ms                                                 | 103 ms: 1.01x slower                                                            |
| pickle_list         | 5.01 us                                                | 5.09 us: 1.02x slower                                                           |
| pickle_dict         | 33.2 us                                                | 34.4 us: 1.04x slower                                                           |
| unpickle_list       | 4.96 us                                                | 5.17 us: 1.04x slower                                                           |
| unpickle            | 14.9 us                                                | 16.6 us: 1.11x slower                                                           |
| Geometric mean      | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (3): json_loads, tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 6.99 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 21.9 ms: 1.05x faster                                                           |
| genshi_xml      | 50.3 ms                                                | 49.1 ms: 1.03x faster                                                           |
| django_template | 34.4 ms                                                | 34.1 ms: 1.01x faster                                                           |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 258 us: 1.36x faster                                                            |
| deepcopy_memo              | 38.0 us                                                | 30.5 us: 1.25x faster                                                           |
| deepcopy_reduce            | 3.17 us                                                | 2.64 us: 1.20x faster                                                           |
| async_tree_memoization_tg  | 465 ms                                                 | 388 ms: 1.20x faster                                                            |
| go                         | 142 ms                                                 | 120 ms: 1.18x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 393 ms: 1.13x faster                                                            |
| async_tree_none            | 354 ms                                                 | 315 ms: 1.12x faster                                                            |
| regex_effbot               | 3.88 ms                                                | 3.63 ms: 1.07x faster                                                           |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                            |
| json                       | 5.20 ms                                                | 4.87 ms: 1.07x faster                                                           |
| mdp                        | 2.74 sec                                               | 2.58 sec: 1.06x faster                                                          |
| pathlib                    | 17.1 ms                                                | 16.3 ms: 1.05x faster                                                           |
| pprint_safe_repr           | 744 ms                                                 | 710 ms: 1.05x faster                                                            |
| genshi_text                | 22.9 ms                                                | 21.9 ms: 1.05x faster                                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.81 ms: 1.04x faster                                                           |
| generators                 | 28.8 ms                                                | 27.6 ms: 1.04x faster                                                           |
| pycparser                  | 1.19 sec                                               | 1.15 sec: 1.04x faster                                                          |
| regex_v8                   | 25.3 ms                                                | 24.3 ms: 1.04x faster                                                           |
| xml_etree_process          | 60.4 ms                                                | 58.2 ms: 1.04x faster                                                           |
| scimark_lu                 | 115 ms                                                 | 111 ms: 1.04x faster                                                            |
| 2to3                       | 265 ms                                                 | 256 ms: 1.04x faster                                                            |
| pprint_pformat             | 1.51 sec                                               | 1.46 sec: 1.03x faster                                                          |
| xml_etree_generate         | 87.0 ms                                                | 84.3 ms: 1.03x faster                                                           |
| bench_thread_pool          | 815 us                                                 | 791 us: 1.03x faster                                                            |
| sympy_str                  | 274 ms                                                 | 266 ms: 1.03x faster                                                            |
| richards_super             | 54.4 ms                                                | 53.0 ms: 1.03x faster                                                           |
| genshi_xml                 | 50.3 ms                                                | 49.1 ms: 1.03x faster                                                           |
| richards                   | 48.1 ms                                                | 46.9 ms: 1.03x faster                                                           |
| float                      | 78.5 ms                                                | 76.6 ms: 1.02x faster                                                           |
| thrift                     | 796 us                                                 | 778 us: 1.02x faster                                                            |
| html5lib                   | 64.5 ms                                                | 63.2 ms: 1.02x faster                                                           |
| regex_compile              | 131 ms                                                 | 129 ms: 1.02x faster                                                            |
| nbody                      | 85.7 ms                                                | 84.1 ms: 1.02x faster                                                           |
| sqlglot_optimize           | 53.9 ms                                                | 52.9 ms: 1.02x faster                                                           |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                            |
| asyncio_tcp                | 488 ms                                                 | 479 ms: 1.02x faster                                                            |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                            |
| sympy_integrate            | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                           |
| xml_etree_parse            | 156 ms                                                 | 154 ms: 1.01x faster                                                            |
| sympy_expand               | 462 ms                                                 | 456 ms: 1.01x faster                                                            |
| pickle                     | 11.6 us                                                | 11.4 us: 1.01x faster                                                           |
| scimark_fft                | 369 ms                                                 | 365 ms: 1.01x faster                                                            |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| crypto_pyaes               | 73.0 ms                                                | 72.3 ms: 1.01x faster                                                           |
| tornado_http               | 91.5 ms                                                | 90.8 ms: 1.01x faster                                                           |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| django_template            | 34.4 ms                                                | 34.1 ms: 1.01x faster                                                           |
| nqueens                    | 80.6 ms                                                | 80.0 ms: 1.01x faster                                                           |
| telco                      | 8.45 ms                                                | 8.40 ms: 1.01x faster                                                           |
| sqlglot_normalize          | 107 ms                                                 | 107 ms: 1.00x faster                                                            |
| python_startup_no_site     | 6.99 ms                                                | 6.99 ms: 1.00x slower                                                           |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.00x slower                                                            |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                            |
| async_generators           | 433 ms                                                 | 435 ms: 1.00x slower                                                            |
| pyflate                    | 460 ms                                                 | 462 ms: 1.01x slower                                                            |
| hexiom                     | 6.13 ms                                                | 6.16 ms: 1.01x slower                                                           |
| regex_dna                  | 220 ms                                                 | 221 ms: 1.01x slower                                                            |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                           |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.01x slower                                                           |
| sqlite_synth               | 2.85 us                                                | 2.88 us: 1.01x slower                                                           |
| coroutines                 | 22.5 ms                                                | 22.7 ms: 1.01x slower                                                           |
| pickle_pure_python         | 300 us                                                 | 303 us: 1.01x slower                                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.75 sec: 1.01x slower                                                          |
| xml_etree_iterparse        | 102 ms                                                 | 103 ms: 1.01x slower                                                            |
| scimark_sor                | 122 ms                                                 | 124 ms: 1.01x slower                                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                           |
| raytrace                   | 262 ms                                                 | 266 ms: 1.02x slower                                                            |
| pickle_list                | 5.01 us                                                | 5.09 us: 1.02x slower                                                           |
| chaos                      | 58.4 ms                                                | 59.7 ms: 1.02x slower                                                           |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| logging_format             | 6.25 us                                                | 6.39 us: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 556 ms: 1.02x slower                                                            |
| dulwich_log                | 63.0 ms                                                | 64.7 ms: 1.03x slower                                                           |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                          |
| scimark_monte_carlo        | 66.3 ms                                                | 68.5 ms: 1.03x slower                                                           |
| pickle_dict                | 33.2 us                                                | 34.4 us: 1.04x slower                                                           |
| unpickle_list              | 4.96 us                                                | 5.17 us: 1.04x slower                                                           |
| coverage                   | 83.7 ms                                                | 87.2 ms: 1.04x slower                                                           |
| deltablue                  | 3.15 ms                                                | 3.29 ms: 1.05x slower                                                           |
| fannkuch                   | 381 ms                                                 | 399 ms: 1.05x slower                                                            |
| gc_traversal               | 3.81 ms                                                | 4.00 ms: 1.05x slower                                                           |
| async_tree_io_tg           | 825 ms                                                 | 868 ms: 1.05x slower                                                            |
| create_gc_cycles           | 1.61 ms                                                | 1.72 ms: 1.07x slower                                                           |
| unpickle                   | 14.9 us                                                | 16.6 us: 1.11x slower                                                           |
| unpack_sequence            | 42.4 ns                                                | 48.1 ns: 1.13x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed, typing_runtime_protocols, logging_simple, json_loads, bench_mp_pool, asyncio_tcp_ssl, tomli_loads, unpickle_pure_python, logging_silent, async_tree_io, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.23% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x