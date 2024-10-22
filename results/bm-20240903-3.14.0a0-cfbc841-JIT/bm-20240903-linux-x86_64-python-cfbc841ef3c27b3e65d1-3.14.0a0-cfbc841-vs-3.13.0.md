# Results vs. 3.13.0

- fork: python
- ref: cfbc841ef3c27b3e65d1
- machine: linux-x86_64
- commit hash: cfbc841
- commit date: 2024-09-03
- overall geometric mean: 1.01x faster
- HPT reliability: 78.24%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 275 ms: 1.04x slower                                                  |
| docutils       | 2.58 sec                                               | 3.03 sec: 1.17x slower                                                |
| tornado_http   | 91.5 ms                                                | 95.6 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 405 ms: 1.15x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 401 ms: 1.10x faster                                                  |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 313 ms: 1.02x faster                                                  |
| asyncio_tcp                | 488 ms                                                 | 485 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                |
| coroutines                 | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 553 ms: 1.02x slower                                                  |
| async_generators           | 433 ms                                                 | 460 ms: 1.06x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 900 ms: 1.09x slower                                                  |
| async_tree_io              | 843 ms                                                 | 932 ms: 1.11x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.2 ms: 1.12x faster                                                 |
| nbody          | 85.7 ms                                                | 79.1 ms: 1.08x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.55 ms: 1.10x faster                                                 |
| regex_v8       | 25.3 ms                                                | 24.8 ms: 1.02x faster                                                 |
| regex_dna      | 220 ms                                                 | 219 ms: 1.00x faster                                                  |
| regex_compile  | 131 ms                                                 | 142 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.8 ms: 1.12x faster                                                 |
| xml_etree_process    | 60.4 ms                                                | 55.2 ms: 1.09x faster                                                 |
| tomli_loads          | 2.11 sec                                               | 1.93 sec: 1.09x faster                                                |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 102 ms                                                 | 98.0 ms: 1.04x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| pickle_pure_python   | 300 us                                                 | 301 us: 1.00x slower                                                  |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                  |
| json_loads           | 27.0 us                                                | 28.6 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.11 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.77 ms: 1.14x faster                                                 |
| django_template | 34.4 ms                                                | 35.6 ms: 1.04x slower                                                 |
| genshi_text     | 22.9 ms                                                | 24.2 ms: 1.06x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 58.1 ms: 1.15x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.3 us: 1.39x faster                                                 |
| deepcopy                   | 352 us                                                 | 266 us: 1.33x faster                                                  |
| richards                   | 48.1 ms                                                | 39.2 ms: 1.23x faster                                                 |
| scimark_fft                | 369 ms                                                 | 303 ms: 1.22x faster                                                  |
| richards_super             | 54.4 ms                                                | 45.4 ms: 1.20x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.20 ms: 1.20x faster                                                 |
| deepcopy_reduce            | 3.17 us                                                | 2.68 us: 1.18x faster                                                 |
| spectral_norm              | 115 ms                                                 | 99.2 ms: 1.16x faster                                                 |
| async_tree_memoization_tg  | 465 ms                                                 | 405 ms: 1.15x faster                                                  |
| mako                       | 11.1 ms                                                | 9.77 ms: 1.14x faster                                                 |
| xml_etree_generate         | 87.0 ms                                                | 77.8 ms: 1.12x faster                                                 |
| float                      | 78.5 ms                                                | 70.2 ms: 1.12x faster                                                 |
| crypto_pyaes               | 73.0 ms                                                | 65.9 ms: 1.11x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 401 ms: 1.10x faster                                                  |
| regex_effbot               | 3.88 ms                                                | 3.55 ms: 1.10x faster                                                 |
| xml_etree_process          | 60.4 ms                                                | 55.2 ms: 1.09x faster                                                 |
| tomli_loads                | 2.11 sec                                               | 1.93 sec: 1.09x faster                                                |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                  |
| go                         | 142 ms                                                 | 130 ms: 1.09x faster                                                  |
| nbody                      | 85.7 ms                                                | 79.1 ms: 1.08x faster                                                 |
| telco                      | 8.45 ms                                                | 7.82 ms: 1.08x faster                                                 |
| mdp                        | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                |
| xml_etree_parse            | 156 ms                                                 | 145 ms: 1.07x faster                                                  |
| pathlib                    | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                 |
| gc_traversal               | 3.81 ms                                                | 3.56 ms: 1.07x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.43 sec: 1.06x faster                                                |
| scimark_monte_carlo        | 66.3 ms                                                | 62.8 ms: 1.06x faster                                                 |
| scimark_sor                | 122 ms                                                 | 116 ms: 1.05x faster                                                  |
| scimark_lu                 | 115 ms                                                 | 109 ms: 1.05x faster                                                  |
| xml_etree_iterparse        | 102 ms                                                 | 98.0 ms: 1.04x faster                                                 |
| pprint_safe_repr           | 744 ms                                                 | 724 ms: 1.03x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 313 ms: 1.02x faster                                                  |
| fannkuch                   | 381 ms                                                 | 372 ms: 1.02x faster                                                  |
| thrift                     | 796 us                                                 | 781 us: 1.02x faster                                                  |
| regex_v8                   | 25.3 ms                                                | 24.8 ms: 1.02x faster                                                 |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                |
| pyflate                    | 460 ms                                                 | 452 ms: 1.02x faster                                                  |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| asyncio_tcp                | 488 ms                                                 | 485 ms: 1.01x faster                                                  |
| regex_dna                  | 220 ms                                                 | 219 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                |
| pickle_pure_python         | 300 us                                                 | 301 us: 1.00x slower                                                  |
| logging_simple             | 5.66 us                                                | 5.70 us: 1.01x slower                                                 |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                  |
| coroutines                 | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                 |
| deltablue                  | 3.15 ms                                                | 3.19 ms: 1.01x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 553 ms: 1.02x slower                                                  |
| comprehensions             | 16.4 us                                                | 16.7 us: 1.02x slower                                                 |
| python_startup_no_site     | 6.99 ms                                                | 7.11 ms: 1.02x slower                                                 |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                  |
| typing_runtime_protocols   | 159 us                                                 | 163 us: 1.02x slower                                                  |
| bench_thread_pool          | 815 us                                                 | 836 us: 1.03x slower                                                  |
| coverage                   | 83.7 ms                                                | 86.5 ms: 1.03x slower                                                 |
| django_template            | 34.4 ms                                                | 35.6 ms: 1.04x slower                                                 |
| 2to3                       | 265 ms                                                 | 275 ms: 1.04x slower                                                  |
| tornado_http               | 91.5 ms                                                | 95.6 ms: 1.04x slower                                                 |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                                  |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.05x slower                                                  |
| genshi_text                | 22.9 ms                                                | 24.2 ms: 1.06x slower                                                 |
| nqueens                    | 80.6 ms                                                | 85.2 ms: 1.06x slower                                                 |
| json_loads                 | 27.0 us                                                | 28.6 us: 1.06x slower                                                 |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.06x slower                                                 |
| async_generators           | 433 ms                                                 | 460 ms: 1.06x slower                                                  |
| sqlglot_optimize           | 53.9 ms                                                | 57.7 ms: 1.07x slower                                                 |
| json                       | 5.20 ms                                                | 5.56 ms: 1.07x slower                                                 |
| sqlglot_transpile          | 1.57 ms                                                | 1.70 ms: 1.08x slower                                                 |
| regex_compile              | 131 ms                                                 | 142 ms: 1.08x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 900 ms: 1.09x slower                                                  |
| create_gc_cycles           | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                 |
| sympy_expand               | 462 ms                                                 | 504 ms: 1.09x slower                                                  |
| dulwich_log                | 63.0 ms                                                | 68.8 ms: 1.09x slower                                                 |
| sympy_str                  | 274 ms                                                 | 299 ms: 1.09x slower                                                  |
| async_tree_io              | 843 ms                                                 | 932 ms: 1.11x slower                                                  |
| hexiom                     | 6.13 ms                                                | 6.85 ms: 1.12x slower                                                 |
| sympy_integrate            | 19.9 ms                                                | 22.7 ms: 1.14x slower                                                 |
| generators                 | 28.8 ms                                                | 32.9 ms: 1.14x slower                                                 |
| genshi_xml                 | 50.3 ms                                                | 58.1 ms: 1.15x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 173 ms: 1.16x slower                                                  |
| docutils                   | 2.58 sec                                               | 3.03 sec: 1.17x slower                                                |
| pylint                     | 313 ms                                                 | 372 ms: 1.19x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (7): logging_format, async_tree_cpu_io_mixed, bench_mp_pool, asyncio_websockets, html5lib, pprint_pformat, chaos
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 78.24% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x