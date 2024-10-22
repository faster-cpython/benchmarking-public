# Results vs. 3.13.0

- fork: faster-cpython
- ref: call_class_tier_2
- machine: linux-x86_64
- commit hash: ae8208f
- commit date: 2024-08-20
- overall geometric mean: 1.15x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 327 ms: 1.23x slower                                                         |
| docutils       | 2.58 sec                                               | 3.26 sec: 1.26x slower                                                       |
| html5lib       | 64.5 ms                                                | 75.9 ms: 1.18x slower                                                        |
| tornado_http   | 91.5 ms                                                | 98.6 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                  | 1.19x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 411 ms: 1.13x faster                                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 552 ms: 1.02x slower                                                         |
| asyncio_tcp                | 488 ms                                                 | 500 ms: 1.02x slower                                                         |
| async_tree_memoization     | 442 ms                                                 | 456 ms: 1.03x slower                                                         |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 595 ms: 1.04x slower                                                         |
| async_tree_io_tg           | 825 ms                                                 | 875 ms: 1.06x slower                                                         |
| coroutines                 | 22.5 ms                                                | 23.9 ms: 1.06x slower                                                        |
| async_generators           | 433 ms                                                 | 467 ms: 1.08x slower                                                         |
| async_tree_io              | 843 ms                                                 | 931 ms: 1.10x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (3): async_tree_none, async_tree_none_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                                         |
| float          | 78.5 ms                                                | 84.3 ms: 1.07x slower                                                        |
| nbody          | 85.7 ms                                                | 120 ms: 1.40x slower                                                         |
| Geometric mean | (ref)                                                  | 1.15x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.65 ms: 1.06x faster                                                        |
| regex_dna      | 220 ms                                                 | 226 ms: 1.03x slower                                                         |
| regex_v8       | 25.3 ms                                                | 26.6 ms: 1.05x slower                                                        |
| regex_compile  | 131 ms                                                 | 183 ms: 1.39x slower                                                         |
| Geometric mean | (ref)                                                  | 1.09x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 150 ms: 1.04x faster                                                         |
| xml_etree_iterparse  | 102 ms                                                 | 108 ms: 1.06x slower                                                         |
| json_loads           | 27.0 us                                                | 28.6 us: 1.06x slower                                                        |
| xml_etree_generate   | 87.0 ms                                                | 94.2 ms: 1.08x slower                                                        |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                        |
| xml_etree_process    | 60.4 ms                                                | 66.5 ms: 1.10x slower                                                        |
| unpickle_pure_python | 213 us                                                 | 253 us: 1.19x slower                                                         |
| tomli_loads          | 2.11 sec                                               | 2.54 sec: 1.20x slower                                                       |
| pickle_pure_python   | 300 us                                                 | 384 us: 1.28x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                        |
| python_startup_no_site | 6.99 ms                                                | 7.11 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 40.9 ms: 1.19x slower                                                        |
| mako            | 11.1 ms                                                | 13.6 ms: 1.22x slower                                                        |
| genshi_text     | 22.9 ms                                                | 28.6 ms: 1.25x slower                                                        |
| genshi_xml      | 50.3 ms                                                | 67.6 ms: 1.34x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.25x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 411 ms: 1.13x faster                                                         |
| deepcopy                   | 352 us                                                 | 323 us: 1.09x faster                                                         |
| regex_effbot               | 3.88 ms                                                | 3.65 ms: 1.06x faster                                                        |
| deepcopy_reduce            | 3.17 us                                                | 3.02 us: 1.05x faster                                                        |
| xml_etree_parse            | 156 ms                                                 | 150 ms: 1.04x faster                                                         |
| gc_traversal               | 3.81 ms                                                | 3.73 ms: 1.02x faster                                                        |
| pathlib                    | 17.1 ms                                                | 16.8 ms: 1.01x faster                                                        |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                       |
| pidigits                   | 186 ms                                                 | 189 ms: 1.01x slower                                                         |
| coverage                   | 83.7 ms                                                | 84.9 ms: 1.01x slower                                                        |
| thrift                     | 796 us                                                 | 807 us: 1.01x slower                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 552 ms: 1.02x slower                                                         |
| python_startup_no_site     | 6.99 ms                                                | 7.11 ms: 1.02x slower                                                        |
| deepcopy_memo              | 38.0 us                                                | 38.8 us: 1.02x slower                                                        |
| asyncio_tcp                | 488 ms                                                 | 500 ms: 1.02x slower                                                         |
| async_tree_memoization     | 442 ms                                                 | 456 ms: 1.03x slower                                                         |
| regex_dna                  | 220 ms                                                 | 226 ms: 1.03x slower                                                         |
| telco                      | 8.45 ms                                                | 8.76 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 595 ms: 1.04x slower                                                         |
| regex_v8                   | 25.3 ms                                                | 26.6 ms: 1.05x slower                                                        |
| mdp                        | 2.74 sec                                               | 2.89 sec: 1.05x slower                                                       |
| xml_etree_iterparse        | 102 ms                                                 | 108 ms: 1.06x slower                                                         |
| async_tree_io_tg           | 825 ms                                                 | 875 ms: 1.06x slower                                                         |
| json_loads                 | 27.0 us                                                | 28.6 us: 1.06x slower                                                        |
| coroutines                 | 22.5 ms                                                | 23.9 ms: 1.06x slower                                                        |
| bench_thread_pool          | 815 us                                                 | 866 us: 1.06x slower                                                         |
| float                      | 78.5 ms                                                | 84.3 ms: 1.07x slower                                                        |
| json                       | 5.20 ms                                                | 5.59 ms: 1.07x slower                                                        |
| tornado_http               | 91.5 ms                                                | 98.6 ms: 1.08x slower                                                        |
| async_generators           | 433 ms                                                 | 467 ms: 1.08x slower                                                         |
| xml_etree_generate         | 87.0 ms                                                | 94.2 ms: 1.08x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                        |
| xml_etree_process          | 60.4 ms                                                | 66.5 ms: 1.10x slower                                                        |
| async_tree_io              | 843 ms                                                 | 931 ms: 1.10x slower                                                         |
| create_gc_cycles           | 1.61 ms                                                | 1.78 ms: 1.11x slower                                                        |
| meteor_contest             | 108 ms                                                 | 122 ms: 1.13x slower                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.82 ms: 1.16x slower                                                        |
| scimark_lu                 | 115 ms                                                 | 134 ms: 1.16x slower                                                         |
| bpe_tokeniser              | 4.69 sec                                               | 5.46 sec: 1.16x slower                                                       |
| logging_simple             | 5.66 us                                                | 6.63 us: 1.17x slower                                                        |
| typing_runtime_protocols   | 159 us                                                 | 187 us: 1.17x slower                                                         |
| scimark_fft                | 369 ms                                                 | 433 ms: 1.17x slower                                                         |
| html5lib                   | 64.5 ms                                                | 75.9 ms: 1.18x slower                                                        |
| unpickle_pure_python       | 213 us                                                 | 253 us: 1.19x slower                                                         |
| django_template            | 34.4 ms                                                | 40.9 ms: 1.19x slower                                                        |
| crypto_pyaes               | 73.0 ms                                                | 87.0 ms: 1.19x slower                                                        |
| pylint                     | 313 ms                                                 | 374 ms: 1.19x slower                                                         |
| logging_format             | 6.25 us                                                | 7.48 us: 1.20x slower                                                        |
| tomli_loads                | 2.11 sec                                               | 2.54 sec: 1.20x slower                                                       |
| spectral_norm              | 115 ms                                                 | 139 ms: 1.21x slower                                                         |
| pyflate                    | 460 ms                                                 | 558 ms: 1.21x slower                                                         |
| scimark_monte_carlo        | 66.3 ms                                                | 80.8 ms: 1.22x slower                                                        |
| sympy_expand               | 462 ms                                                 | 563 ms: 1.22x slower                                                         |
| sympy_sum                  | 150 ms                                                 | 183 ms: 1.22x slower                                                         |
| mako                       | 11.1 ms                                                | 13.6 ms: 1.22x slower                                                        |
| pprint_safe_repr           | 744 ms                                                 | 911 ms: 1.22x slower                                                         |
| pycparser                  | 1.19 sec                                               | 1.47 sec: 1.23x slower                                                       |
| 2to3                       | 265 ms                                                 | 327 ms: 1.23x slower                                                         |
| sympy_integrate            | 19.9 ms                                                | 24.5 ms: 1.23x slower                                                        |
| sympy_str                  | 274 ms                                                 | 338 ms: 1.23x slower                                                         |
| go                         | 142 ms                                                 | 175 ms: 1.24x slower                                                         |
| sqlglot_optimize           | 53.9 ms                                                | 67.0 ms: 1.24x slower                                                        |
| genshi_text                | 22.9 ms                                                | 28.6 ms: 1.25x slower                                                        |
| fannkuch                   | 381 ms                                                 | 478 ms: 1.25x slower                                                         |
| docutils                   | 2.58 sec                                               | 3.26 sec: 1.26x slower                                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.60 ms: 1.26x slower                                                        |
| sqlglot_normalize          | 107 ms                                                 | 136 ms: 1.26x slower                                                         |
| sqlglot_transpile          | 1.57 ms                                                | 2.00 ms: 1.27x slower                                                        |
| pprint_pformat             | 1.51 sec                                               | 1.93 sec: 1.28x slower                                                       |
| pickle_pure_python         | 300 us                                                 | 384 us: 1.28x slower                                                         |
| scimark_sor                | 122 ms                                                 | 157 ms: 1.28x slower                                                         |
| nqueens                    | 80.6 ms                                                | 104 ms: 1.29x slower                                                         |
| logging_silent             | 102 ns                                                 | 132 ns: 1.30x slower                                                         |
| raytrace                   | 262 ms                                                 | 349 ms: 1.33x slower                                                         |
| genshi_xml                 | 50.3 ms                                                | 67.6 ms: 1.34x slower                                                        |
| regex_compile              | 131 ms                                                 | 183 ms: 1.39x slower                                                         |
| nbody                      | 85.7 ms                                                | 120 ms: 1.40x slower                                                         |
| generators                 | 28.8 ms                                                | 40.2 ms: 1.40x slower                                                        |
| chaos                      | 58.4 ms                                                | 83.4 ms: 1.43x slower                                                        |
| comprehensions             | 16.4 us                                                | 24.2 us: 1.47x slower                                                        |
| richards_super             | 54.4 ms                                                | 80.7 ms: 1.48x slower                                                        |
| deltablue                  | 3.15 ms                                                | 4.70 ms: 1.49x slower                                                        |
| richards                   | 48.1 ms                                                | 72.0 ms: 1.50x slower                                                        |
| hexiom                     | 6.13 ms                                                | 9.54 ms: 1.56x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.15x slower                                                                 |

Benchmark hidden because not significant (4): async_tree_none, async_tree_none_tg, bench_mp_pool, asyncio_websockets
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 1.02x