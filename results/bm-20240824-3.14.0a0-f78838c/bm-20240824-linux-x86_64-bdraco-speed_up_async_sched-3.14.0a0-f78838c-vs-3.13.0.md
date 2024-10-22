# Results vs. 3.13.0

- fork: bdraco
- ref: speed_up_async_sched
- machine: linux-x86_64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.02x faster
- HPT reliability: 99.86%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 255 ms: 1.04x faster                                                  |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                |
| html5lib       | 64.5 ms                                                | 65.2 ms: 1.01x slower                                                 |
| tornado_http   | 91.5 ms                                                | 89.9 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 402 ms: 1.16x faster                                                  |
| async_tree_none            | 354 ms                                                 | 321 ms: 1.10x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 402 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 544 ms: 1.06x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 307 ms: 1.04x faster                                                  |
| asyncio_tcp                | 488 ms                                                 | 477 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 546 ms: 1.01x slower                                                  |
| asyncio_websockets         | 555 ms                                                 | 559 ms: 1.01x slower                                                  |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                 |
| async_tree_io              | 843 ms                                                 | 891 ms: 1.06x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 903 ms: 1.09x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 77.7 ms: 1.01x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.58 ms: 1.08x faster                                                 |
| regex_v8       | 25.3 ms                                                | 24.1 ms: 1.05x faster                                                 |
| regex_compile  | 131 ms                                                 | 128 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process   | 60.4 ms                                                | 58.2 ms: 1.04x faster                                                 |
| xml_etree_generate  | 87.0 ms                                                | 83.8 ms: 1.04x faster                                                 |
| tomli_loads         | 2.11 sec                                               | 2.07 sec: 1.02x faster                                                |
| json_dumps          | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| xml_etree_iterparse | 102 ms                                                 | 104 ms: 1.02x slower                                                  |
| json_loads          | 27.0 us                                                | 28.2 us: 1.05x slower                                                 |
| Geometric mean      | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (3): xml_etree_parse, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.10 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 21.8 ms: 1.05x faster                                                 |
| django_template | 34.4 ms                                                | 33.7 ms: 1.02x faster                                                 |
| genshi_xml      | 50.3 ms                                                | 49.5 ms: 1.02x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 259 us: 1.36x faster                                                  |
| deepcopy_memo              | 38.0 us                                                | 29.5 us: 1.29x faster                                                 |
| deepcopy_reduce            | 3.17 us                                                | 2.64 us: 1.20x faster                                                 |
| async_tree_memoization_tg  | 465 ms                                                 | 402 ms: 1.16x faster                                                  |
| async_tree_none            | 354 ms                                                 | 321 ms: 1.10x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 402 ms: 1.10x faster                                                  |
| pathlib                    | 17.1 ms                                                | 15.7 ms: 1.09x faster                                                 |
| mdp                        | 2.74 sec                                               | 2.53 sec: 1.08x faster                                                |
| regex_effbot               | 3.88 ms                                                | 3.58 ms: 1.08x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.76 ms: 1.06x faster                                                 |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 544 ms: 1.06x faster                                                  |
| regex_v8                   | 25.3 ms                                                | 24.1 ms: 1.05x faster                                                 |
| genshi_text                | 22.9 ms                                                | 21.8 ms: 1.05x faster                                                 |
| pycparser                  | 1.19 sec                                               | 1.14 sec: 1.05x faster                                                |
| richards_super             | 54.4 ms                                                | 52.0 ms: 1.05x faster                                                 |
| generators                 | 28.8 ms                                                | 27.6 ms: 1.05x faster                                                 |
| thrift                     | 796 us                                                 | 764 us: 1.04x faster                                                  |
| richards                   | 48.1 ms                                                | 46.2 ms: 1.04x faster                                                 |
| async_tree_none_tg         | 320 ms                                                 | 307 ms: 1.04x faster                                                  |
| bench_thread_pool          | 815 us                                                 | 783 us: 1.04x faster                                                  |
| 2to3                       | 265 ms                                                 | 255 ms: 1.04x faster                                                  |
| xml_etree_process          | 60.4 ms                                                | 58.2 ms: 1.04x faster                                                 |
| xml_etree_generate         | 87.0 ms                                                | 83.8 ms: 1.04x faster                                                 |
| logging_format             | 6.25 us                                                | 6.03 us: 1.04x faster                                                 |
| logging_simple             | 5.66 us                                                | 5.48 us: 1.03x faster                                                 |
| pprint_safe_repr           | 744 ms                                                 | 720 ms: 1.03x faster                                                  |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.03x faster                                                  |
| sympy_str                  | 274 ms                                                 | 265 ms: 1.03x faster                                                  |
| pprint_pformat             | 1.51 sec                                               | 1.47 sec: 1.03x faster                                                |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                                  |
| sympy_expand               | 462 ms                                                 | 451 ms: 1.02x faster                                                  |
| asyncio_tcp                | 488 ms                                                 | 477 ms: 1.02x faster                                                  |
| tomli_loads                | 2.11 sec                                               | 2.07 sec: 1.02x faster                                                |
| regex_compile              | 131 ms                                                 | 128 ms: 1.02x faster                                                  |
| sympy_integrate            | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                 |
| django_template            | 34.4 ms                                                | 33.7 ms: 1.02x faster                                                 |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| genshi_xml                 | 50.3 ms                                                | 49.5 ms: 1.02x faster                                                 |
| tornado_http               | 91.5 ms                                                | 89.9 ms: 1.02x faster                                                 |
| nqueens                    | 80.6 ms                                                | 79.3 ms: 1.02x faster                                                 |
| gc_traversal               | 3.81 ms                                                | 3.75 ms: 1.02x faster                                                 |
| crypto_pyaes               | 73.0 ms                                                | 72.0 ms: 1.01x faster                                                 |
| sqlglot_optimize           | 53.9 ms                                                | 53.3 ms: 1.01x faster                                                 |
| telco                      | 8.45 ms                                                | 8.36 ms: 1.01x faster                                                 |
| float                      | 78.5 ms                                                | 77.7 ms: 1.01x faster                                                 |
| scimark_fft                | 369 ms                                                 | 365 ms: 1.01x faster                                                  |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| logging_silent             | 102 ns                                                 | 101 ns: 1.01x faster                                                  |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| sqlglot_normalize          | 107 ms                                                 | 107 ms: 1.01x faster                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.57 ms: 1.00x faster                                                 |
| chaos                      | 58.4 ms                                                | 58.2 ms: 1.00x faster                                                 |
| hexiom                     | 6.13 ms                                                | 6.11 ms: 1.00x faster                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.00x slower                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 546 ms: 1.01x slower                                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.27 ms: 1.01x slower                                                 |
| asyncio_websockets         | 555 ms                                                 | 559 ms: 1.01x slower                                                  |
| deltablue                  | 3.15 ms                                                | 3.18 ms: 1.01x slower                                                 |
| html5lib                   | 64.5 ms                                                | 65.2 ms: 1.01x slower                                                 |
| scimark_monte_carlo        | 66.3 ms                                                | 67.3 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.99 ms                                                | 7.10 ms: 1.02x slower                                                 |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                 |
| coverage                   | 83.7 ms                                                | 85.4 ms: 1.02x slower                                                 |
| pyflate                    | 460 ms                                                 | 470 ms: 1.02x slower                                                  |
| xml_etree_iterparse        | 102 ms                                                 | 104 ms: 1.02x slower                                                  |
| json                       | 5.20 ms                                                | 5.33 ms: 1.02x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.84 sec: 1.03x slower                                                |
| scimark_sor                | 122 ms                                                 | 127 ms: 1.03x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                |
| json_loads                 | 27.0 us                                                | 28.2 us: 1.05x slower                                                 |
| fannkuch                   | 381 ms                                                 | 401 ms: 1.05x slower                                                  |
| async_tree_io              | 843 ms                                                 | 891 ms: 1.06x slower                                                  |
| create_gc_cycles           | 1.61 ms                                                | 1.76 ms: 1.09x slower                                                 |
| async_tree_io_tg           | 825 ms                                                 | 903 ms: 1.09x slower                                                  |
| go                         | 142 ms                                                 | 162 ms: 1.15x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (11): typing_runtime_protocols, nbody, xml_etree_parse, unpickle_pure_python, bench_mp_pool, regex_dna, mako, raytrace, pickle_pure_python, async_generators, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.86% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x