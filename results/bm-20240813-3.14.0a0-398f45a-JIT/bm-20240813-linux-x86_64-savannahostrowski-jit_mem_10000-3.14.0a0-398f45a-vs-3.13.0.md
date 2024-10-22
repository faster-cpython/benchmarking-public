# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_mem_10000
- machine: linux-x86_64
- commit hash: 398f45a
- commit date: 2024-08-13
- overall geometric mean: 1.00x faster
- HPT reliability: 80.96%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 301 ms: 1.14x slower                                                      |
| docutils       | 2.58 sec                                               | 2.82 sec: 1.09x slower                                                    |
| html5lib       | 64.5 ms                                                | 70.0 ms: 1.09x slower                                                     |
| tornado_http   | 91.5 ms                                                | 95.6 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.09x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 402 ms: 1.16x faster                                                      |
| async_tree_none            | 354 ms                                                 | 325 ms: 1.09x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                                      |
| async_tree_none_tg         | 320 ms                                                 | 301 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 546 ms: 1.01x slower                                                      |
| asyncio_websockets         | 555 ms                                                 | 559 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                     |
| asyncio_tcp                | 488 ms                                                 | 504 ms: 1.03x slower                                                      |
| async_generators           | 433 ms                                                 | 454 ms: 1.05x slower                                                      |
| async_tree_io              | 843 ms                                                 | 892 ms: 1.06x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 85.7 ms                                                | 80.9 ms: 1.06x faster                                                     |
| float          | 78.5 ms                                                | 74.6 ms: 1.05x faster                                                     |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.76 ms: 1.03x faster                                                     |
| regex_v8       | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                     |
| regex_compile  | 131 ms                                                 | 141 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.93 sec: 1.09x faster                                                    |
| xml_etree_process    | 60.4 ms                                                | 59.5 ms: 1.02x faster                                                     |
| xml_etree_parse      | 156 ms                                                 | 154 ms: 1.01x faster                                                      |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                     |
| xml_etree_generate   | 87.0 ms                                                | 86.1 ms: 1.01x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                      |
| pickle_pure_python   | 300 us                                                 | 305 us: 1.01x slower                                                      |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.03x slower                                                      |
| json_loads           | 27.0 us                                                | 28.8 us: 1.07x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                     |
| python_startup_no_site | 6.99 ms                                                | 7.14 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.73 ms: 1.14x faster                                                     |
| django_template | 34.4 ms                                                | 35.6 ms: 1.04x slower                                                     |
| genshi_text     | 22.9 ms                                                | 25.8 ms: 1.13x slower                                                     |
| genshi_xml      | 50.3 ms                                                | 61.2 ms: 1.22x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.7 us: 1.43x faster                                                     |
| deepcopy                   | 352 us                                                 | 261 us: 1.35x faster                                                      |
| deepcopy_reduce            | 3.17 us                                                | 2.65 us: 1.19x faster                                                     |
| scimark_fft                | 369 ms                                                 | 311 ms: 1.19x faster                                                      |
| richards_super             | 54.4 ms                                                | 46.3 ms: 1.18x faster                                                     |
| richards                   | 48.1 ms                                                | 41.1 ms: 1.17x faster                                                     |
| async_tree_memoization_tg  | 465 ms                                                 | 402 ms: 1.16x faster                                                      |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                      |
| mako                       | 11.1 ms                                                | 9.73 ms: 1.14x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.49 ms: 1.12x faster                                                     |
| crypto_pyaes               | 73.0 ms                                                | 66.6 ms: 1.10x faster                                                     |
| tomli_loads                | 2.11 sec                                               | 1.93 sec: 1.09x faster                                                    |
| async_tree_none            | 354 ms                                                 | 325 ms: 1.09x faster                                                      |
| telco                      | 8.45 ms                                                | 7.81 ms: 1.08x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                                      |
| scimark_monte_carlo        | 66.3 ms                                                | 62.3 ms: 1.06x faster                                                     |
| async_tree_none_tg         | 320 ms                                                 | 301 ms: 1.06x faster                                                      |
| pyflate                    | 460 ms                                                 | 433 ms: 1.06x faster                                                      |
| nbody                      | 85.7 ms                                                | 80.9 ms: 1.06x faster                                                     |
| pathlib                    | 17.1 ms                                                | 16.2 ms: 1.05x faster                                                     |
| float                      | 78.5 ms                                                | 74.6 ms: 1.05x faster                                                     |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.05x faster                                                      |
| scimark_lu                 | 115 ms                                                 | 110 ms: 1.05x faster                                                      |
| regex_effbot               | 3.88 ms                                                | 3.76 ms: 1.03x faster                                                     |
| regex_v8                   | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                     |
| fannkuch                   | 381 ms                                                 | 369 ms: 1.03x faster                                                      |
| thrift                     | 796 us                                                 | 779 us: 1.02x faster                                                      |
| logging_simple             | 5.66 us                                                | 5.56 us: 1.02x faster                                                     |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                      |
| logging_format             | 6.25 us                                                | 6.14 us: 1.02x faster                                                     |
| xml_etree_process          | 60.4 ms                                                | 59.5 ms: 1.02x faster                                                     |
| gc_traversal               | 3.81 ms                                                | 3.75 ms: 1.01x faster                                                     |
| xml_etree_parse            | 156 ms                                                 | 154 ms: 1.01x faster                                                      |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                     |
| xml_etree_generate         | 87.0 ms                                                | 86.1 ms: 1.01x faster                                                     |
| chaos                      | 58.4 ms                                                | 58.0 ms: 1.01x faster                                                     |
| pycparser                  | 1.19 sec                                               | 1.19 sec: 1.01x faster                                                    |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 546 ms: 1.01x slower                                                      |
| asyncio_websockets         | 555 ms                                                 | 559 ms: 1.01x slower                                                      |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                                      |
| mdp                        | 2.74 sec                                               | 2.77 sec: 1.01x slower                                                    |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                      |
| bench_thread_pool          | 815 us                                                 | 823 us: 1.01x slower                                                      |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                                     |
| pprint_safe_repr           | 744 ms                                                 | 753 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| pickle_pure_python         | 300 us                                                 | 305 us: 1.01x slower                                                      |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                     |
| pprint_pformat             | 1.51 sec                                               | 1.54 sec: 1.02x slower                                                    |
| json                       | 5.20 ms                                                | 5.31 ms: 1.02x slower                                                     |
| python_startup_no_site     | 6.99 ms                                                | 7.14 ms: 1.02x slower                                                     |
| coverage                   | 83.7 ms                                                | 85.8 ms: 1.03x slower                                                     |
| xml_etree_iterparse        | 102 ms                                                 | 105 ms: 1.03x slower                                                      |
| asyncio_tcp                | 488 ms                                                 | 504 ms: 1.03x slower                                                      |
| raytrace                   | 262 ms                                                 | 271 ms: 1.03x slower                                                      |
| django_template            | 34.4 ms                                                | 35.6 ms: 1.04x slower                                                     |
| go                         | 142 ms                                                 | 147 ms: 1.04x slower                                                      |
| tornado_http               | 91.5 ms                                                | 95.6 ms: 1.04x slower                                                     |
| async_generators           | 433 ms                                                 | 454 ms: 1.05x slower                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.95 sec: 1.05x slower                                                    |
| async_tree_io              | 843 ms                                                 | 892 ms: 1.06x slower                                                      |
| sqlglot_normalize          | 107 ms                                                 | 114 ms: 1.06x slower                                                      |
| nqueens                    | 80.6 ms                                                | 85.9 ms: 1.07x slower                                                     |
| json_loads                 | 27.0 us                                                | 28.8 us: 1.07x slower                                                     |
| deltablue                  | 3.15 ms                                                | 3.37 ms: 1.07x slower                                                     |
| regex_compile              | 131 ms                                                 | 141 ms: 1.07x slower                                                      |
| typing_runtime_protocols   | 159 us                                                 | 172 us: 1.08x slower                                                      |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                                     |
| html5lib                   | 64.5 ms                                                | 70.0 ms: 1.09x slower                                                     |
| sympy_str                  | 274 ms                                                 | 297 ms: 1.09x slower                                                      |
| sympy_expand               | 462 ms                                                 | 504 ms: 1.09x slower                                                      |
| docutils                   | 2.58 sec                                               | 2.82 sec: 1.09x slower                                                    |
| sqlglot_parse              | 1.27 ms                                                | 1.40 ms: 1.11x slower                                                     |
| hexiom                     | 6.13 ms                                                | 6.83 ms: 1.11x slower                                                     |
| genshi_text                | 22.9 ms                                                | 25.8 ms: 1.13x slower                                                     |
| sqlglot_optimize           | 53.9 ms                                                | 61.0 ms: 1.13x slower                                                     |
| 2to3                       | 265 ms                                                 | 301 ms: 1.14x slower                                                      |
| sympy_sum                  | 150 ms                                                 | 171 ms: 1.14x slower                                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.80 ms: 1.14x slower                                                     |
| sympy_integrate            | 19.9 ms                                                | 22.9 ms: 1.15x slower                                                     |
| pylint                     | 313 ms                                                 | 365 ms: 1.17x slower                                                      |
| genshi_xml                 | 50.3 ms                                                | 61.2 ms: 1.22x slower                                                     |
| generators                 | 28.8 ms                                                | 35.2 ms: 1.22x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, regex_dna, bench_mp_pool, logging_silent, async_tree_io_tg
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 80.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x