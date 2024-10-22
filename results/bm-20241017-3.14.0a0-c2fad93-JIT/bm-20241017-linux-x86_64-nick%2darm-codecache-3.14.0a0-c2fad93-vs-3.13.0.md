# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.03x slower
- HPT reliability: 58.65%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 278 ms: 1.05x slower                                           |
| docutils       | 2.58 sec                                               | 2.96 sec: 1.15x slower                                         |
| tornado_http   | 91.5 ms                                                | 94.9 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                  | 1.06x slower                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 388 ms: 1.20x faster                                           |
| async_tree_none            | 354 ms                                                 | 331 ms: 1.07x faster                                           |
| async_tree_none_tg         | 320 ms                                                 | 307 ms: 1.04x faster                                           |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 555 ms: 1.03x faster                                           |
| asyncio_websockets         | 555 ms                                                 | 559 ms: 1.01x slower                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                         |
| asyncio_tcp                | 488 ms                                                 | 498 ms: 1.02x slower                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 561 ms: 1.03x slower                                           |
| async_tree_io              | 843 ms                                                 | 897 ms: 1.06x slower                                           |
| async_generators           | 433 ms                                                 | 463 ms: 1.07x slower                                           |
| async_tree_io_tg           | 825 ms                                                 | 890 ms: 1.08x slower                                           |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (2): async_tree_memoization, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 85.7 ms                                                | 79.3 ms: 1.08x faster                                          |
| float          | 78.5 ms                                                | 74.3 ms: 1.06x faster                                          |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                           |
| Geometric mean | (ref)                                                  | 1.05x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.81 ms: 1.02x faster                                          |
| regex_dna      | 220 ms                                                 | 229 ms: 1.04x slower                                           |
| regex_compile  | 131 ms                                                 | 138 ms: 1.05x slower                                           |
| regex_v8       | 25.3 ms                                                | 26.8 ms: 1.06x slower                                          |
| Geometric mean | (ref)                                                  | 1.03x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 78.6 ms: 1.11x faster                                          |
| xml_etree_process    | 60.4 ms                                                | 54.8 ms: 1.10x faster                                          |
| tomli_loads          | 2.11 sec                                               | 1.93 sec: 1.10x faster                                         |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                           |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                          |
| xml_etree_iterparse  | 102 ms                                                 | 99.5 ms: 1.03x faster                                          |
| json_loads           | 27.0 us                                                | 26.8 us: 1.01x faster                                          |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                           |
| pickle_pure_python   | 300 us                                                 | 304 us: 1.01x slower                                           |
| pickle_list          | 5.01 us                                                | 5.08 us: 1.02x slower                                          |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                          |
| unpickle_list        | 4.96 us                                                | 5.11 us: 1.03x slower                                          |
| pickle_dict          | 33.2 us                                                | 35.0 us: 1.06x slower                                          |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                   |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.07 ms: 1.01x slower                                          |
| python_startup         | 10.6 ms                                                | 11.9 ms: 1.12x slower                                          |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.87 ms: 1.12x faster                                          |
| django_template | 34.4 ms                                                | 36.7 ms: 1.07x slower                                          |
| genshi_text     | 22.9 ms                                                | 25.0 ms: 1.09x slower                                          |
| genshi_xml      | 50.3 ms                                                | 59.7 ms: 1.19x slower                                          |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.8 us: 1.42x faster                                          |
| deepcopy                   | 352 us                                                 | 262 us: 1.34x faster                                           |
| scimark_fft                | 369 ms                                                 | 303 ms: 1.22x faster                                           |
| deepcopy_reduce            | 3.17 us                                                | 2.64 us: 1.20x faster                                          |
| async_tree_memoization_tg  | 465 ms                                                 | 388 ms: 1.20x faster                                           |
| richards_super             | 54.4 ms                                                | 46.9 ms: 1.16x faster                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.40 ms: 1.14x faster                                          |
| richards                   | 48.1 ms                                                | 42.6 ms: 1.13x faster                                          |
| mako                       | 11.1 ms                                                | 9.87 ms: 1.12x faster                                          |
| telco                      | 8.45 ms                                                | 7.64 ms: 1.11x faster                                          |
| xml_etree_generate         | 87.0 ms                                                | 78.6 ms: 1.11x faster                                          |
| xml_etree_process          | 60.4 ms                                                | 54.8 ms: 1.10x faster                                          |
| tomli_loads                | 2.11 sec                                               | 1.93 sec: 1.10x faster                                         |
| crypto_pyaes               | 73.0 ms                                                | 67.0 ms: 1.09x faster                                          |
| nbody                      | 85.7 ms                                                | 79.3 ms: 1.08x faster                                          |
| mdp                        | 2.74 sec                                               | 2.54 sec: 1.08x faster                                         |
| pathlib                    | 17.1 ms                                                | 15.8 ms: 1.08x faster                                          |
| async_tree_none            | 354 ms                                                 | 331 ms: 1.07x faster                                           |
| go                         | 142 ms                                                 | 132 ms: 1.07x faster                                           |
| pprint_safe_repr           | 744 ms                                                 | 697 ms: 1.07x faster                                           |
| logging_silent             | 102 ns                                                 | 96.0 ns: 1.06x faster                                          |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                           |
| float                      | 78.5 ms                                                | 74.3 ms: 1.06x faster                                          |
| scimark_monte_carlo        | 66.3 ms                                                | 62.8 ms: 1.06x faster                                          |
| scimark_lu                 | 115 ms                                                 | 109 ms: 1.05x faster                                           |
| async_tree_none_tg         | 320 ms                                                 | 307 ms: 1.04x faster                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.51 sec: 1.04x faster                                         |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.03x faster                                           |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 555 ms: 1.03x faster                                           |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                          |
| json                       | 5.20 ms                                                | 5.06 ms: 1.03x faster                                          |
| pprint_pformat             | 1.51 sec                                               | 1.47 sec: 1.03x faster                                         |
| xml_etree_iterparse        | 102 ms                                                 | 99.5 ms: 1.03x faster                                          |
| thrift                     | 796 us                                                 | 780 us: 1.02x faster                                           |
| regex_effbot               | 3.88 ms                                                | 3.81 ms: 1.02x faster                                          |
| logging_format             | 6.25 us                                                | 6.14 us: 1.02x faster                                          |
| pyflate                    | 460 ms                                                 | 453 ms: 1.02x faster                                           |
| logging_simple             | 5.66 us                                                | 5.58 us: 1.01x faster                                          |
| sqlite_synth               | 2.85 us                                                | 2.81 us: 1.01x faster                                          |
| json_loads                 | 27.0 us                                                | 26.8 us: 1.01x faster                                          |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                           |
| asyncio_websockets         | 555 ms                                                 | 559 ms: 1.01x slower                                           |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                           |
| pickle_pure_python         | 300 us                                                 | 304 us: 1.01x slower                                           |
| fannkuch                   | 381 ms                                                 | 385 ms: 1.01x slower                                           |
| python_startup_no_site     | 6.99 ms                                                | 7.07 ms: 1.01x slower                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                         |
| coverage                   | 83.7 ms                                                | 84.9 ms: 1.01x slower                                          |
| pickle_list                | 5.01 us                                                | 5.08 us: 1.02x slower                                          |
| chaos                      | 58.4 ms                                                | 59.5 ms: 1.02x slower                                          |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                          |
| pycparser                  | 1.19 sec                                               | 1.22 sec: 1.02x slower                                         |
| asyncio_tcp                | 488 ms                                                 | 498 ms: 1.02x slower                                           |
| deltablue                  | 3.15 ms                                                | 3.22 ms: 1.02x slower                                          |
| unpickle_list              | 4.96 us                                                | 5.11 us: 1.03x slower                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 561 ms: 1.03x slower                                           |
| tornado_http               | 91.5 ms                                                | 94.9 ms: 1.04x slower                                          |
| typing_runtime_protocols   | 159 us                                                 | 166 us: 1.04x slower                                           |
| regex_dna                  | 220 ms                                                 | 229 ms: 1.04x slower                                           |
| comprehensions             | 16.4 us                                                | 17.1 us: 1.04x slower                                          |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.05x slower                                          |
| 2to3                       | 265 ms                                                 | 278 ms: 1.05x slower                                           |
| regex_compile              | 131 ms                                                 | 138 ms: 1.05x slower                                           |
| pickle_dict                | 33.2 us                                                | 35.0 us: 1.06x slower                                          |
| regex_v8                   | 25.3 ms                                                | 26.8 ms: 1.06x slower                                          |
| raytrace                   | 262 ms                                                 | 277 ms: 1.06x slower                                           |
| dulwich_log                | 63.0 ms                                                | 66.9 ms: 1.06x slower                                          |
| async_tree_io              | 843 ms                                                 | 897 ms: 1.06x slower                                           |
| django_template            | 34.4 ms                                                | 36.7 ms: 1.07x slower                                          |
| sqlglot_normalize          | 107 ms                                                 | 115 ms: 1.07x slower                                           |
| sqlglot_transpile          | 1.57 ms                                                | 1.68 ms: 1.07x slower                                          |
| async_generators           | 433 ms                                                 | 463 ms: 1.07x slower                                           |
| async_tree_io_tg           | 825 ms                                                 | 890 ms: 1.08x slower                                           |
| sympy_expand               | 462 ms                                                 | 502 ms: 1.09x slower                                           |
| genshi_text                | 22.9 ms                                                | 25.0 ms: 1.09x slower                                          |
| sympy_str                  | 274 ms                                                 | 301 ms: 1.10x slower                                           |
| bench_thread_pool          | 815 us                                                 | 897 us: 1.10x slower                                           |
| sqlglot_optimize           | 53.9 ms                                                | 59.7 ms: 1.11x slower                                          |
| nqueens                    | 80.6 ms                                                | 89.3 ms: 1.11x slower                                          |
| python_startup             | 10.6 ms                                                | 11.9 ms: 1.12x slower                                          |
| gc_traversal               | 3.81 ms                                                | 4.29 ms: 1.13x slower                                          |
| hexiom                     | 6.13 ms                                                | 6.99 ms: 1.14x slower                                          |
| docutils                   | 2.58 sec                                               | 2.96 sec: 1.15x slower                                         |
| sympy_sum                  | 150 ms                                                 | 176 ms: 1.18x slower                                           |
| sympy_integrate            | 19.9 ms                                                | 23.4 ms: 1.18x slower                                          |
| genshi_xml                 | 50.3 ms                                                | 59.7 ms: 1.19x slower                                          |
| pylint                     | 313 ms                                                 | 374 ms: 1.20x slower                                           |
| generators                 | 28.8 ms                                                | 35.4 ms: 1.23x slower                                          |
| create_gc_cycles           | 1.61 ms                                                | 2.60 ms: 1.61x slower                                          |
| unpack_sequence            | 42.4 ns                                                | 108 ns: 2.55x slower                                           |
| bench_mp_pool              | 24.0 ms                                                | 84.4 ms: 3.52x slower                                          |
| Geometric mean             | (ref)                                                  | 1.03x slower                                                   |

Benchmark hidden because not significant (6): async_tree_memoization, unpickle, html5lib, meteor_contest, coroutines, scimark_sor
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241017-3.14.0a0-c2fad93-JIT/bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93.json: sphinx

# HPT report

- Reliability score: 58.65% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.20x