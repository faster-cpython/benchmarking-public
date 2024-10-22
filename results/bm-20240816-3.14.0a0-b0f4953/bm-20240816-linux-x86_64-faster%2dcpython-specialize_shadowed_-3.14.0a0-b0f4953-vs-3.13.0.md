# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_shadowed_
- machine: linux-x86_64
- commit hash: b0f4953
- commit date: 2024-08-16
- overall geometric mean: 1.01x faster
- HPT reliability: 91.12%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 254 ms: 1.04x faster                                                            |
| docutils       | 2.58 sec                                               | 2.71 sec: 1.05x slower                                                          |
| html5lib       | 64.5 ms                                                | 63.8 ms: 1.01x faster                                                           |
| tornado_http   | 91.5 ms                                                | 90.3 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                            |
| async_tree_none            | 354 ms                                                 | 323 ms: 1.10x faster                                                            |
| async_tree_none_tg         | 320 ms                                                 | 301 ms: 1.06x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 422 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 527 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 560 ms: 1.03x faster                                                            |
| asyncio_tcp                | 488 ms                                                 | 481 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                          |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                            |
| coroutines                 | 22.5 ms                                                | 23.1 ms: 1.03x slower                                                           |
| async_tree_io              | 843 ms                                                 | 897 ms: 1.06x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 886 ms: 1.07x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                            |
| float          | 78.5 ms                                                | 78.9 ms: 1.01x slower                                                           |
| nbody          | 85.7 ms                                                | 88.1 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.68 ms: 1.05x faster                                                           |
| regex_compile  | 131 ms                                                 | 129 ms: 1.02x faster                                                            |
| regex_v8       | 25.3 ms                                                | 25.0 ms: 1.01x faster                                                           |
| regex_dna      | 220 ms                                                 | 223 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 58.9 ms: 1.03x faster                                                           |
| xml_etree_generate   | 87.0 ms                                                | 85.7 ms: 1.01x faster                                                           |
| tomli_loads          | 2.11 sec                                               | 2.10 sec: 1.01x faster                                                          |
| pickle_pure_python   | 300 us                                                 | 302 us: 1.00x slower                                                            |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                            |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.02x slower                                                            |
| json_loads           | 27.0 us                                                | 28.5 us: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 22.2 ms: 1.03x faster                                                           |
| genshi_xml      | 50.3 ms                                                | 49.3 ms: 1.02x faster                                                           |
| django_template | 34.4 ms                                                | 34.2 ms: 1.01x faster                                                           |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 260 us: 1.35x faster                                                            |
| deepcopy_memo              | 38.0 us                                                | 30.1 us: 1.26x faster                                                           |
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                            |
| deepcopy_reduce            | 3.17 us                                                | 2.70 us: 1.17x faster                                                           |
| async_tree_none            | 354 ms                                                 | 323 ms: 1.10x faster                                                            |
| pathlib                    | 17.1 ms                                                | 15.6 ms: 1.09x faster                                                           |
| async_tree_none_tg         | 320 ms                                                 | 301 ms: 1.06x faster                                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.72 ms: 1.06x faster                                                           |
| pycparser                  | 1.19 sec                                               | 1.13 sec: 1.06x faster                                                          |
| regex_effbot               | 3.88 ms                                                | 3.68 ms: 1.05x faster                                                           |
| async_tree_memoization     | 442 ms                                                 | 422 ms: 1.05x faster                                                            |
| 2to3                       | 265 ms                                                 | 254 ms: 1.04x faster                                                            |
| thrift                     | 796 us                                                 | 766 us: 1.04x faster                                                            |
| bench_thread_pool          | 815 us                                                 | 784 us: 1.04x faster                                                            |
| richards                   | 48.1 ms                                                | 46.5 ms: 1.03x faster                                                           |
| richards_super             | 54.4 ms                                                | 52.8 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 527 ms: 1.03x faster                                                            |
| genshi_text                | 22.9 ms                                                | 22.2 ms: 1.03x faster                                                           |
| pprint_safe_repr           | 744 ms                                                 | 724 ms: 1.03x faster                                                            |
| generators                 | 28.8 ms                                                | 28.0 ms: 1.03x faster                                                           |
| gc_traversal               | 3.81 ms                                                | 3.71 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 560 ms: 1.03x faster                                                            |
| xml_etree_process          | 60.4 ms                                                | 58.9 ms: 1.03x faster                                                           |
| genshi_xml                 | 50.3 ms                                                | 49.3 ms: 1.02x faster                                                           |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                            |
| crypto_pyaes               | 73.0 ms                                                | 71.5 ms: 1.02x faster                                                           |
| logging_simple             | 5.66 us                                                | 5.55 us: 1.02x faster                                                           |
| scimark_fft                | 369 ms                                                 | 361 ms: 1.02x faster                                                            |
| regex_compile              | 131 ms                                                 | 129 ms: 1.02x faster                                                            |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                            |
| pprint_pformat             | 1.51 sec                                               | 1.49 sec: 1.02x faster                                                          |
| xml_etree_generate         | 87.0 ms                                                | 85.7 ms: 1.01x faster                                                           |
| telco                      | 8.45 ms                                                | 8.33 ms: 1.01x faster                                                           |
| nqueens                    | 80.6 ms                                                | 79.5 ms: 1.01x faster                                                           |
| asyncio_tcp                | 488 ms                                                 | 481 ms: 1.01x faster                                                            |
| tornado_http               | 91.5 ms                                                | 90.3 ms: 1.01x faster                                                           |
| logging_format             | 6.25 us                                                | 6.18 us: 1.01x faster                                                           |
| html5lib                   | 64.5 ms                                                | 63.8 ms: 1.01x faster                                                           |
| sympy_str                  | 274 ms                                                 | 271 ms: 1.01x faster                                                            |
| sympy_expand               | 462 ms                                                 | 457 ms: 1.01x faster                                                            |
| regex_v8                   | 25.3 ms                                                | 25.0 ms: 1.01x faster                                                           |
| sympy_integrate            | 19.9 ms                                                | 19.8 ms: 1.01x faster                                                           |
| tomli_loads                | 2.11 sec                                               | 2.10 sec: 1.01x faster                                                          |
| raytrace                   | 262 ms                                                 | 260 ms: 1.01x faster                                                            |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| django_template            | 34.4 ms                                                | 34.2 ms: 1.01x faster                                                           |
| sqlglot_optimize           | 53.9 ms                                                | 53.6 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                          |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                                            |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                            |
| pickle_pure_python         | 300 us                                                 | 302 us: 1.00x slower                                                            |
| float                      | 78.5 ms                                                | 78.9 ms: 1.01x slower                                                           |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                           |
| coverage                   | 83.7 ms                                                | 84.4 ms: 1.01x slower                                                           |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.01x slower                                                            |
| sqlglot_normalize          | 107 ms                                                 | 109 ms: 1.01x slower                                                            |
| python_startup_no_site     | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                           |
| regex_dna                  | 220 ms                                                 | 223 ms: 1.01x slower                                                            |
| hexiom                     | 6.13 ms                                                | 6.24 ms: 1.02x slower                                                           |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                           |
| comprehensions             | 16.4 us                                                | 16.7 us: 1.02x slower                                                           |
| pyflate                    | 460 ms                                                 | 469 ms: 1.02x slower                                                            |
| json                       | 5.20 ms                                                | 5.31 ms: 1.02x slower                                                           |
| deltablue                  | 3.15 ms                                                | 3.22 ms: 1.02x slower                                                           |
| xml_etree_iterparse        | 102 ms                                                 | 105 ms: 1.02x slower                                                            |
| coroutines                 | 22.5 ms                                                | 23.1 ms: 1.03x slower                                                           |
| nbody                      | 85.7 ms                                                | 88.1 ms: 1.03x slower                                                           |
| scimark_monte_carlo        | 66.3 ms                                                | 68.3 ms: 1.03x slower                                                           |
| logging_silent             | 102 ns                                                 | 105 ns: 1.03x slower                                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.84 sec: 1.03x slower                                                          |
| docutils                   | 2.58 sec                                               | 2.71 sec: 1.05x slower                                                          |
| scimark_sor                | 122 ms                                                 | 129 ms: 1.05x slower                                                            |
| json_loads                 | 27.0 us                                                | 28.5 us: 1.05x slower                                                           |
| fannkuch                   | 381 ms                                                 | 404 ms: 1.06x slower                                                            |
| async_tree_io              | 843 ms                                                 | 897 ms: 1.06x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 886 ms: 1.07x slower                                                            |
| create_gc_cycles           | 1.61 ms                                                | 1.73 ms: 1.07x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (10): mdp, typing_runtime_protocols, bench_mp_pool, json_dumps, xml_etree_parse, scimark_lu, async_generators, chaos, go, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 91.12% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x