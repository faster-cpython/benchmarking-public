# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.01x slower
- HPT reliability: 54.44%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 278 ms: 1.05x slower                                           |
| docutils       | 2.58 sec                                               | 2.94 sec: 1.14x slower                                         |
| tornado_http   | 91.5 ms                                                | 95.6 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                  | 1.06x slower                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 386 ms: 1.20x faster                                           |
| async_tree_none            | 354 ms                                                 | 319 ms: 1.11x faster                                           |
| async_tree_memoization     | 442 ms                                                 | 406 ms: 1.09x faster                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                         |
| asyncio_tcp                | 488 ms                                                 | 493 ms: 1.01x slower                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 551 ms: 1.01x slower                                           |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                          |
| async_tree_io              | 843 ms                                                 | 886 ms: 1.05x slower                                           |
| async_tree_io_tg           | 825 ms                                                 | 872 ms: 1.06x slower                                           |
| async_generators           | 433 ms                                                 | 457 ms: 1.06x slower                                           |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.9 ms: 1.09x faster                                          |
| nbody          | 85.7 ms                                                | 80.1 ms: 1.07x faster                                          |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                           |
| Geometric mean | (ref)                                                  | 1.05x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.68 ms: 1.06x faster                                          |
| regex_dna      | 220 ms                                                 | 227 ms: 1.03x slower                                           |
| regex_v8       | 25.3 ms                                                | 26.4 ms: 1.04x slower                                          |
| regex_compile  | 131 ms                                                 | 143 ms: 1.09x slower                                           |
| Geometric mean | (ref)                                                  | 1.03x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.6 ms: 1.12x faster                                          |
| xml_etree_process    | 60.4 ms                                                | 54.7 ms: 1.10x faster                                          |
| tomli_loads          | 2.11 sec                                               | 1.93 sec: 1.09x faster                                         |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.07x faster                                           |
| xml_etree_iterparse  | 102 ms                                                 | 98.2 ms: 1.04x faster                                          |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                          |
| pickle_pure_python   | 300 us                                                 | 302 us: 1.01x slower                                           |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                           |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                          |
| pickle_list          | 5.01 us                                                | 5.13 us: 1.03x slower                                          |
| unpickle_list        | 4.96 us                                                | 5.29 us: 1.07x slower                                          |
| pickle_dict          | 33.2 us                                                | 35.5 us: 1.07x slower                                          |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                   |

Benchmark hidden because not significant (2): unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                          |
| python_startup_no_site | 6.99 ms                                                | 7.10 ms: 1.02x slower                                          |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.94 ms: 1.12x faster                                          |
| django_template | 34.4 ms                                                | 35.8 ms: 1.04x slower                                          |
| genshi_text     | 22.9 ms                                                | 25.4 ms: 1.11x slower                                          |
| genshi_xml      | 50.3 ms                                                | 58.2 ms: 1.16x slower                                          |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.1 us: 1.40x faster                                          |
| deepcopy                   | 352 us                                                 | 263 us: 1.34x faster                                           |
| scimark_fft                | 369 ms                                                 | 305 ms: 1.21x faster                                           |
| async_tree_memoization_tg  | 465 ms                                                 | 386 ms: 1.20x faster                                           |
| deepcopy_reduce            | 3.17 us                                                | 2.66 us: 1.19x faster                                          |
| richards_super             | 54.4 ms                                                | 45.8 ms: 1.19x faster                                          |
| richards                   | 48.1 ms                                                | 41.0 ms: 1.17x faster                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.37 ms: 1.15x faster                                          |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                           |
| xml_etree_generate         | 87.0 ms                                                | 77.6 ms: 1.12x faster                                          |
| mako                       | 11.1 ms                                                | 9.94 ms: 1.12x faster                                          |
| async_tree_none            | 354 ms                                                 | 319 ms: 1.11x faster                                           |
| telco                      | 8.45 ms                                                | 7.62 ms: 1.11x faster                                          |
| xml_etree_process          | 60.4 ms                                                | 54.7 ms: 1.10x faster                                          |
| tomli_loads                | 2.11 sec                                               | 1.93 sec: 1.09x faster                                         |
| float                      | 78.5 ms                                                | 71.9 ms: 1.09x faster                                          |
| async_tree_memoization     | 442 ms                                                 | 406 ms: 1.09x faster                                           |
| crypto_pyaes               | 73.0 ms                                                | 67.4 ms: 1.08x faster                                          |
| pathlib                    | 17.1 ms                                                | 15.9 ms: 1.08x faster                                          |
| xml_etree_parse            | 156 ms                                                 | 145 ms: 1.07x faster                                           |
| nbody                      | 85.7 ms                                                | 80.1 ms: 1.07x faster                                          |
| pprint_safe_repr           | 744 ms                                                 | 698 ms: 1.07x faster                                           |
| go                         | 142 ms                                                 | 134 ms: 1.06x faster                                           |
| regex_effbot               | 3.88 ms                                                | 3.68 ms: 1.06x faster                                          |
| bpe_tokeniser              | 4.69 sec                                               | 4.47 sec: 1.05x faster                                         |
| scimark_lu                 | 115 ms                                                 | 110 ms: 1.05x faster                                           |
| json                       | 5.20 ms                                                | 4.96 ms: 1.05x faster                                          |
| pprint_pformat             | 1.51 sec                                               | 1.45 sec: 1.04x faster                                         |
| sqlite_synth               | 2.85 us                                                | 2.73 us: 1.04x faster                                          |
| xml_etree_iterparse        | 102 ms                                                 | 98.2 ms: 1.04x faster                                          |
| scimark_monte_carlo        | 66.3 ms                                                | 64.0 ms: 1.03x faster                                          |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.03x faster                                           |
| logging_silent             | 102 ns                                                 | 100.0 ns: 1.02x faster                                         |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                          |
| fannkuch                   | 381 ms                                                 | 374 ms: 1.02x faster                                           |
| gc_traversal               | 3.81 ms                                                | 3.75 ms: 1.02x faster                                          |
| mdp                        | 2.74 sec                                               | 2.71 sec: 1.01x faster                                         |
| logging_format             | 6.25 us                                                | 6.19 us: 1.01x faster                                          |
| thrift                     | 796 us                                                 | 790 us: 1.01x faster                                           |
| pyflate                    | 460 ms                                                 | 457 ms: 1.01x faster                                           |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                           |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x slower                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                         |
| pickle_pure_python         | 300 us                                                 | 302 us: 1.01x slower                                           |
| asyncio_tcp                | 488 ms                                                 | 493 ms: 1.01x slower                                           |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 551 ms: 1.01x slower                                           |
| pycparser                  | 1.19 sec                                               | 1.21 sec: 1.02x slower                                         |
| python_startup_no_site     | 6.99 ms                                                | 7.10 ms: 1.02x slower                                          |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                          |
| deltablue                  | 3.15 ms                                                | 3.21 ms: 1.02x slower                                          |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                          |
| typing_runtime_protocols   | 159 us                                                 | 163 us: 1.02x slower                                           |
| coverage                   | 83.7 ms                                                | 85.8 ms: 1.02x slower                                          |
| pickle_list                | 5.01 us                                                | 5.13 us: 1.03x slower                                          |
| regex_dna                  | 220 ms                                                 | 227 ms: 1.03x slower                                           |
| chaos                      | 58.4 ms                                                | 60.7 ms: 1.04x slower                                          |
| comprehensions             | 16.4 us                                                | 17.0 us: 1.04x slower                                          |
| django_template            | 34.4 ms                                                | 35.8 ms: 1.04x slower                                          |
| tornado_http               | 91.5 ms                                                | 95.6 ms: 1.04x slower                                          |
| regex_v8                   | 25.3 ms                                                | 26.4 ms: 1.04x slower                                          |
| 2to3                       | 265 ms                                                 | 278 ms: 1.05x slower                                           |
| async_tree_io              | 843 ms                                                 | 886 ms: 1.05x slower                                           |
| raytrace                   | 262 ms                                                 | 276 ms: 1.05x slower                                           |
| async_tree_io_tg           | 825 ms                                                 | 872 ms: 1.06x slower                                           |
| async_generators           | 433 ms                                                 | 457 ms: 1.06x slower                                           |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.06x slower                                          |
| nqueens                    | 80.6 ms                                                | 85.8 ms: 1.06x slower                                          |
| unpickle_list              | 4.96 us                                                | 5.29 us: 1.07x slower                                          |
| sqlglot_normalize          | 107 ms                                                 | 115 ms: 1.07x slower                                           |
| pickle_dict                | 33.2 us                                                | 35.5 us: 1.07x slower                                          |
| sqlglot_transpile          | 1.57 ms                                                | 1.69 ms: 1.07x slower                                          |
| create_gc_cycles           | 1.61 ms                                                | 1.73 ms: 1.08x slower                                          |
| sympy_expand               | 462 ms                                                 | 499 ms: 1.08x slower                                           |
| regex_compile              | 131 ms                                                 | 143 ms: 1.09x slower                                           |
| dulwich_log                | 63.0 ms                                                | 68.5 ms: 1.09x slower                                          |
| sympy_str                  | 274 ms                                                 | 300 ms: 1.10x slower                                           |
| bench_thread_pool          | 815 us                                                 | 897 us: 1.10x slower                                           |
| genshi_text                | 22.9 ms                                                | 25.4 ms: 1.11x slower                                          |
| sqlglot_optimize           | 53.9 ms                                                | 59.9 ms: 1.11x slower                                          |
| docutils                   | 2.58 sec                                               | 2.94 sec: 1.14x slower                                         |
| hexiom                     | 6.13 ms                                                | 6.99 ms: 1.14x slower                                          |
| genshi_xml                 | 50.3 ms                                                | 58.2 ms: 1.16x slower                                          |
| sympy_integrate            | 19.9 ms                                                | 23.4 ms: 1.18x slower                                          |
| sympy_sum                  | 150 ms                                                 | 177 ms: 1.18x slower                                           |
| pylint                     | 313 ms                                                 | 373 ms: 1.19x slower                                           |
| generators                 | 28.8 ms                                                | 35.1 ms: 1.22x slower                                          |
| bench_mp_pool              | 24.0 ms                                                | 61.3 ms: 2.55x slower                                          |
| unpack_sequence            | 42.4 ns                                                | 110 ns: 2.59x slower                                           |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                   |

Benchmark hidden because not significant (8): async_tree_none_tg, unpickle, logging_simple, meteor_contest, async_tree_cpu_io_mixed, json_loads, asyncio_websockets, html5lib
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 54.44% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x