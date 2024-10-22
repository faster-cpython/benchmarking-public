# Results vs. 3.13.0

- fork: serhiy-storchaka
- ref: pickle_save_global3
- machine: linux-x86_64
- commit hash: 5efa5a5
- commit date: 2024-07-30
- overall geometric mean: 1.02x faster
- HPT reliability: 88.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 263 ms: 1.01x faster                                                             |
| docutils       | 2.58 sec                                               | 2.73 sec: 1.06x slower                                                           |
| html5lib       | 64.5 ms                                                | 65.8 ms: 1.02x slower                                                            |
| tornado_http   | 91.5 ms                                                | 90.2 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                                             |
| async_tree_none            | 354 ms                                                 | 324 ms: 1.09x faster                                                             |
| async_tree_none_tg         | 320 ms                                                 | 298 ms: 1.08x faster                                                             |
| async_tree_memoization     | 442 ms                                                 | 425 ms: 1.04x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 531 ms: 1.02x faster                                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                           |
| asyncio_tcp                | 488 ms                                                 | 487 ms: 1.00x faster                                                             |
| asyncio_websockets         | 555 ms                                                 | 560 ms: 1.01x slower                                                             |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                            |
| async_generators           | 433 ms                                                 | 443 ms: 1.02x slower                                                             |
| async_tree_io_tg           | 825 ms                                                 | 869 ms: 1.05x slower                                                             |
| async_tree_io              | 843 ms                                                 | 903 ms: 1.07x slower                                                             |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                             |
| nbody          | 85.7 ms                                                | 86.5 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.83 ms: 1.01x faster                                                            |
| regex_compile  | 131 ms                                                 | 130 ms: 1.01x faster                                                             |
| regex_dna      | 220 ms                                                 | 227 ms: 1.03x slower                                                             |
| regex_v8       | 25.3 ms                                                | 26.4 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|---------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads         | 2.11 sec                                               | 2.04 sec: 1.04x faster                                                           |
| xml_etree_process   | 60.4 ms                                                | 58.6 ms: 1.03x faster                                                            |
| xml_etree_generate  | 87.0 ms                                                | 84.9 ms: 1.02x faster                                                            |
| json_dumps          | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                            |
| pickle_pure_python  | 300 us                                                 | 302 us: 1.01x slower                                                             |
| xml_etree_parse     | 156 ms                                                 | 158 ms: 1.01x slower                                                             |
| json_loads          | 27.0 us                                                | 27.8 us: 1.03x slower                                                            |
| xml_etree_iterparse | 102 ms                                                 | 105 ms: 1.03x slower                                                             |
| Geometric mean      | (ref)                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                            |
| python_startup_no_site | 6.99 ms                                                | 7.04 ms: 1.01x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 22.3 ms: 1.03x faster                                                            |
| mako            | 11.1 ms                                                | 11.1 ms: 1.00x faster                                                            |
| django_template | 34.4 ms                                                | 35.0 ms: 1.02x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 261 us: 1.35x faster                                                             |
| deepcopy_memo              | 38.0 us                                                | 29.7 us: 1.28x faster                                                            |
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                                             |
| deepcopy_reduce            | 3.17 us                                                | 2.74 us: 1.15x faster                                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.51 ms: 1.11x faster                                                            |
| async_tree_none            | 354 ms                                                 | 324 ms: 1.09x faster                                                             |
| mdp                        | 2.74 sec                                               | 2.52 sec: 1.09x faster                                                           |
| async_tree_none_tg         | 320 ms                                                 | 298 ms: 1.08x faster                                                             |
| gc_traversal               | 3.81 ms                                                | 3.56 ms: 1.07x faster                                                            |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                            |
| spectral_norm              | 115 ms                                                 | 109 ms: 1.06x faster                                                             |
| richards                   | 48.1 ms                                                | 45.8 ms: 1.05x faster                                                            |
| richards_super             | 54.4 ms                                                | 51.8 ms: 1.05x faster                                                            |
| telco                      | 8.45 ms                                                | 8.11 ms: 1.04x faster                                                            |
| logging_format             | 6.25 us                                                | 6.01 us: 1.04x faster                                                            |
| logging_simple             | 5.66 us                                                | 5.44 us: 1.04x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 425 ms: 1.04x faster                                                             |
| tomli_loads                | 2.11 sec                                               | 2.04 sec: 1.04x faster                                                           |
| bench_thread_pool          | 815 us                                                 | 786 us: 1.04x faster                                                             |
| json                       | 5.20 ms                                                | 5.04 ms: 1.03x faster                                                            |
| xml_etree_process          | 60.4 ms                                                | 58.6 ms: 1.03x faster                                                            |
| scimark_fft                | 369 ms                                                 | 359 ms: 1.03x faster                                                             |
| genshi_text                | 22.9 ms                                                | 22.3 ms: 1.03x faster                                                            |
| xml_etree_generate         | 87.0 ms                                                | 84.9 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 531 ms: 1.02x faster                                                             |
| scimark_lu                 | 115 ms                                                 | 112 ms: 1.02x faster                                                             |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                           |
| thrift                     | 796 us                                                 | 784 us: 1.02x faster                                                             |
| sqlglot_optimize           | 53.9 ms                                                | 53.1 ms: 1.02x faster                                                            |
| tornado_http               | 91.5 ms                                                | 90.2 ms: 1.02x faster                                                            |
| regex_effbot               | 3.88 ms                                                | 3.83 ms: 1.01x faster                                                            |
| raytrace                   | 262 ms                                                 | 258 ms: 1.01x faster                                                             |
| sympy_str                  | 274 ms                                                 | 270 ms: 1.01x faster                                                             |
| go                         | 142 ms                                                 | 140 ms: 1.01x faster                                                             |
| nqueens                    | 80.6 ms                                                | 79.6 ms: 1.01x faster                                                            |
| generators                 | 28.8 ms                                                | 28.5 ms: 1.01x faster                                                            |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                            |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                            |
| sympy_integrate            | 19.9 ms                                                | 19.7 ms: 1.01x faster                                                            |
| 2to3                       | 265 ms                                                 | 263 ms: 1.01x faster                                                             |
| sqlglot_normalize          | 107 ms                                                 | 107 ms: 1.01x faster                                                             |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                             |
| regex_compile              | 131 ms                                                 | 130 ms: 1.01x faster                                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                           |
| mako                       | 11.1 ms                                                | 11.1 ms: 1.00x faster                                                            |
| asyncio_tcp                | 488 ms                                                 | 487 ms: 1.00x faster                                                             |
| coverage                   | 83.7 ms                                                | 84.1 ms: 1.00x slower                                                            |
| pickle_pure_python         | 300 us                                                 | 302 us: 1.01x slower                                                             |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                             |
| python_startup_no_site     | 6.99 ms                                                | 7.04 ms: 1.01x slower                                                            |
| asyncio_websockets         | 555 ms                                                 | 560 ms: 1.01x slower                                                             |
| nbody                      | 85.7 ms                                                | 86.5 ms: 1.01x slower                                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                            |
| scimark_monte_carlo        | 66.3 ms                                                | 67.2 ms: 1.01x slower                                                            |
| typing_runtime_protocols   | 159 us                                                 | 161 us: 1.01x slower                                                             |
| xml_etree_parse            | 156 ms                                                 | 158 ms: 1.01x slower                                                             |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                            |
| django_template            | 34.4 ms                                                | 35.0 ms: 1.02x slower                                                            |
| html5lib                   | 64.5 ms                                                | 65.8 ms: 1.02x slower                                                            |
| hexiom                     | 6.13 ms                                                | 6.26 ms: 1.02x slower                                                            |
| async_generators           | 433 ms                                                 | 443 ms: 1.02x slower                                                             |
| deltablue                  | 3.15 ms                                                | 3.23 ms: 1.03x slower                                                            |
| json_loads                 | 27.0 us                                                | 27.8 us: 1.03x slower                                                            |
| comprehensions             | 16.4 us                                                | 16.9 us: 1.03x slower                                                            |
| xml_etree_iterparse        | 102 ms                                                 | 105 ms: 1.03x slower                                                             |
| bpe_tokeniser              | 4.69 sec                                               | 4.84 sec: 1.03x slower                                                           |
| regex_dna                  | 220 ms                                                 | 227 ms: 1.03x slower                                                             |
| scimark_sor                | 122 ms                                                 | 127 ms: 1.03x slower                                                             |
| pyflate                    | 460 ms                                                 | 477 ms: 1.04x slower                                                             |
| regex_v8                   | 25.3 ms                                                | 26.4 ms: 1.05x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 869 ms: 1.05x slower                                                             |
| docutils                   | 2.58 sec                                               | 2.73 sec: 1.06x slower                                                           |
| fannkuch                   | 381 ms                                                 | 403 ms: 1.06x slower                                                             |
| create_gc_cycles           | 1.61 ms                                                | 1.72 ms: 1.07x slower                                                            |
| async_tree_io              | 843 ms                                                 | 903 ms: 1.07x slower                                                             |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (14): async_tree_cpu_io_mixed, sympy_expand, genshi_xml, logging_silent, unpickle_pure_python, pprint_safe_repr, crypto_pyaes, bench_mp_pool, sqlglot_transpile, float, sympy_sum, chaos, pprint_pformat, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 88.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x