# Results vs. 3.13.0

- fork: faster-cpython
- ref: call_class_tier_2
- machine: linux-x86_64
- commit hash: af5ed4b
- commit date: 2024-08-19
- overall geometric mean: 1.14x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 322 ms: 1.22x slower                                                         |
| docutils       | 2.58 sec                                               | 3.26 sec: 1.26x slower                                                       |
| html5lib       | 64.5 ms                                                | 75.5 ms: 1.17x slower                                                        |
| tornado_http   | 91.5 ms                                                | 99.3 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                  | 1.18x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 410 ms: 1.13x faster                                                         |
| async_tree_none_tg         | 320 ms                                                 | 313 ms: 1.02x faster                                                         |
| async_tree_none            | 354 ms                                                 | 349 ms: 1.01x faster                                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 552 ms: 1.02x slower                                                         |
| asyncio_tcp                | 488 ms                                                 | 501 ms: 1.03x slower                                                         |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 594 ms: 1.04x slower                                                         |
| coroutines                 | 22.5 ms                                                | 23.9 ms: 1.06x slower                                                        |
| async_tree_io_tg           | 825 ms                                                 | 890 ms: 1.08x slower                                                         |
| async_generators           | 433 ms                                                 | 467 ms: 1.08x slower                                                         |
| async_tree_io              | 843 ms                                                 | 935 ms: 1.11x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                                         |
| float          | 78.5 ms                                                | 84.9 ms: 1.08x slower                                                        |
| nbody          | 85.7 ms                                                | 118 ms: 1.37x slower                                                         |
| Geometric mean | (ref)                                                  | 1.15x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.77 ms: 1.03x faster                                                        |
| regex_dna      | 220 ms                                                 | 221 ms: 1.00x slower                                                         |
| regex_v8       | 25.3 ms                                                | 25.8 ms: 1.02x slower                                                        |
| regex_compile  | 131 ms                                                 | 180 ms: 1.37x slower                                                         |
| Geometric mean | (ref)                                                  | 1.08x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 150 ms: 1.04x faster                                                         |
| json_dumps           | 10.4 ms                                                | 10.8 ms: 1.04x slower                                                        |
| xml_etree_iterparse  | 102 ms                                                 | 107 ms: 1.04x slower                                                         |
| json_loads           | 27.0 us                                                | 28.6 us: 1.06x slower                                                        |
| xml_etree_generate   | 87.0 ms                                                | 93.7 ms: 1.08x slower                                                        |
| xml_etree_process    | 60.4 ms                                                | 66.1 ms: 1.09x slower                                                        |
| tomli_loads          | 2.11 sec                                               | 2.44 sec: 1.16x slower                                                       |
| unpickle_pure_python | 213 us                                                 | 249 us: 1.17x slower                                                         |
| pickle_pure_python   | 300 us                                                 | 374 us: 1.24x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.09x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                        |
| python_startup_no_site | 6.99 ms                                                | 7.08 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 40.6 ms: 1.18x slower                                                        |
| mako            | 11.1 ms                                                | 13.5 ms: 1.21x slower                                                        |
| genshi_text     | 22.9 ms                                                | 28.7 ms: 1.25x slower                                                        |
| genshi_xml      | 50.3 ms                                                | 66.9 ms: 1.33x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.24x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 410 ms: 1.13x faster                                                         |
| deepcopy                   | 352 us                                                 | 321 us: 1.10x faster                                                         |
| deepcopy_reduce            | 3.17 us                                                | 2.94 us: 1.08x faster                                                        |
| xml_etree_parse            | 156 ms                                                 | 150 ms: 1.04x faster                                                         |
| deepcopy_memo              | 38.0 us                                                | 36.6 us: 1.04x faster                                                        |
| pathlib                    | 17.1 ms                                                | 16.5 ms: 1.04x faster                                                        |
| regex_effbot               | 3.88 ms                                                | 3.77 ms: 1.03x faster                                                        |
| async_tree_none_tg         | 320 ms                                                 | 313 ms: 1.02x faster                                                         |
| async_tree_none            | 354 ms                                                 | 349 ms: 1.01x faster                                                         |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                        |
| regex_dna                  | 220 ms                                                 | 221 ms: 1.00x slower                                                         |
| thrift                     | 796 us                                                 | 803 us: 1.01x slower                                                         |
| coverage                   | 83.7 ms                                                | 84.6 ms: 1.01x slower                                                        |
| pidigits                   | 186 ms                                                 | 189 ms: 1.01x slower                                                         |
| python_startup_no_site     | 6.99 ms                                                | 7.08 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 552 ms: 1.02x slower                                                         |
| regex_v8                   | 25.3 ms                                                | 25.8 ms: 1.02x slower                                                        |
| asyncio_tcp                | 488 ms                                                 | 501 ms: 1.03x slower                                                         |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 594 ms: 1.04x slower                                                         |
| json_dumps                 | 10.4 ms                                                | 10.8 ms: 1.04x slower                                                        |
| telco                      | 8.45 ms                                                | 8.80 ms: 1.04x slower                                                        |
| xml_etree_iterparse        | 102 ms                                                 | 107 ms: 1.04x slower                                                         |
| bench_thread_pool          | 815 us                                                 | 863 us: 1.06x slower                                                         |
| json_loads                 | 27.0 us                                                | 28.6 us: 1.06x slower                                                        |
| coroutines                 | 22.5 ms                                                | 23.9 ms: 1.06x slower                                                        |
| json                       | 5.20 ms                                                | 5.53 ms: 1.06x slower                                                        |
| xml_etree_generate         | 87.0 ms                                                | 93.7 ms: 1.08x slower                                                        |
| async_tree_io_tg           | 825 ms                                                 | 890 ms: 1.08x slower                                                         |
| async_generators           | 433 ms                                                 | 467 ms: 1.08x slower                                                         |
| float                      | 78.5 ms                                                | 84.9 ms: 1.08x slower                                                        |
| tornado_http               | 91.5 ms                                                | 99.3 ms: 1.08x slower                                                        |
| create_gc_cycles           | 1.61 ms                                                | 1.76 ms: 1.09x slower                                                        |
| xml_etree_process          | 60.4 ms                                                | 66.1 ms: 1.09x slower                                                        |
| async_tree_io              | 843 ms                                                 | 935 ms: 1.11x slower                                                         |
| meteor_contest             | 108 ms                                                 | 121 ms: 1.13x slower                                                         |
| logging_simple             | 5.66 us                                                | 6.42 us: 1.13x slower                                                        |
| scimark_fft                | 369 ms                                                 | 423 ms: 1.15x slower                                                         |
| tomli_loads                | 2.11 sec                                               | 2.44 sec: 1.16x slower                                                       |
| bpe_tokeniser              | 4.69 sec                                               | 5.44 sec: 1.16x slower                                                       |
| logging_format             | 6.25 us                                                | 7.28 us: 1.16x slower                                                        |
| scimark_lu                 | 115 ms                                                 | 134 ms: 1.17x slower                                                         |
| unpickle_pure_python       | 213 us                                                 | 249 us: 1.17x slower                                                         |
| html5lib                   | 64.5 ms                                                | 75.5 ms: 1.17x slower                                                        |
| spectral_norm              | 115 ms                                                 | 135 ms: 1.17x slower                                                         |
| typing_runtime_protocols   | 159 us                                                 | 187 us: 1.18x slower                                                         |
| django_template            | 34.4 ms                                                | 40.6 ms: 1.18x slower                                                        |
| crypto_pyaes               | 73.0 ms                                                | 86.7 ms: 1.19x slower                                                        |
| pylint                     | 313 ms                                                 | 372 ms: 1.19x slower                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.98 ms: 1.19x slower                                                        |
| pprint_safe_repr           | 744 ms                                                 | 890 ms: 1.20x slower                                                         |
| scimark_monte_carlo        | 66.3 ms                                                | 80.2 ms: 1.21x slower                                                        |
| pycparser                  | 1.19 sec                                               | 1.45 sec: 1.21x slower                                                       |
| mako                       | 11.1 ms                                                | 13.5 ms: 1.21x slower                                                        |
| logging_silent             | 102 ns                                                 | 124 ns: 1.22x slower                                                         |
| 2to3                       | 265 ms                                                 | 322 ms: 1.22x slower                                                         |
| scimark_sor                | 122 ms                                                 | 149 ms: 1.22x slower                                                         |
| pyflate                    | 460 ms                                                 | 560 ms: 1.22x slower                                                         |
| sympy_sum                  | 150 ms                                                 | 183 ms: 1.22x slower                                                         |
| sympy_str                  | 274 ms                                                 | 335 ms: 1.22x slower                                                         |
| sympy_expand               | 462 ms                                                 | 566 ms: 1.23x slower                                                         |
| sympy_integrate            | 19.9 ms                                                | 24.5 ms: 1.23x slower                                                        |
| sqlglot_optimize           | 53.9 ms                                                | 66.5 ms: 1.23x slower                                                        |
| fannkuch                   | 381 ms                                                 | 472 ms: 1.24x slower                                                         |
| sqlglot_normalize          | 107 ms                                                 | 134 ms: 1.24x slower                                                         |
| pprint_pformat             | 1.51 sec                                               | 1.88 sec: 1.24x slower                                                       |
| pickle_pure_python         | 300 us                                                 | 374 us: 1.24x slower                                                         |
| sqlglot_parse              | 1.27 ms                                                | 1.58 ms: 1.25x slower                                                        |
| go                         | 142 ms                                                 | 177 ms: 1.25x slower                                                         |
| genshi_text                | 22.9 ms                                                | 28.7 ms: 1.25x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.97 ms: 1.25x slower                                                        |
| docutils                   | 2.58 sec                                               | 3.26 sec: 1.26x slower                                                       |
| nqueens                    | 80.6 ms                                                | 104 ms: 1.29x slower                                                         |
| raytrace                   | 262 ms                                                 | 344 ms: 1.32x slower                                                         |
| genshi_xml                 | 50.3 ms                                                | 66.9 ms: 1.33x slower                                                        |
| regex_compile              | 131 ms                                                 | 180 ms: 1.37x slower                                                         |
| nbody                      | 85.7 ms                                                | 118 ms: 1.37x slower                                                         |
| comprehensions             | 16.4 us                                                | 22.8 us: 1.39x slower                                                        |
| richards_super             | 54.4 ms                                                | 76.0 ms: 1.40x slower                                                        |
| chaos                      | 58.4 ms                                                | 82.2 ms: 1.41x slower                                                        |
| richards                   | 48.1 ms                                                | 67.7 ms: 1.41x slower                                                        |
| generators                 | 28.8 ms                                                | 40.8 ms: 1.42x slower                                                        |
| deltablue                  | 3.15 ms                                                | 4.48 ms: 1.42x slower                                                        |
| hexiom                     | 6.13 ms                                                | 9.07 ms: 1.48x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.14x slower                                                                 |

Benchmark hidden because not significant (5): bench_mp_pool, gc_traversal, asyncio_websockets, mdp, async_tree_memoization
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 1.02x