# Results vs. 3.13.0

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 190fbfa
- commit date: 2024-07-14
- overall geometric mean: 1.01x slower
- HPT reliability: 69.97%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 273 ms: 1.03x slower                                                      |
| docutils       | 2.58 sec                                               | 2.98 sec: 1.15x slower                                                    |
| html5lib       | 64.5 ms                                                | 71.6 ms: 1.11x slower                                                     |
| tornado_http   | 91.5 ms                                                | 98.3 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                  | 1.09x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 383 ms: 1.21x faster                                                      |
| async_tree_none           | 354 ms                                                 | 328 ms: 1.08x faster                                                      |
| async_tree_memoization    | 442 ms                                                 | 412 ms: 1.07x faster                                                      |
| async_tree_none_tg        | 320 ms                                                 | 305 ms: 1.05x faster                                                      |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                    |
| async_tree_io_tg          | 825 ms                                                 | 867 ms: 1.05x slower                                                      |
| asyncio_tcp               | 488 ms                                                 | 518 ms: 1.06x slower                                                      |
| async_tree_io             | 843 ms                                                 | 910 ms: 1.08x slower                                                      |
| async_generators          | 433 ms                                                 | 514 ms: 1.19x slower                                                      |
| coroutines                | 22.5 ms                                                | 27.6 ms: 1.23x slower                                                     |
| Geometric mean            | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.4 ms: 1.11x faster                                                     |
| nbody          | 85.7 ms                                                | 77.0 ms: 1.11x faster                                                     |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.61 ms: 1.08x faster                                                     |
| regex_v8       | 25.3 ms                                                | 23.7 ms: 1.07x faster                                                     |
| regex_compile  | 131 ms                                                 | 132 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.93 sec: 1.10x faster                                                    |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                      |
| xml_etree_generate   | 87.0 ms                                                | 84.3 ms: 1.03x faster                                                     |
| xml_etree_process    | 60.4 ms                                                | 58.6 ms: 1.03x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                      |
| pickle_pure_python   | 300 us                                                 | 304 us: 1.01x slower                                                      |
| xml_etree_iterparse  | 102 ms                                                 | 103 ms: 1.01x slower                                                      |
| json_loads           | 27.0 us                                                | 27.5 us: 1.02x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                     |
| python_startup_no_site | 6.99 ms                                                | 7.13 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.96 ms: 1.11x faster                                                     |
| django_template | 34.4 ms                                                | 40.4 ms: 1.17x slower                                                     |
| genshi_text     | 22.9 ms                                                | 27.7 ms: 1.21x slower                                                     |
| genshi_xml      | 50.3 ms                                                | 63.3 ms: 1.26x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.13x slower                                                              |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 26.6 us: 1.43x faster                                                     |
| deepcopy                  | 352 us                                                 | 258 us: 1.36x faster                                                      |
| richards                  | 48.1 ms                                                | 39.1 ms: 1.23x faster                                                     |
| async_tree_memoization_tg | 465 ms                                                 | 383 ms: 1.21x faster                                                      |
| richards_super            | 54.4 ms                                                | 45.3 ms: 1.20x faster                                                     |
| deepcopy_reduce           | 3.17 us                                                | 2.68 us: 1.18x faster                                                     |
| scimark_fft               | 369 ms                                                 | 313 ms: 1.18x faster                                                      |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.36 ms: 1.15x faster                                                     |
| spectral_norm             | 115 ms                                                 | 101 ms: 1.14x faster                                                      |
| float                     | 78.5 ms                                                | 70.4 ms: 1.11x faster                                                     |
| mako                      | 11.1 ms                                                | 9.96 ms: 1.11x faster                                                     |
| nbody                     | 85.7 ms                                                | 77.0 ms: 1.11x faster                                                     |
| tomli_loads               | 2.11 sec                                               | 1.93 sec: 1.10x faster                                                    |
| crypto_pyaes              | 73.0 ms                                                | 66.7 ms: 1.09x faster                                                     |
| async_tree_none           | 354 ms                                                 | 328 ms: 1.08x faster                                                      |
| regex_effbot              | 3.88 ms                                                | 3.61 ms: 1.08x faster                                                     |
| async_tree_memoization    | 442 ms                                                 | 412 ms: 1.07x faster                                                      |
| pathlib                   | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                     |
| regex_v8                  | 25.3 ms                                                | 23.7 ms: 1.07x faster                                                     |
| pycparser                 | 1.19 sec                                               | 1.13 sec: 1.06x faster                                                    |
| telco                     | 8.45 ms                                                | 8.00 ms: 1.06x faster                                                     |
| xml_etree_parse           | 156 ms                                                 | 148 ms: 1.05x faster                                                      |
| async_tree_none_tg        | 320 ms                                                 | 305 ms: 1.05x faster                                                      |
| scimark_monte_carlo       | 66.3 ms                                                | 63.4 ms: 1.05x faster                                                     |
| chaos                     | 58.4 ms                                                | 56.0 ms: 1.04x faster                                                     |
| pprint_safe_repr          | 744 ms                                                 | 715 ms: 1.04x faster                                                      |
| fannkuch                  | 381 ms                                                 | 366 ms: 1.04x faster                                                      |
| pprint_pformat            | 1.51 sec                                               | 1.46 sec: 1.03x faster                                                    |
| xml_etree_generate        | 87.0 ms                                                | 84.3 ms: 1.03x faster                                                     |
| xml_etree_process         | 60.4 ms                                                | 58.6 ms: 1.03x faster                                                     |
| logging_format            | 6.25 us                                                | 6.09 us: 1.03x faster                                                     |
| pyflate                   | 460 ms                                                 | 449 ms: 1.02x faster                                                      |
| logging_simple            | 5.66 us                                                | 5.54 us: 1.02x faster                                                     |
| gc_traversal              | 3.81 ms                                                | 3.73 ms: 1.02x faster                                                     |
| json                      | 5.20 ms                                                | 5.10 ms: 1.02x faster                                                     |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.01x faster                                                      |
| go                        | 142 ms                                                 | 140 ms: 1.01x faster                                                      |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                     |
| sqlglot_parse             | 1.27 ms                                                | 1.27 ms: 1.01x slower                                                     |
| regex_compile             | 131 ms                                                 | 132 ms: 1.01x slower                                                      |
| bpe_tokeniser             | 4.69 sec                                               | 4.73 sec: 1.01x slower                                                    |
| unpickle_pure_python      | 213 us                                                 | 215 us: 1.01x slower                                                      |
| pidigits                  | 186 ms                                                 | 188 ms: 1.01x slower                                                      |
| pickle_pure_python        | 300 us                                                 | 304 us: 1.01x slower                                                      |
| thrift                    | 796 us                                                 | 807 us: 1.01x slower                                                      |
| xml_etree_iterparse       | 102 ms                                                 | 103 ms: 1.01x slower                                                      |
| json_loads                | 27.0 us                                                | 27.5 us: 1.02x slower                                                     |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                    |
| python_startup_no_site    | 6.99 ms                                                | 7.13 ms: 1.02x slower                                                     |
| sqlglot_transpile         | 1.57 ms                                                | 1.62 ms: 1.03x slower                                                     |
| raytrace                  | 262 ms                                                 | 269 ms: 1.03x slower                                                      |
| 2to3                      | 265 ms                                                 | 273 ms: 1.03x slower                                                      |
| scimark_lu                | 115 ms                                                 | 119 ms: 1.03x slower                                                      |
| scimark_sor               | 122 ms                                                 | 127 ms: 1.03x slower                                                      |
| sqlglot_normalize         | 107 ms                                                 | 113 ms: 1.05x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 867 ms: 1.05x slower                                                      |
| bench_thread_pool         | 815 us                                                 | 857 us: 1.05x slower                                                      |
| sympy_expand              | 462 ms                                                 | 489 ms: 1.06x slower                                                      |
| dulwich_log               | 63.0 ms                                                | 66.7 ms: 1.06x slower                                                     |
| asyncio_tcp               | 488 ms                                                 | 518 ms: 1.06x slower                                                      |
| sqlglot_optimize          | 53.9 ms                                                | 57.3 ms: 1.06x slower                                                     |
| hexiom                    | 6.13 ms                                                | 6.52 ms: 1.06x slower                                                     |
| typing_runtime_protocols  | 159 us                                                 | 171 us: 1.07x slower                                                      |
| tornado_http              | 91.5 ms                                                | 98.3 ms: 1.07x slower                                                     |
| async_tree_io             | 843 ms                                                 | 910 ms: 1.08x slower                                                      |
| deltablue                 | 3.15 ms                                                | 3.42 ms: 1.09x slower                                                     |
| create_gc_cycles          | 1.61 ms                                                | 1.76 ms: 1.09x slower                                                     |
| sympy_str                 | 274 ms                                                 | 300 ms: 1.10x slower                                                      |
| coverage                  | 83.7 ms                                                | 92.4 ms: 1.10x slower                                                     |
| html5lib                  | 64.5 ms                                                | 71.6 ms: 1.11x slower                                                     |
| sympy_sum                 | 150 ms                                                 | 168 ms: 1.12x slower                                                      |
| dask                      | 338 ms                                                 | 384 ms: 1.14x slower                                                      |
| docutils                  | 2.58 sec                                               | 2.98 sec: 1.15x slower                                                    |
| django_template           | 34.4 ms                                                | 40.4 ms: 1.17x slower                                                     |
| pylint                    | 313 ms                                                 | 368 ms: 1.17x slower                                                      |
| async_generators          | 433 ms                                                 | 514 ms: 1.19x slower                                                      |
| nqueens                   | 80.6 ms                                                | 97.5 ms: 1.21x slower                                                     |
| genshi_text               | 22.9 ms                                                | 27.7 ms: 1.21x slower                                                     |
| coroutines                | 22.5 ms                                                | 27.6 ms: 1.23x slower                                                     |
| genshi_xml                | 50.3 ms                                                | 63.3 ms: 1.26x slower                                                     |
| sympy_integrate           | 19.9 ms                                                | 25.3 ms: 1.27x slower                                                     |
| generators                | 28.8 ms                                                | 56.1 ms: 1.95x slower                                                     |
| Geometric mean            | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed, regex_dna, mdp, bench_mp_pool, json_dumps, logging_silent, asyncio_websockets, async_tree_cpu_io_mixed_tg, comprehensions
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 69.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x