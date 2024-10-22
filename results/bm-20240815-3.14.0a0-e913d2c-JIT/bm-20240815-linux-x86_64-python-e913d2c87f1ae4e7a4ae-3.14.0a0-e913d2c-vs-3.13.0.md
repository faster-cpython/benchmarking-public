# Results vs. 3.13.0

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: linux-x86_64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.01x faster
- HPT reliability: 52.53%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 279 ms: 1.05x slower                                                  |
| docutils       | 2.58 sec                                               | 3.01 sec: 1.16x slower                                                |
| html5lib       | 64.5 ms                                                | 67.2 ms: 1.04x slower                                                 |
| tornado_http   | 91.5 ms                                                | 93.4 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                                  |
| async_tree_none            | 354 ms                                                 | 323 ms: 1.10x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 427 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 535 ms: 1.02x faster                                                  |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                |
| asyncio_tcp                | 488 ms                                                 | 499 ms: 1.02x slower                                                  |
| coroutines                 | 22.5 ms                                                | 23.4 ms: 1.04x slower                                                 |
| async_tree_io_tg           | 825 ms                                                 | 860 ms: 1.04x slower                                                  |
| async_generators           | 433 ms                                                 | 452 ms: 1.04x slower                                                  |
| async_tree_io              | 843 ms                                                 | 905 ms: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.7 ms: 1.11x faster                                                 |
| nbody          | 85.7 ms                                                | 80.0 ms: 1.07x faster                                                 |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.75 ms: 1.03x faster                                                 |
| regex_v8       | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                 |
| regex_dna      | 220 ms                                                 | 221 ms: 1.01x slower                                                  |
| regex_compile  | 131 ms                                                 | 142 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.93 sec: 1.09x faster                                                |
| xml_etree_generate   | 87.0 ms                                                | 81.6 ms: 1.07x faster                                                 |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                  |
| xml_etree_process    | 60.4 ms                                                | 57.5 ms: 1.05x faster                                                 |
| xml_etree_iterparse  | 102 ms                                                 | 98.4 ms: 1.04x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 212 us: 1.01x faster                                                  |
| pickle_pure_python   | 300 us                                                 | 302 us: 1.01x slower                                                  |
| json_loads           | 27.0 us                                                | 28.6 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.12 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.98 ms: 1.11x faster                                                 |
| django_template | 34.4 ms                                                | 36.8 ms: 1.07x slower                                                 |
| genshi_text     | 22.9 ms                                                | 26.6 ms: 1.16x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 59.9 ms: 1.19x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.07x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.0 us: 1.41x faster                                                 |
| deepcopy                   | 352 us                                                 | 263 us: 1.34x faster                                                  |
| richards                   | 48.1 ms                                                | 39.4 ms: 1.22x faster                                                 |
| richards_super             | 54.4 ms                                                | 44.7 ms: 1.22x faster                                                 |
| deepcopy_reduce            | 3.17 us                                                | 2.64 us: 1.20x faster                                                 |
| scimark_fft                | 369 ms                                                 | 308 ms: 1.20x faster                                                  |
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.31 ms: 1.17x faster                                                 |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                  |
| mako                       | 11.1 ms                                                | 9.98 ms: 1.11x faster                                                 |
| float                      | 78.5 ms                                                | 70.7 ms: 1.11x faster                                                 |
| crypto_pyaes               | 73.0 ms                                                | 66.4 ms: 1.10x faster                                                 |
| async_tree_none            | 354 ms                                                 | 323 ms: 1.10x faster                                                  |
| tomli_loads                | 2.11 sec                                               | 1.93 sec: 1.09x faster                                                |
| telco                      | 8.45 ms                                                | 7.76 ms: 1.09x faster                                                 |
| mdp                        | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                |
| scimark_sor                | 122 ms                                                 | 114 ms: 1.08x faster                                                  |
| nbody                      | 85.7 ms                                                | 80.0 ms: 1.07x faster                                                 |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                                  |
| xml_etree_generate         | 87.0 ms                                                | 81.6 ms: 1.07x faster                                                 |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                 |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                                  |
| scimark_lu                 | 115 ms                                                 | 109 ms: 1.06x faster                                                  |
| xml_etree_process          | 60.4 ms                                                | 57.5 ms: 1.05x faster                                                 |
| logging_format             | 6.25 us                                                | 6.00 us: 1.04x faster                                                 |
| scimark_monte_carlo        | 66.3 ms                                                | 63.6 ms: 1.04x faster                                                 |
| xml_etree_iterparse        | 102 ms                                                 | 98.4 ms: 1.04x faster                                                 |
| gc_traversal               | 3.81 ms                                                | 3.67 ms: 1.04x faster                                                 |
| logging_simple             | 5.66 us                                                | 5.47 us: 1.04x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 427 ms: 1.04x faster                                                  |
| regex_effbot               | 3.88 ms                                                | 3.75 ms: 1.03x faster                                                 |
| pyflate                    | 460 ms                                                 | 445 ms: 1.03x faster                                                  |
| fannkuch                   | 381 ms                                                 | 369 ms: 1.03x faster                                                  |
| regex_v8                   | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.59 sec: 1.02x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 535 ms: 1.02x faster                                                  |
| deltablue                  | 3.15 ms                                                | 3.11 ms: 1.01x faster                                                 |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 212 us: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                                  |
| bench_thread_pool          | 815 us                                                 | 817 us: 1.00x slower                                                  |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                  |
| regex_dna                  | 220 ms                                                 | 221 ms: 1.01x slower                                                  |
| pickle_pure_python         | 300 us                                                 | 302 us: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                |
| raytrace                   | 262 ms                                                 | 264 ms: 1.01x slower                                                  |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                                 |
| python_startup_no_site     | 6.99 ms                                                | 7.12 ms: 1.02x slower                                                 |
| tornado_http               | 91.5 ms                                                | 93.4 ms: 1.02x slower                                                 |
| pprint_pformat             | 1.51 sec                                               | 1.54 sec: 1.02x slower                                                |
| asyncio_tcp                | 488 ms                                                 | 499 ms: 1.02x slower                                                  |
| json                       | 5.20 ms                                                | 5.32 ms: 1.02x slower                                                 |
| go                         | 142 ms                                                 | 145 ms: 1.02x slower                                                  |
| coroutines                 | 22.5 ms                                                | 23.4 ms: 1.04x slower                                                 |
| html5lib                   | 64.5 ms                                                | 67.2 ms: 1.04x slower                                                 |
| async_tree_io_tg           | 825 ms                                                 | 860 ms: 1.04x slower                                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                                 |
| async_generators           | 433 ms                                                 | 452 ms: 1.04x slower                                                  |
| coverage                   | 83.7 ms                                                | 87.5 ms: 1.05x slower                                                 |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.05x slower                                                  |
| 2to3                       | 265 ms                                                 | 279 ms: 1.05x slower                                                  |
| nqueens                    | 80.6 ms                                                | 85.2 ms: 1.06x slower                                                 |
| json_loads                 | 27.0 us                                                | 28.6 us: 1.06x slower                                                 |
| sqlglot_transpile          | 1.57 ms                                                | 1.68 ms: 1.07x slower                                                 |
| django_template            | 34.4 ms                                                | 36.8 ms: 1.07x slower                                                 |
| sqlglot_optimize           | 53.9 ms                                                | 57.8 ms: 1.07x slower                                                 |
| async_tree_io              | 843 ms                                                 | 905 ms: 1.07x slower                                                  |
| regex_compile              | 131 ms                                                 | 142 ms: 1.09x slower                                                  |
| create_gc_cycles           | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                 |
| typing_runtime_protocols   | 159 us                                                 | 174 us: 1.09x slower                                                  |
| sympy_expand               | 462 ms                                                 | 506 ms: 1.10x slower                                                  |
| sympy_str                  | 274 ms                                                 | 301 ms: 1.10x slower                                                  |
| hexiom                     | 6.13 ms                                                | 6.81 ms: 1.11x slower                                                 |
| generators                 | 28.8 ms                                                | 32.6 ms: 1.13x slower                                                 |
| sympy_integrate            | 19.9 ms                                                | 22.9 ms: 1.15x slower                                                 |
| genshi_text                | 22.9 ms                                                | 26.6 ms: 1.16x slower                                                 |
| docutils                   | 2.58 sec                                               | 3.01 sec: 1.16x slower                                                |
| sympy_sum                  | 150 ms                                                 | 175 ms: 1.17x slower                                                  |
| pylint                     | 313 ms                                                 | 368 ms: 1.18x slower                                                  |
| genshi_xml                 | 50.3 ms                                                | 59.9 ms: 1.19x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed, logging_silent, chaos, pprint_safe_repr, meteor_contest, thrift, bench_mp_pool, json_dumps, pycparser
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 52.53% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x