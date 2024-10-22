# Results vs. 3.13.0

- fork: python
- ref: df13a1821a90fcfb75ec
- machine: linux-x86_64
- commit hash: df13a18
- commit date: 2024-08-01
- overall geometric mean: 1.01x faster
- HPT reliability: 75.81%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 274 ms: 1.04x slower                                                  |
| docutils       | 2.58 sec                                               | 2.91 sec: 1.13x slower                                                |
| html5lib       | 64.5 ms                                                | 65.2 ms: 1.01x slower                                                 |
| tornado_http   | 91.5 ms                                                | 92.3 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 396 ms: 1.17x faster                                                  |
| async_tree_none           | 354 ms                                                 | 328 ms: 1.08x faster                                                  |
| async_tree_none_tg        | 320 ms                                                 | 303 ms: 1.06x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 426 ms: 1.04x faster                                                  |
| asyncio_tcp               | 488 ms                                                 | 490 ms: 1.00x slower                                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                |
| async_tree_io_tg          | 825 ms                                                 | 871 ms: 1.06x slower                                                  |
| async_generators          | 433 ms                                                 | 466 ms: 1.08x slower                                                  |
| async_tree_io             | 843 ms                                                 | 910 ms: 1.08x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.6 ms: 1.10x faster                                                 |
| nbody          | 85.7 ms                                                | 79.8 ms: 1.07x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.75 ms: 1.04x faster                                                 |
| regex_compile  | 131 ms                                                 | 133 ms: 1.01x slower                                                  |
| regex_dna      | 220 ms                                                 | 223 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 80.0 ms: 1.09x faster                                                 |
| tomli_loads          | 2.11 sec                                               | 1.95 sec: 1.08x faster                                                |
| xml_etree_process    | 60.4 ms                                                | 56.0 ms: 1.08x faster                                                 |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 102 ms                                                 | 99.8 ms: 1.02x faster                                                 |
| pickle_pure_python   | 300 us                                                 | 297 us: 1.01x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                  |
| json_loads           | 27.0 us                                                | 27.9 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.14 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.82 ms: 1.13x faster                                                 |
| django_template | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                 |
| genshi_text     | 22.9 ms                                                | 24.7 ms: 1.08x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 54.5 ms: 1.08x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 29.0 us: 1.31x faster                                                 |
| deepcopy                  | 352 us                                                 | 273 us: 1.29x faster                                                  |
| scimark_fft               | 369 ms                                                 | 311 ms: 1.19x faster                                                  |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.24 ms: 1.19x faster                                                 |
| async_tree_memoization_tg | 465 ms                                                 | 396 ms: 1.17x faster                                                  |
| richards                  | 48.1 ms                                                | 41.1 ms: 1.17x faster                                                 |
| richards_super            | 54.4 ms                                                | 46.8 ms: 1.16x faster                                                 |
| mako                      | 11.1 ms                                                | 9.82 ms: 1.13x faster                                                 |
| deepcopy_reduce           | 3.17 us                                                | 2.82 us: 1.12x faster                                                 |
| spectral_norm             | 115 ms                                                 | 103 ms: 1.12x faster                                                  |
| float                     | 78.5 ms                                                | 71.6 ms: 1.10x faster                                                 |
| scimark_monte_carlo       | 66.3 ms                                                | 60.9 ms: 1.09x faster                                                 |
| xml_etree_generate        | 87.0 ms                                                | 80.0 ms: 1.09x faster                                                 |
| tomli_loads               | 2.11 sec                                               | 1.95 sec: 1.08x faster                                                |
| crypto_pyaes              | 73.0 ms                                                | 67.4 ms: 1.08x faster                                                 |
| async_tree_none           | 354 ms                                                 | 328 ms: 1.08x faster                                                  |
| xml_etree_process         | 60.4 ms                                                | 56.0 ms: 1.08x faster                                                 |
| nbody                     | 85.7 ms                                                | 79.8 ms: 1.07x faster                                                 |
| telco                     | 8.45 ms                                                | 7.95 ms: 1.06x faster                                                 |
| pyflate                   | 460 ms                                                 | 433 ms: 1.06x faster                                                  |
| xml_etree_parse           | 156 ms                                                 | 147 ms: 1.06x faster                                                  |
| async_tree_none_tg        | 320 ms                                                 | 303 ms: 1.06x faster                                                  |
| scimark_lu                | 115 ms                                                 | 109 ms: 1.06x faster                                                  |
| scimark_sor               | 122 ms                                                 | 117 ms: 1.05x faster                                                  |
| pathlib                   | 17.1 ms                                                | 16.3 ms: 1.05x faster                                                 |
| mdp                       | 2.74 sec                                               | 2.63 sec: 1.04x faster                                                |
| async_tree_memoization    | 442 ms                                                 | 426 ms: 1.04x faster                                                  |
| bpe_tokeniser             | 4.69 sec                                               | 4.51 sec: 1.04x faster                                                |
| regex_effbot              | 3.88 ms                                                | 3.75 ms: 1.04x faster                                                 |
| logging_format            | 6.25 us                                                | 6.06 us: 1.03x faster                                                 |
| fannkuch                  | 381 ms                                                 | 369 ms: 1.03x faster                                                  |
| meteor_contest            | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| xml_etree_iterparse       | 102 ms                                                 | 99.8 ms: 1.02x faster                                                 |
| pycparser                 | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                |
| gc_traversal              | 3.81 ms                                                | 3.74 ms: 1.02x faster                                                 |
| logging_simple            | 5.66 us                                                | 5.57 us: 1.02x faster                                                 |
| json                      | 5.20 ms                                                | 5.13 ms: 1.01x faster                                                 |
| chaos                     | 58.4 ms                                                | 57.8 ms: 1.01x faster                                                 |
| comprehensions            | 16.4 us                                                | 16.2 us: 1.01x faster                                                 |
| pickle_pure_python        | 300 us                                                 | 297 us: 1.01x faster                                                  |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| asyncio_tcp               | 488 ms                                                 | 490 ms: 1.00x slower                                                  |
| unpickle_pure_python      | 213 us                                                 | 215 us: 1.01x slower                                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                |
| bench_thread_pool         | 815 us                                                 | 821 us: 1.01x slower                                                  |
| tornado_http              | 91.5 ms                                                | 92.3 ms: 1.01x slower                                                 |
| html5lib                  | 64.5 ms                                                | 65.2 ms: 1.01x slower                                                 |
| regex_compile             | 131 ms                                                 | 133 ms: 1.01x slower                                                  |
| regex_dna                 | 220 ms                                                 | 223 ms: 1.01x slower                                                  |
| python_startup_no_site    | 6.99 ms                                                | 7.14 ms: 1.02x slower                                                 |
| sqlglot_parse             | 1.27 ms                                                | 1.30 ms: 1.03x slower                                                 |
| sqlglot_transpile         | 1.57 ms                                                | 1.62 ms: 1.03x slower                                                 |
| go                        | 142 ms                                                 | 146 ms: 1.03x slower                                                  |
| json_loads                | 27.0 us                                                | 27.9 us: 1.03x slower                                                 |
| logging_silent            | 102 ns                                                 | 106 ns: 1.03x slower                                                  |
| sqlglot_optimize          | 53.9 ms                                                | 55.8 ms: 1.04x slower                                                 |
| raytrace                  | 262 ms                                                 | 271 ms: 1.04x slower                                                  |
| 2to3                      | 265 ms                                                 | 274 ms: 1.04x slower                                                  |
| django_template           | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                 |
| sqlglot_normalize         | 107 ms                                                 | 113 ms: 1.05x slower                                                  |
| async_tree_io_tg          | 825 ms                                                 | 871 ms: 1.06x slower                                                  |
| typing_runtime_protocols  | 159 us                                                 | 168 us: 1.06x slower                                                  |
| nqueens                   | 80.6 ms                                                | 86.4 ms: 1.07x slower                                                 |
| async_generators          | 433 ms                                                 | 466 ms: 1.08x slower                                                  |
| genshi_text               | 22.9 ms                                                | 24.7 ms: 1.08x slower                                                 |
| async_tree_io             | 843 ms                                                 | 910 ms: 1.08x slower                                                  |
| dask                      | 338 ms                                                 | 365 ms: 1.08x slower                                                  |
| genshi_xml                | 50.3 ms                                                | 54.5 ms: 1.08x slower                                                 |
| coverage                  | 83.7 ms                                                | 91.3 ms: 1.09x slower                                                 |
| create_gc_cycles          | 1.61 ms                                                | 1.76 ms: 1.09x slower                                                 |
| sympy_str                 | 274 ms                                                 | 300 ms: 1.10x slower                                                  |
| hexiom                    | 6.13 ms                                                | 6.73 ms: 1.10x slower                                                 |
| sympy_expand              | 462 ms                                                 | 510 ms: 1.11x slower                                                  |
| docutils                  | 2.58 sec                                               | 2.91 sec: 1.13x slower                                                |
| pylint                    | 313 ms                                                 | 355 ms: 1.13x slower                                                  |
| sympy_integrate           | 19.9 ms                                                | 22.6 ms: 1.14x slower                                                 |
| sympy_sum                 | 150 ms                                                 | 170 ms: 1.14x slower                                                  |
| deltablue                 | 3.15 ms                                                | 3.60 ms: 1.14x slower                                                 |
| generators                | 28.8 ms                                                | 33.1 ms: 1.15x slower                                                 |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, pprint_safe_repr, json_dumps, thrift, asyncio_websockets, regex_v8, pprint_pformat, bench_mp_pool, coroutines
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 75.81% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x