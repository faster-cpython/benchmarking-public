# Results vs. 3.13.0

- fork: brandtbucher
- ref: invalidate_side_exit
- machine: linux-x86_64
- commit hash: eb895df
- commit date: 2024-07-16
- overall geometric mean: 1.01x faster
- HPT reliability: 50.09%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 271 ms: 1.02x slower                                                        |
| docutils       | 2.58 sec                                               | 2.86 sec: 1.11x slower                                                      |
| html5lib       | 64.5 ms                                                | 65.5 ms: 1.02x slower                                                       |
| tornado_http   | 91.5 ms                                                | 93.0 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 380 ms: 1.22x faster                                                        |
| async_tree_none           | 354 ms                                                 | 328 ms: 1.08x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 412 ms: 1.07x faster                                                        |
| async_tree_none_tg        | 320 ms                                                 | 302 ms: 1.06x faster                                                        |
| coroutines                | 22.5 ms                                                | 22.3 ms: 1.01x faster                                                       |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                        |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 849 ms: 1.03x slower                                                        |
| asyncio_tcp               | 488 ms                                                 | 504 ms: 1.03x slower                                                        |
| async_tree_io             | 843 ms                                                 | 886 ms: 1.05x slower                                                        |
| async_generators          | 433 ms                                                 | 455 ms: 1.05x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                                |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.0 ms: 1.12x faster                                                       |
| nbody          | 85.7 ms                                                | 80.2 ms: 1.07x faster                                                       |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.71 ms: 1.05x faster                                                       |
| regex_v8       | 25.3 ms                                                | 24.9 ms: 1.02x faster                                                       |
| regex_compile  | 131 ms                                                 | 135 ms: 1.03x slower                                                        |
| regex_dna      | 220 ms                                                 | 229 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.95 sec: 1.08x faster                                                      |
| xml_etree_generate   | 87.0 ms                                                | 81.2 ms: 1.07x faster                                                       |
| xml_etree_process    | 60.4 ms                                                | 57.3 ms: 1.05x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                        |
| xml_etree_iterparse  | 102 ms                                                 | 99.0 ms: 1.03x faster                                                       |
| pickle_pure_python   | 300 us                                                 | 297 us: 1.01x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                        |
| json_loads           | 27.0 us                                                | 27.3 us: 1.01x slower                                                       |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.18 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.71 ms: 1.14x faster                                                       |
| django_template | 34.4 ms                                                | 35.9 ms: 1.04x slower                                                       |
| genshi_text     | 22.9 ms                                                | 25.2 ms: 1.10x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 56.7 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240716-linux-x86_64-brandtbucher-invalidate_side_exit-3.14.0a0-eb895df |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 28.8 us: 1.32x faster                                                       |
| deepcopy                  | 352 us                                                 | 272 us: 1.29x faster                                                        |
| async_tree_memoization_tg | 465 ms                                                 | 380 ms: 1.22x faster                                                        |
| richards                  | 48.1 ms                                                | 40.6 ms: 1.19x faster                                                       |
| scimark_fft               | 369 ms                                                 | 314 ms: 1.18x faster                                                        |
| richards_super            | 54.4 ms                                                | 46.5 ms: 1.17x faster                                                       |
| mako                      | 11.1 ms                                                | 9.71 ms: 1.14x faster                                                       |
| deepcopy_reduce           | 3.17 us                                                | 2.79 us: 1.14x faster                                                       |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.44 ms: 1.13x faster                                                       |
| spectral_norm             | 115 ms                                                 | 102 ms: 1.13x faster                                                        |
| float                     | 78.5 ms                                                | 70.0 ms: 1.12x faster                                                       |
| scimark_monte_carlo       | 66.3 ms                                                | 60.9 ms: 1.09x faster                                                       |
| crypto_pyaes              | 73.0 ms                                                | 67.4 ms: 1.08x faster                                                       |
| pycparser                 | 1.19 sec                                               | 1.10 sec: 1.08x faster                                                      |
| tomli_loads               | 2.11 sec                                               | 1.95 sec: 1.08x faster                                                      |
| async_tree_none           | 354 ms                                                 | 328 ms: 1.08x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 412 ms: 1.07x faster                                                        |
| xml_etree_generate        | 87.0 ms                                                | 81.2 ms: 1.07x faster                                                       |
| nbody                     | 85.7 ms                                                | 80.2 ms: 1.07x faster                                                       |
| pyflate                   | 460 ms                                                 | 432 ms: 1.06x faster                                                        |
| telco                     | 8.45 ms                                                | 7.96 ms: 1.06x faster                                                       |
| pathlib                   | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                       |
| async_tree_none_tg        | 320 ms                                                 | 302 ms: 1.06x faster                                                        |
| xml_etree_process         | 60.4 ms                                                | 57.3 ms: 1.05x faster                                                       |
| xml_etree_parse           | 156 ms                                                 | 148 ms: 1.05x faster                                                        |
| fannkuch                  | 381 ms                                                 | 363 ms: 1.05x faster                                                        |
| regex_effbot              | 3.88 ms                                                | 3.71 ms: 1.05x faster                                                       |
| pprint_safe_repr          | 744 ms                                                 | 719 ms: 1.03x faster                                                        |
| pprint_pformat            | 1.51 sec                                               | 1.46 sec: 1.03x faster                                                      |
| xml_etree_iterparse       | 102 ms                                                 | 99.0 ms: 1.03x faster                                                       |
| mdp                       | 2.74 sec                                               | 2.68 sec: 1.02x faster                                                      |
| gc_traversal              | 3.81 ms                                                | 3.74 ms: 1.02x faster                                                       |
| regex_v8                  | 25.3 ms                                                | 24.9 ms: 1.02x faster                                                       |
| logging_format            | 6.25 us                                                | 6.17 us: 1.01x faster                                                       |
| pickle_pure_python        | 300 us                                                 | 297 us: 1.01x faster                                                        |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.01x faster                                                        |
| coroutines                | 22.5 ms                                                | 22.3 ms: 1.01x faster                                                       |
| logging_simple            | 5.66 us                                                | 5.62 us: 1.01x faster                                                       |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                       |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                        |
| comprehensions            | 16.4 us                                                | 16.5 us: 1.01x slower                                                       |
| unpickle_pure_python      | 213 us                                                 | 216 us: 1.01x slower                                                        |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| sqlglot_transpile         | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                       |
| bpe_tokeniser             | 4.69 sec                                               | 4.75 sec: 1.01x slower                                                      |
| json_loads                | 27.0 us                                                | 27.3 us: 1.01x slower                                                       |
| html5lib                  | 64.5 ms                                                | 65.5 ms: 1.02x slower                                                       |
| go                        | 142 ms                                                 | 144 ms: 1.02x slower                                                        |
| tornado_http              | 91.5 ms                                                | 93.0 ms: 1.02x slower                                                       |
| json_dumps                | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                       |
| 2to3                      | 265 ms                                                 | 271 ms: 1.02x slower                                                        |
| generators                | 28.8 ms                                                | 29.5 ms: 1.02x slower                                                       |
| bench_thread_pool         | 815 us                                                 | 833 us: 1.02x slower                                                        |
| python_startup_no_site    | 6.99 ms                                                | 7.18 ms: 1.03x slower                                                       |
| async_tree_io_tg          | 825 ms                                                 | 849 ms: 1.03x slower                                                        |
| sqlglot_optimize          | 53.9 ms                                                | 55.5 ms: 1.03x slower                                                       |
| regex_compile             | 131 ms                                                 | 135 ms: 1.03x slower                                                        |
| raytrace                  | 262 ms                                                 | 270 ms: 1.03x slower                                                        |
| asyncio_tcp               | 488 ms                                                 | 504 ms: 1.03x slower                                                        |
| logging_silent            | 102 ns                                                 | 106 ns: 1.04x slower                                                        |
| sqlglot_normalize         | 107 ms                                                 | 112 ms: 1.04x slower                                                        |
| django_template           | 34.4 ms                                                | 35.9 ms: 1.04x slower                                                       |
| regex_dna                 | 220 ms                                                 | 229 ms: 1.04x slower                                                        |
| async_tree_io             | 843 ms                                                 | 886 ms: 1.05x slower                                                        |
| async_generators          | 433 ms                                                 | 455 ms: 1.05x slower                                                        |
| scimark_sor               | 122 ms                                                 | 129 ms: 1.05x slower                                                        |
| nqueens                   | 80.6 ms                                                | 85.1 ms: 1.06x slower                                                       |
| sympy_str                 | 274 ms                                                 | 291 ms: 1.06x slower                                                        |
| typing_runtime_protocols  | 159 us                                                 | 170 us: 1.07x slower                                                        |
| pylint                    | 313 ms                                                 | 334 ms: 1.07x slower                                                        |
| hexiom                    | 6.13 ms                                                | 6.54 ms: 1.07x slower                                                       |
| sympy_expand              | 462 ms                                                 | 494 ms: 1.07x slower                                                        |
| scimark_lu                | 115 ms                                                 | 123 ms: 1.07x slower                                                        |
| dask                      | 338 ms                                                 | 362 ms: 1.07x slower                                                        |
| dulwich_log               | 63.0 ms                                                | 67.6 ms: 1.07x slower                                                       |
| sympy_integrate           | 19.9 ms                                                | 21.7 ms: 1.09x slower                                                       |
| create_gc_cycles          | 1.61 ms                                                | 1.76 ms: 1.10x slower                                                       |
| genshi_text               | 22.9 ms                                                | 25.2 ms: 1.10x slower                                                       |
| sympy_sum                 | 150 ms                                                 | 165 ms: 1.10x slower                                                        |
| deltablue                 | 3.15 ms                                                | 3.48 ms: 1.11x slower                                                       |
| docutils                  | 2.58 sec                                               | 2.86 sec: 1.11x slower                                                      |
| coverage                  | 83.7 ms                                                | 93.8 ms: 1.12x slower                                                       |
| genshi_xml                | 50.3 ms                                                | 56.7 ms: 1.13x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, chaos, json, bench_mp_pool, thrift, sqlglot_parse, async_tree_cpu_io_mixed_tg
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 50.09% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x