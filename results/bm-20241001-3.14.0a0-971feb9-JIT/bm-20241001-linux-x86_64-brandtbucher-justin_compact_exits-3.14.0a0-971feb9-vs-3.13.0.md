# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: 971feb9
- commit date: 2024-10-01
- overall geometric mean: 1.00x faster
- HPT reliability: 94.01%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 277 ms: 1.05x slower                                                        |
| html5lib       | 64.5 ms                                                | 62.7 ms: 1.03x faster                                                       |
| tornado_http   | 91.5 ms                                                | 94.1 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 405 ms: 1.09x faster                                                        |
| async_tree_none            | 354 ms                                                 | 325 ms: 1.09x faster                                                        |
| asyncio_tcp                | 488 ms                                                 | 484 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 558 ms: 1.03x slower                                                        |
| async_tree_io              | 843 ms                                                 | 892 ms: 1.06x slower                                                        |
| async_generators           | 433 ms                                                 | 461 ms: 1.06x slower                                                        |
| async_tree_io_tg           | 825 ms                                                 | 883 ms: 1.07x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.4 ms: 1.10x faster                                                       |
| nbody          | 85.7 ms                                                | 82.8 ms: 1.04x faster                                                       |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.61 ms: 1.07x faster                                                       |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                                        |
| regex_v8       | 25.3 ms                                                | 25.1 ms: 1.01x faster                                                       |
| regex_compile  | 131 ms                                                 | 140 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate  | 87.0 ms                                                | 76.7 ms: 1.13x faster                                                       |
| tomli_loads         | 2.11 sec                                               | 1.88 sec: 1.12x faster                                                      |
| xml_etree_process   | 60.4 ms                                                | 54.1 ms: 1.12x faster                                                       |
| xml_etree_parse     | 156 ms                                                 | 146 ms: 1.06x faster                                                        |
| xml_etree_iterparse | 102 ms                                                 | 98.7 ms: 1.03x faster                                                       |
| json_dumps          | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                       |
| unpickle            | 14.9 us                                                | 14.6 us: 1.02x faster                                                       |
| json_loads          | 27.0 us                                                | 26.8 us: 1.01x faster                                                       |
| pickle_list         | 5.01 us                                                | 5.06 us: 1.01x slower                                                       |
| pickle              | 11.6 us                                                | 11.8 us: 1.02x slower                                                       |
| pickle_pure_python  | 300 us                                                 | 307 us: 1.02x slower                                                        |
| pickle_dict         | 33.2 us                                                | 34.1 us: 1.03x slower                                                       |
| unpickle_list       | 4.96 us                                                | 5.25 us: 1.06x slower                                                       |
| Geometric mean      | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.09 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.79 ms: 1.13x faster                                                       |
| django_template | 34.4 ms                                                | 35.4 ms: 1.03x slower                                                       |
| genshi_text     | 22.9 ms                                                | 25.0 ms: 1.09x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 57.7 ms: 1.15x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| richards                   | 48.1 ms                                                | 32.7 ms: 1.47x faster                                                       |
| deepcopy_memo              | 38.0 us                                                | 26.8 us: 1.42x faster                                                       |
| richards_super             | 54.4 ms                                                | 38.5 ms: 1.41x faster                                                       |
| deepcopy                   | 352 us                                                 | 261 us: 1.35x faster                                                        |
| scimark_fft                | 369 ms                                                 | 307 ms: 1.20x faster                                                        |
| deepcopy_reduce            | 3.17 us                                                | 2.66 us: 1.19x faster                                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.40 ms: 1.14x faster                                                       |
| xml_etree_generate         | 87.0 ms                                                | 76.7 ms: 1.13x faster                                                       |
| mako                       | 11.1 ms                                                | 9.79 ms: 1.13x faster                                                       |
| crypto_pyaes               | 73.0 ms                                                | 64.9 ms: 1.12x faster                                                       |
| tomli_loads                | 2.11 sec                                               | 1.88 sec: 1.12x faster                                                      |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                        |
| xml_etree_process          | 60.4 ms                                                | 54.1 ms: 1.12x faster                                                       |
| go                         | 142 ms                                                 | 127 ms: 1.11x faster                                                        |
| telco                      | 8.45 ms                                                | 7.63 ms: 1.11x faster                                                       |
| float                      | 78.5 ms                                                | 71.4 ms: 1.10x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 405 ms: 1.09x faster                                                        |
| pathlib                    | 17.1 ms                                                | 15.6 ms: 1.09x faster                                                       |
| async_tree_none            | 354 ms                                                 | 325 ms: 1.09x faster                                                        |
| mdp                        | 2.74 sec                                               | 2.53 sec: 1.08x faster                                                      |
| pprint_safe_repr           | 744 ms                                                 | 691 ms: 1.08x faster                                                        |
| regex_effbot               | 3.88 ms                                                | 3.61 ms: 1.07x faster                                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.39 sec: 1.07x faster                                                      |
| scimark_monte_carlo        | 66.3 ms                                                | 62.2 ms: 1.07x faster                                                       |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.06x faster                                                        |
| pprint_pformat             | 1.51 sec                                               | 1.44 sec: 1.05x faster                                                      |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.04x faster                                                        |
| pyflate                    | 460 ms                                                 | 441 ms: 1.04x faster                                                        |
| sqlite_synth               | 2.85 us                                                | 2.74 us: 1.04x faster                                                       |
| fannkuch                   | 381 ms                                                 | 366 ms: 1.04x faster                                                        |
| nbody                      | 85.7 ms                                                | 82.8 ms: 1.04x faster                                                       |
| pycparser                  | 1.19 sec                                               | 1.15 sec: 1.03x faster                                                      |
| xml_etree_iterparse        | 102 ms                                                 | 98.7 ms: 1.03x faster                                                       |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                       |
| scimark_lu                 | 115 ms                                                 | 111 ms: 1.03x faster                                                        |
| html5lib                   | 64.5 ms                                                | 62.7 ms: 1.03x faster                                                       |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.02x faster                                                        |
| logging_format             | 6.25 us                                                | 6.11 us: 1.02x faster                                                       |
| json                       | 5.20 ms                                                | 5.10 ms: 1.02x faster                                                       |
| unpickle                   | 14.9 us                                                | 14.6 us: 1.02x faster                                                       |
| regex_dna                  | 220 ms                                                 | 217 ms: 1.01x faster                                                        |
| comprehensions             | 16.4 us                                                | 16.2 us: 1.01x faster                                                       |
| asyncio_tcp                | 488 ms                                                 | 484 ms: 1.01x faster                                                        |
| logging_simple             | 5.66 us                                                | 5.62 us: 1.01x faster                                                       |
| deltablue                  | 3.15 ms                                                | 3.13 ms: 1.01x faster                                                       |
| json_loads                 | 27.0 us                                                | 26.8 us: 1.01x faster                                                       |
| pidigits                   | 186 ms                                                 | 185 ms: 1.01x faster                                                        |
| regex_v8                   | 25.3 ms                                                | 25.1 ms: 1.01x faster                                                       |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| pickle_list                | 5.01 us                                                | 5.06 us: 1.01x slower                                                       |
| python_startup_no_site     | 6.99 ms                                                | 7.09 ms: 1.01x slower                                                       |
| chaos                      | 58.4 ms                                                | 59.3 ms: 1.02x slower                                                       |
| gc_traversal               | 3.81 ms                                                | 3.88 ms: 1.02x slower                                                       |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                                       |
| pickle_pure_python         | 300 us                                                 | 307 us: 1.02x slower                                                        |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 558 ms: 1.03x slower                                                        |
| coverage                   | 83.7 ms                                                | 85.9 ms: 1.03x slower                                                       |
| logging_silent             | 102 ns                                                 | 105 ns: 1.03x slower                                                        |
| pickle_dict                | 33.2 us                                                | 34.1 us: 1.03x slower                                                       |
| tornado_http               | 91.5 ms                                                | 94.1 ms: 1.03x slower                                                       |
| django_template            | 34.4 ms                                                | 35.4 ms: 1.03x slower                                                       |
| typing_runtime_protocols   | 159 us                                                 | 164 us: 1.03x slower                                                        |
| sqlglot_parse              | 1.27 ms                                                | 1.31 ms: 1.03x slower                                                       |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                                        |
| 2to3                       | 265 ms                                                 | 277 ms: 1.05x slower                                                        |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.05x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.65 ms: 1.05x slower                                                       |
| unpickle_list              | 4.96 us                                                | 5.25 us: 1.06x slower                                                       |
| async_tree_io              | 843 ms                                                 | 892 ms: 1.06x slower                                                        |
| regex_compile              | 131 ms                                                 | 140 ms: 1.06x slower                                                        |
| async_generators           | 433 ms                                                 | 461 ms: 1.06x slower                                                        |
| async_tree_io_tg           | 825 ms                                                 | 883 ms: 1.07x slower                                                        |
| dulwich_log                | 63.0 ms                                                | 67.6 ms: 1.07x slower                                                       |
| create_gc_cycles           | 1.61 ms                                                | 1.73 ms: 1.08x slower                                                       |
| sympy_expand               | 462 ms                                                 | 500 ms: 1.08x slower                                                        |
| sympy_str                  | 274 ms                                                 | 298 ms: 1.09x slower                                                        |
| hexiom                     | 6.13 ms                                                | 6.67 ms: 1.09x slower                                                       |
| bench_thread_pool          | 815 us                                                 | 891 us: 1.09x slower                                                        |
| genshi_text                | 22.9 ms                                                | 25.0 ms: 1.09x slower                                                       |
| nqueens                    | 80.6 ms                                                | 89.6 ms: 1.11x slower                                                       |
| sympy_integrate            | 19.9 ms                                                | 22.6 ms: 1.14x slower                                                       |
| genshi_xml                 | 50.3 ms                                                | 57.7 ms: 1.15x slower                                                       |
| pylint                     | 313 ms                                                 | 364 ms: 1.16x slower                                                        |
| generators                 | 28.8 ms                                                | 34.1 ms: 1.18x slower                                                       |
| sympy_sum                  | 150 ms                                                 | 177 ms: 1.18x slower                                                        |
| unpack_sequence            | 42.4 ns                                                | 105 ns: 2.47x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 60.8 ms: 2.53x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_cpu_io_mixed, thrift, unpickle_pure_python, asyncio_websockets
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, docutils, flaskblogging, gunicorn, mypy2, sqlglot_optimize

# HPT report

- Reliability score: 94.01% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x