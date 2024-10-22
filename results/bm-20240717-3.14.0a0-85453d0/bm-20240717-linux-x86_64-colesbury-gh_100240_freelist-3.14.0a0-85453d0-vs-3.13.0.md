# Results vs. 3.13.0

- fork: colesbury
- ref: gh_100240_freelist
- machine: linux-x86_64
- commit hash: 85453d0
- commit date: 2024-07-17
- overall geometric mean: 1.02x faster
- HPT reliability: 98.77%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 261 ms: 1.01x faster                                                   |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                 |
| html5lib       | 64.5 ms                                                | 64.9 ms: 1.01x slower                                                  |
| tornado_http   | 91.5 ms                                                | 90.0 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 370 ms: 1.25x faster                                                   |
| async_tree_none            | 354 ms                                                 | 318 ms: 1.11x faster                                                   |
| async_tree_none_tg         | 320 ms                                                 | 287 ms: 1.11x faster                                                   |
| async_tree_memoization     | 442 ms                                                 | 400 ms: 1.11x faster                                                   |
| async_tree_io              | 843 ms                                                 | 820 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 562 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 538 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                 |
| asyncio_tcp                | 488 ms                                                 | 487 ms: 1.00x faster                                                   |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                   |
| async_generators           | 433 ms                                                 | 438 ms: 1.01x slower                                                   |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 76.7 ms: 1.02x faster                                                  |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                   |
| nbody          | 85.7 ms                                                | 86.9 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.66 ms: 1.06x faster                                                  |
| regex_v8       | 25.3 ms                                                | 23.8 ms: 1.06x faster                                                  |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                   |
| regex_compile  | 131 ms                                                 | 130 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 59.2 ms: 1.02x faster                                                  |
| xml_etree_generate   | 87.0 ms                                                | 85.6 ms: 1.02x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 212 us: 1.01x faster                                                   |
| tomli_loads          | 2.11 sec                                               | 2.13 sec: 1.01x slower                                                 |
| xml_etree_iterparse  | 102 ms                                                 | 104 ms: 1.02x slower                                                   |
| json_loads           | 27.0 us                                                | 27.8 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                  |
| python_startup_no_site | 6.99 ms                                                | 7.08 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 33.8 ms: 1.02x faster                                                  |
| genshi_xml      | 50.3 ms                                                | 49.7 ms: 1.01x faster                                                  |
| mako            | 11.1 ms                                                | 11.1 ms: 1.00x slower                                                  |
| genshi_text     | 22.9 ms                                                | 23.1 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 259 us: 1.36x faster                                                   |
| deepcopy_memo              | 38.0 us                                                | 29.7 us: 1.28x faster                                                  |
| async_tree_memoization_tg  | 465 ms                                                 | 370 ms: 1.25x faster                                                   |
| deepcopy_reduce            | 3.17 us                                                | 2.66 us: 1.19x faster                                                  |
| async_tree_none            | 354 ms                                                 | 318 ms: 1.11x faster                                                   |
| async_tree_none_tg         | 320 ms                                                 | 287 ms: 1.11x faster                                                   |
| async_tree_memoization     | 442 ms                                                 | 400 ms: 1.11x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.59 ms: 1.10x faster                                                  |
| mdp                        | 2.74 sec                                               | 2.51 sec: 1.09x faster                                                 |
| pathlib                    | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                  |
| gc_traversal               | 3.81 ms                                                | 3.53 ms: 1.08x faster                                                  |
| regex_effbot               | 3.88 ms                                                | 3.66 ms: 1.06x faster                                                  |
| regex_v8                   | 25.3 ms                                                | 23.8 ms: 1.06x faster                                                  |
| telco                      | 8.45 ms                                                | 8.03 ms: 1.05x faster                                                  |
| pycparser                  | 1.19 sec                                               | 1.13 sec: 1.05x faster                                                 |
| bench_thread_pool          | 815 us                                                 | 786 us: 1.04x faster                                                   |
| scimark_lu                 | 115 ms                                                 | 111 ms: 1.03x faster                                                   |
| richards                   | 48.1 ms                                                | 46.6 ms: 1.03x faster                                                  |
| async_tree_io              | 843 ms                                                 | 820 ms: 1.03x faster                                                   |
| logging_simple             | 5.66 us                                                | 5.51 us: 1.03x faster                                                  |
| richards_super             | 54.4 ms                                                | 53.1 ms: 1.03x faster                                                  |
| float                      | 78.5 ms                                                | 76.7 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 562 ms: 1.02x faster                                                   |
| json                       | 5.20 ms                                                | 5.09 ms: 1.02x faster                                                  |
| xml_etree_process          | 60.4 ms                                                | 59.2 ms: 1.02x faster                                                  |
| nqueens                    | 80.6 ms                                                | 79.1 ms: 1.02x faster                                                  |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                   |
| django_template            | 34.4 ms                                                | 33.8 ms: 1.02x faster                                                  |
| tornado_http               | 91.5 ms                                                | 90.0 ms: 1.02x faster                                                  |
| xml_etree_generate         | 87.0 ms                                                | 85.6 ms: 1.02x faster                                                  |
| logging_format             | 6.25 us                                                | 6.16 us: 1.02x faster                                                  |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                   |
| scimark_fft                | 369 ms                                                 | 363 ms: 1.02x faster                                                   |
| sqlglot_normalize          | 107 ms                                                 | 106 ms: 1.01x faster                                                   |
| pprint_safe_repr           | 744 ms                                                 | 734 ms: 1.01x faster                                                   |
| 2to3                       | 265 ms                                                 | 261 ms: 1.01x faster                                                   |
| sympy_str                  | 274 ms                                                 | 270 ms: 1.01x faster                                                   |
| genshi_xml                 | 50.3 ms                                                | 49.7 ms: 1.01x faster                                                  |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                  |
| sqlglot_optimize           | 53.9 ms                                                | 53.3 ms: 1.01x faster                                                  |
| raytrace                   | 262 ms                                                 | 258 ms: 1.01x faster                                                   |
| crypto_pyaes               | 73.0 ms                                                | 72.1 ms: 1.01x faster                                                  |
| sympy_expand               | 462 ms                                                 | 457 ms: 1.01x faster                                                   |
| pprint_pformat             | 1.51 sec                                               | 1.49 sec: 1.01x faster                                                 |
| sympy_integrate            | 19.9 ms                                                | 19.7 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 538 ms: 1.01x faster                                                   |
| unpickle_pure_python       | 213 us                                                 | 212 us: 1.01x faster                                                   |
| regex_compile              | 131 ms                                                 | 130 ms: 1.01x faster                                                   |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                 |
| asyncio_tcp                | 488 ms                                                 | 487 ms: 1.00x faster                                                   |
| mako                       | 11.1 ms                                                | 11.1 ms: 1.00x slower                                                  |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                   |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                   |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                  |
| html5lib                   | 64.5 ms                                                | 64.9 ms: 1.01x slower                                                  |
| hexiom                     | 6.13 ms                                                | 6.16 ms: 1.01x slower                                                  |
| tomli_loads                | 2.11 sec                                               | 2.13 sec: 1.01x slower                                                 |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                   |
| genshi_text                | 22.9 ms                                                | 23.1 ms: 1.01x slower                                                  |
| async_generators           | 433 ms                                                 | 438 ms: 1.01x slower                                                   |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                                  |
| typing_runtime_protocols   | 159 us                                                 | 161 us: 1.01x slower                                                   |
| nbody                      | 85.7 ms                                                | 86.9 ms: 1.01x slower                                                  |
| python_startup_no_site     | 6.99 ms                                                | 7.08 ms: 1.01x slower                                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                  |
| pyflate                    | 460 ms                                                 | 469 ms: 1.02x slower                                                   |
| xml_etree_iterparse        | 102 ms                                                 | 104 ms: 1.02x slower                                                   |
| dulwich_log                | 63.0 ms                                                | 64.4 ms: 1.02x slower                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.80 sec: 1.02x slower                                                 |
| deltablue                  | 3.15 ms                                                | 3.24 ms: 1.03x slower                                                  |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                  |
| json_loads                 | 27.0 us                                                | 27.8 us: 1.03x slower                                                  |
| generators                 | 28.8 ms                                                | 29.9 ms: 1.04x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                 |
| scimark_sor                | 122 ms                                                 | 129 ms: 1.06x slower                                                   |
| fannkuch                   | 381 ms                                                 | 408 ms: 1.07x slower                                                   |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                                  |
| coverage                   | 83.7 ms                                                | 91.7 ms: 1.09x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (11): pylint, logging_silent, sympy_sum, pickle_pure_python, chaos, go, bench_mp_pool, thrift, xml_etree_parse, scimark_monte_carlo, async_tree_io_tg
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 98.77% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x