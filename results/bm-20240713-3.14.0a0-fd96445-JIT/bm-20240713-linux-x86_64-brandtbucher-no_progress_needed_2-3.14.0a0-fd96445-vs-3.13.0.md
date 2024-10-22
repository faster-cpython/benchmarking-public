# Results vs. 3.13.0

- fork: brandtbucher
- ref: no_progress_needed_2
- machine: linux-x86_64
- commit hash: fd96445
- commit date: 2024-07-13
- overall geometric mean: 1.01x faster
- HPT reliability: 73.24%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 276 ms: 1.04x slower                                                        |
| docutils       | 2.58 sec                                               | 2.88 sec: 1.11x slower                                                      |
| html5lib       | 64.5 ms                                                | 65.1 ms: 1.01x slower                                                       |
| tornado_http   | 91.5 ms                                                | 93.2 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 382 ms: 1.22x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 412 ms: 1.07x faster                                                        |
| async_tree_none           | 354 ms                                                 | 330 ms: 1.07x faster                                                        |
| async_tree_none_tg        | 320 ms                                                 | 306 ms: 1.04x faster                                                        |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                        |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                      |
| asyncio_tcp               | 488 ms                                                 | 505 ms: 1.03x slower                                                        |
| async_tree_io_tg          | 825 ms                                                 | 855 ms: 1.04x slower                                                        |
| coroutines                | 22.5 ms                                                | 23.5 ms: 1.04x slower                                                       |
| async_generators          | 433 ms                                                 | 456 ms: 1.05x slower                                                        |
| async_tree_io             | 843 ms                                                 | 893 ms: 1.06x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.8 ms: 1.11x faster                                                       |
| nbody          | 85.7 ms                                                | 79.4 ms: 1.08x faster                                                       |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.77 ms: 1.03x faster                                                       |
| regex_dna      | 220 ms                                                 | 222 ms: 1.01x slower                                                        |
| regex_v8       | 25.3 ms                                                | 25.5 ms: 1.01x slower                                                       |
| regex_compile  | 131 ms                                                 | 137 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.91 sec: 1.11x faster                                                      |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                        |
| xml_etree_generate   | 87.0 ms                                                | 83.1 ms: 1.05x faster                                                       |
| xml_etree_process    | 60.4 ms                                                | 58.5 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 102 ms                                                 | 99.5 ms: 1.03x faster                                                       |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                        |
| pickle_pure_python   | 300 us                                                 | 304 us: 1.01x slower                                                        |
| json_loads           | 27.0 us                                                | 28.3 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.15 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.60 ms: 1.16x faster                                                       |
| django_template | 34.4 ms                                                | 35.8 ms: 1.04x slower                                                       |
| genshi_text     | 22.9 ms                                                | 25.4 ms: 1.11x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 57.0 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 27.3 us: 1.39x faster                                                       |
| deepcopy                  | 352 us                                                 | 276 us: 1.28x faster                                                        |
| richards                  | 48.1 ms                                                | 37.7 ms: 1.28x faster                                                       |
| richards_super            | 54.4 ms                                                | 43.9 ms: 1.24x faster                                                       |
| async_tree_memoization_tg | 465 ms                                                 | 382 ms: 1.22x faster                                                        |
| scimark_fft               | 369 ms                                                 | 310 ms: 1.19x faster                                                        |
| mako                      | 11.1 ms                                                | 9.60 ms: 1.16x faster                                                       |
| deepcopy_reduce           | 3.17 us                                                | 2.76 us: 1.15x faster                                                       |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.45 ms: 1.13x faster                                                       |
| spectral_norm             | 115 ms                                                 | 103 ms: 1.11x faster                                                        |
| float                     | 78.5 ms                                                | 70.8 ms: 1.11x faster                                                       |
| tomli_loads               | 2.11 sec                                               | 1.91 sec: 1.11x faster                                                      |
| scimark_monte_carlo       | 66.3 ms                                                | 60.5 ms: 1.10x faster                                                       |
| nbody                     | 85.7 ms                                                | 79.4 ms: 1.08x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 412 ms: 1.07x faster                                                        |
| async_tree_none           | 354 ms                                                 | 330 ms: 1.07x faster                                                        |
| mdp                       | 2.74 sec                                               | 2.56 sec: 1.07x faster                                                      |
| crypto_pyaes              | 73.0 ms                                                | 68.1 ms: 1.07x faster                                                       |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                        |
| pathlib                   | 17.1 ms                                                | 16.0 ms: 1.06x faster                                                       |
| telco                     | 8.45 ms                                                | 7.97 ms: 1.06x faster                                                       |
| pyflate                   | 460 ms                                                 | 433 ms: 1.06x faster                                                        |
| fannkuch                  | 381 ms                                                 | 360 ms: 1.06x faster                                                        |
| xml_etree_generate        | 87.0 ms                                                | 83.1 ms: 1.05x faster                                                       |
| async_tree_none_tg        | 320 ms                                                 | 306 ms: 1.04x faster                                                        |
| gc_traversal              | 3.81 ms                                                | 3.65 ms: 1.04x faster                                                       |
| xml_etree_process         | 60.4 ms                                                | 58.5 ms: 1.03x faster                                                       |
| regex_effbot              | 3.88 ms                                                | 3.77 ms: 1.03x faster                                                       |
| logging_format            | 6.25 us                                                | 6.08 us: 1.03x faster                                                       |
| logging_simple            | 5.66 us                                                | 5.52 us: 1.03x faster                                                       |
| xml_etree_iterparse       | 102 ms                                                 | 99.5 ms: 1.03x faster                                                       |
| chaos                     | 58.4 ms                                                | 57.3 ms: 1.02x faster                                                       |
| pprint_safe_repr          | 744 ms                                                 | 733 ms: 1.02x faster                                                        |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.01x faster                                                        |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                       |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x slower                                                        |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                        |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                      |
| unpickle_pure_python      | 213 us                                                 | 215 us: 1.01x slower                                                        |
| html5lib                  | 64.5 ms                                                | 65.1 ms: 1.01x slower                                                       |
| regex_dna                 | 220 ms                                                 | 222 ms: 1.01x slower                                                        |
| thrift                    | 796 us                                                 | 805 us: 1.01x slower                                                        |
| regex_v8                  | 25.3 ms                                                | 25.5 ms: 1.01x slower                                                       |
| pickle_pure_python        | 300 us                                                 | 304 us: 1.01x slower                                                        |
| logging_silent            | 102 ns                                                 | 103 ns: 1.01x slower                                                        |
| bpe_tokeniser             | 4.69 sec                                               | 4.77 sec: 1.02x slower                                                      |
| bench_thread_pool         | 815 us                                                 | 828 us: 1.02x slower                                                        |
| tornado_http              | 91.5 ms                                                | 93.2 ms: 1.02x slower                                                       |
| sqlglot_transpile         | 1.57 ms                                                | 1.61 ms: 1.02x slower                                                       |
| comprehensions            | 16.4 us                                                | 16.8 us: 1.02x slower                                                       |
| raytrace                  | 262 ms                                                 | 268 ms: 1.02x slower                                                        |
| python_startup_no_site    | 6.99 ms                                                | 7.15 ms: 1.02x slower                                                       |
| go                        | 142 ms                                                 | 145 ms: 1.03x slower                                                        |
| generators                | 28.8 ms                                                | 29.7 ms: 1.03x slower                                                       |
| sqlglot_optimize          | 53.9 ms                                                | 55.6 ms: 1.03x slower                                                       |
| asyncio_tcp               | 488 ms                                                 | 505 ms: 1.03x slower                                                        |
| async_tree_io_tg          | 825 ms                                                 | 855 ms: 1.04x slower                                                        |
| sqlglot_normalize         | 107 ms                                                 | 111 ms: 1.04x slower                                                        |
| django_template           | 34.4 ms                                                | 35.8 ms: 1.04x slower                                                       |
| 2to3                      | 265 ms                                                 | 276 ms: 1.04x slower                                                        |
| coroutines                | 22.5 ms                                                | 23.5 ms: 1.04x slower                                                       |
| regex_compile             | 131 ms                                                 | 137 ms: 1.05x slower                                                        |
| json_loads                | 27.0 us                                                | 28.3 us: 1.05x slower                                                       |
| dulwich_log               | 63.0 ms                                                | 66.1 ms: 1.05x slower                                                       |
| async_generators          | 433 ms                                                 | 456 ms: 1.05x slower                                                        |
| typing_runtime_protocols  | 159 us                                                 | 168 us: 1.06x slower                                                        |
| async_tree_io             | 843 ms                                                 | 893 ms: 1.06x slower                                                        |
| sympy_str                 | 274 ms                                                 | 291 ms: 1.06x slower                                                        |
| dask                      | 338 ms                                                 | 362 ms: 1.07x slower                                                        |
| nqueens                   | 80.6 ms                                                | 86.7 ms: 1.08x slower                                                       |
| sympy_expand              | 462 ms                                                 | 497 ms: 1.08x slower                                                        |
| scimark_sor               | 122 ms                                                 | 132 ms: 1.08x slower                                                        |
| deltablue                 | 3.15 ms                                                | 3.42 ms: 1.09x slower                                                       |
| pylint                    | 313 ms                                                 | 340 ms: 1.09x slower                                                        |
| hexiom                    | 6.13 ms                                                | 6.69 ms: 1.09x slower                                                       |
| scimark_lu                | 115 ms                                                 | 126 ms: 1.09x slower                                                        |
| create_gc_cycles          | 1.61 ms                                                | 1.76 ms: 1.10x slower                                                       |
| coverage                  | 83.7 ms                                                | 92.2 ms: 1.10x slower                                                       |
| sympy_integrate           | 19.9 ms                                                | 21.9 ms: 1.10x slower                                                       |
| genshi_text               | 22.9 ms                                                | 25.4 ms: 1.11x slower                                                       |
| docutils                  | 2.58 sec                                               | 2.88 sec: 1.11x slower                                                      |
| sympy_sum                 | 150 ms                                                 | 167 ms: 1.11x slower                                                        |
| genshi_xml                | 50.3 ms                                                | 57.0 ms: 1.13x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, pycparser, json, async_tree_cpu_io_mixed_tg, pprint_pformat, bench_mp_pool, sqlglot_parse, json_dumps
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 73.24% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x