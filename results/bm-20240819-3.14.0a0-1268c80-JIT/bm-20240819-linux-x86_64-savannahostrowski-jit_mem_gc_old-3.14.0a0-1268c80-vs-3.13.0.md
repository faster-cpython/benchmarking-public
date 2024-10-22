# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_mem_gc_old
- machine: linux-x86_64
- commit hash: 1268c80
- commit date: 2024-08-19
- overall geometric mean: 1.01x faster
- HPT reliability: 65.86%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 281 ms: 1.06x slower                                                       |
| docutils       | 2.58 sec                                               | 3.00 sec: 1.16x slower                                                     |
| html5lib       | 64.5 ms                                                | 64.2 ms: 1.01x faster                                                      |
| tornado_http   | 91.5 ms                                                | 93.3 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.06x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 394 ms: 1.18x faster                                                       |
| async_tree_none            | 354 ms                                                 | 329 ms: 1.08x faster                                                       |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 426 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 533 ms: 1.02x faster                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                     |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                       |
| asyncio_tcp                | 488 ms                                                 | 493 ms: 1.01x slower                                                       |
| coroutines                 | 22.5 ms                                                | 23.1 ms: 1.03x slower                                                      |
| async_tree_io_tg           | 825 ms                                                 | 860 ms: 1.04x slower                                                       |
| async_generators           | 433 ms                                                 | 457 ms: 1.05x slower                                                       |
| async_tree_io              | 843 ms                                                 | 898 ms: 1.07x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.8 ms: 1.11x faster                                                      |
| nbody          | 85.7 ms                                                | 83.4 ms: 1.03x faster                                                      |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.59 ms: 1.08x faster                                                      |
| regex_v8       | 25.3 ms                                                | 24.3 ms: 1.04x faster                                                      |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                       |
| regex_compile  | 131 ms                                                 | 142 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|---------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads         | 2.11 sec                                               | 1.90 sec: 1.11x faster                                                     |
| xml_etree_parse     | 156 ms                                                 | 146 ms: 1.07x faster                                                       |
| xml_etree_generate  | 87.0 ms                                                | 81.7 ms: 1.06x faster                                                      |
| xml_etree_process   | 60.4 ms                                                | 57.1 ms: 1.06x faster                                                      |
| xml_etree_iterparse | 102 ms                                                 | 98.2 ms: 1.04x faster                                                      |
| pickle_pure_python  | 300 us                                                 | 304 us: 1.01x slower                                                       |
| json_loads          | 27.0 us                                                | 29.0 us: 1.08x slower                                                      |
| Geometric mean      | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (2): json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                      |
| python_startup_no_site | 6.99 ms                                                | 7.12 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                      |
| django_template | 34.4 ms                                                | 35.8 ms: 1.04x slower                                                      |
| genshi_text     | 22.9 ms                                                | 25.9 ms: 1.13x slower                                                      |
| genshi_xml      | 50.3 ms                                                | 61.2 ms: 1.22x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.07x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_old-3.14.0a0-1268c80 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.7 us: 1.42x faster                                                      |
| deepcopy                   | 352 us                                                 | 268 us: 1.31x faster                                                       |
| richards                   | 48.1 ms                                                | 39.0 ms: 1.24x faster                                                      |
| scimark_fft                | 369 ms                                                 | 303 ms: 1.22x faster                                                       |
| richards_super             | 54.4 ms                                                | 44.8 ms: 1.21x faster                                                      |
| async_tree_memoization_tg  | 465 ms                                                 | 394 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 3.17 us                                                | 2.69 us: 1.18x faster                                                      |
| spectral_norm              | 115 ms                                                 | 99.3 ms: 1.16x faster                                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.40 ms: 1.14x faster                                                      |
| tomli_loads                | 2.11 sec                                               | 1.90 sec: 1.11x faster                                                     |
| mako                       | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                      |
| crypto_pyaes               | 73.0 ms                                                | 65.8 ms: 1.11x faster                                                      |
| float                      | 78.5 ms                                                | 70.8 ms: 1.11x faster                                                      |
| telco                      | 8.45 ms                                                | 7.82 ms: 1.08x faster                                                      |
| regex_effbot               | 3.88 ms                                                | 3.59 ms: 1.08x faster                                                      |
| mdp                        | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                     |
| async_tree_none            | 354 ms                                                 | 329 ms: 1.08x faster                                                       |
| scimark_monte_carlo        | 66.3 ms                                                | 61.9 ms: 1.07x faster                                                      |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                       |
| scimark_sor                | 122 ms                                                 | 115 ms: 1.07x faster                                                       |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                       |
| xml_etree_generate         | 87.0 ms                                                | 81.7 ms: 1.06x faster                                                      |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                      |
| scimark_lu                 | 115 ms                                                 | 108 ms: 1.06x faster                                                       |
| xml_etree_process          | 60.4 ms                                                | 57.1 ms: 1.06x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 426 ms: 1.04x faster                                                       |
| regex_v8                   | 25.3 ms                                                | 24.3 ms: 1.04x faster                                                      |
| xml_etree_iterparse        | 102 ms                                                 | 98.2 ms: 1.04x faster                                                      |
| regex_dna                  | 220 ms                                                 | 212 ms: 1.04x faster                                                       |
| logging_format             | 6.25 us                                                | 6.03 us: 1.04x faster                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.55 sec: 1.03x faster                                                     |
| fannkuch                   | 381 ms                                                 | 370 ms: 1.03x faster                                                       |
| nbody                      | 85.7 ms                                                | 83.4 ms: 1.03x faster                                                      |
| pyflate                    | 460 ms                                                 | 447 ms: 1.03x faster                                                       |
| logging_simple             | 5.66 us                                                | 5.53 us: 1.02x faster                                                      |
| gc_traversal               | 3.81 ms                                                | 3.72 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 533 ms: 1.02x faster                                                       |
| thrift                     | 796 us                                                 | 782 us: 1.02x faster                                                       |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                       |
| pprint_safe_repr           | 744 ms                                                 | 732 ms: 1.02x faster                                                       |
| logging_silent             | 102 ns                                                 | 101 ns: 1.01x faster                                                       |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                      |
| html5lib                   | 64.5 ms                                                | 64.2 ms: 1.01x faster                                                      |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                     |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                       |
| bench_thread_pool          | 815 us                                                 | 819 us: 1.01x slower                                                       |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.01x slower                                                      |
| pprint_pformat             | 1.51 sec                                               | 1.53 sec: 1.01x slower                                                     |
| asyncio_tcp                | 488 ms                                                 | 493 ms: 1.01x slower                                                       |
| pickle_pure_python         | 300 us                                                 | 304 us: 1.01x slower                                                       |
| raytrace                   | 262 ms                                                 | 266 ms: 1.02x slower                                                       |
| python_startup_no_site     | 6.99 ms                                                | 7.12 ms: 1.02x slower                                                      |
| tornado_http               | 91.5 ms                                                | 93.3 ms: 1.02x slower                                                      |
| coverage                   | 83.7 ms                                                | 85.4 ms: 1.02x slower                                                      |
| coroutines                 | 22.5 ms                                                | 23.1 ms: 1.03x slower                                                      |
| json                       | 5.20 ms                                                | 5.35 ms: 1.03x slower                                                      |
| go                         | 142 ms                                                 | 146 ms: 1.03x slower                                                       |
| django_template            | 34.4 ms                                                | 35.8 ms: 1.04x slower                                                      |
| async_tree_io_tg           | 825 ms                                                 | 860 ms: 1.04x slower                                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.05x slower                                                      |
| async_generators           | 433 ms                                                 | 457 ms: 1.05x slower                                                       |
| 2to3                       | 265 ms                                                 | 281 ms: 1.06x slower                                                       |
| sqlglot_normalize          | 107 ms                                                 | 114 ms: 1.06x slower                                                       |
| async_tree_io              | 843 ms                                                 | 898 ms: 1.07x slower                                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.69 ms: 1.07x slower                                                      |
| sqlglot_optimize           | 53.9 ms                                                | 57.9 ms: 1.07x slower                                                      |
| json_loads                 | 27.0 us                                                | 29.0 us: 1.08x slower                                                      |
| typing_runtime_protocols   | 159 us                                                 | 172 us: 1.08x slower                                                       |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                                      |
| regex_compile              | 131 ms                                                 | 142 ms: 1.09x slower                                                       |
| nqueens                    | 80.6 ms                                                | 87.7 ms: 1.09x slower                                                      |
| sympy_expand               | 462 ms                                                 | 508 ms: 1.10x slower                                                       |
| sympy_str                  | 274 ms                                                 | 303 ms: 1.11x slower                                                       |
| hexiom                     | 6.13 ms                                                | 6.87 ms: 1.12x slower                                                      |
| genshi_text                | 22.9 ms                                                | 25.9 ms: 1.13x slower                                                      |
| sympy_integrate            | 19.9 ms                                                | 23.1 ms: 1.16x slower                                                      |
| docutils                   | 2.58 sec                                               | 3.00 sec: 1.16x slower                                                     |
| generators                 | 28.8 ms                                                | 33.5 ms: 1.16x slower                                                      |
| pylint                     | 313 ms                                                 | 369 ms: 1.18x slower                                                       |
| sympy_sum                  | 150 ms                                                 | 177 ms: 1.18x slower                                                       |
| genshi_xml                 | 50.3 ms                                                | 61.2 ms: 1.22x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, pycparser, chaos, bench_mp_pool, deltablue, json_dumps, unpickle_pure_python
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 65.86% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x