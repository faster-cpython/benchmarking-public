# Results vs. 3.13.0

- fork: brandtbucher
- ref: stitch_executors
- machine: linux-x86_64
- commit hash: ef0f4a5
- commit date: 2024-07-11
- overall geometric mean: 1.01x faster
- HPT reliability: 52.88%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 271 ms: 1.02x slower                                                    |
| docutils       | 2.58 sec                                               | 2.85 sec: 1.10x slower                                                  |
| html5lib       | 64.5 ms                                                | 63.0 ms: 1.02x faster                                                   |
| tornado_http   | 91.5 ms                                                | 92.5 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 376 ms: 1.24x faster                                                    |
| async_tree_none           | 354 ms                                                 | 323 ms: 1.10x faster                                                    |
| async_tree_memoization    | 442 ms                                                 | 406 ms: 1.09x faster                                                    |
| async_tree_none_tg        | 320 ms                                                 | 298 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 561 ms: 1.02x faster                                                    |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                    |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| async_tree_io_tg          | 825 ms                                                 | 845 ms: 1.02x slower                                                    |
| asyncio_tcp               | 488 ms                                                 | 504 ms: 1.03x slower                                                    |
| coroutines                | 22.5 ms                                                | 23.6 ms: 1.05x slower                                                   |
| async_generators          | 433 ms                                                 | 464 ms: 1.07x slower                                                    |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (2): async_tree_io, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.8 ms: 1.12x faster                                                   |
| nbody          | 85.7 ms                                                | 79.6 ms: 1.08x faster                                                   |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                  | 1.07x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.75 ms: 1.04x faster                                                   |
| regex_v8       | 25.3 ms                                                | 25.4 ms: 1.01x slower                                                   |
| regex_dna      | 220 ms                                                 | 228 ms: 1.04x slower                                                    |
| regex_compile  | 131 ms                                                 | 136 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                  |
| xml_etree_generate   | 87.0 ms                                                | 81.0 ms: 1.07x faster                                                   |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                    |
| xml_etree_process    | 60.4 ms                                                | 57.6 ms: 1.05x faster                                                   |
| xml_etree_iterparse  | 102 ms                                                 | 98.5 ms: 1.04x faster                                                   |
| pickle_pure_python   | 300 us                                                 | 295 us: 1.02x faster                                                    |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                   |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                    |
| json_loads           | 27.0 us                                                | 27.9 us: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                   |
| python_startup_no_site | 6.99 ms                                                | 7.10 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.84 ms: 1.13x faster                                                   |
| django_template | 34.4 ms                                                | 35.3 ms: 1.03x slower                                                   |
| genshi_text     | 22.9 ms                                                | 24.8 ms: 1.08x slower                                                   |
| genshi_xml      | 50.3 ms                                                | 58.1 ms: 1.15x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 28.2 us: 1.35x faster                                                   |
| deepcopy                  | 352 us                                                 | 278 us: 1.27x faster                                                    |
| async_tree_memoization_tg | 465 ms                                                 | 376 ms: 1.24x faster                                                    |
| scimark_fft               | 369 ms                                                 | 311 ms: 1.18x faster                                                    |
| deepcopy_reduce           | 3.17 us                                                | 2.72 us: 1.16x faster                                                   |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.36 ms: 1.15x faster                                                   |
| richards                  | 48.1 ms                                                | 42.6 ms: 1.13x faster                                                   |
| mako                      | 11.1 ms                                                | 9.84 ms: 1.13x faster                                                   |
| float                     | 78.5 ms                                                | 69.8 ms: 1.12x faster                                                   |
| richards_super            | 54.4 ms                                                | 48.7 ms: 1.12x faster                                                   |
| async_tree_none           | 354 ms                                                 | 323 ms: 1.10x faster                                                    |
| crypto_pyaes              | 73.0 ms                                                | 66.8 ms: 1.09x faster                                                   |
| async_tree_memoization    | 442 ms                                                 | 406 ms: 1.09x faster                                                    |
| tomli_loads               | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                  |
| spectral_norm             | 115 ms                                                 | 106 ms: 1.08x faster                                                    |
| nbody                     | 85.7 ms                                                | 79.6 ms: 1.08x faster                                                   |
| async_tree_none_tg        | 320 ms                                                 | 298 ms: 1.07x faster                                                    |
| scimark_monte_carlo       | 66.3 ms                                                | 61.7 ms: 1.07x faster                                                   |
| xml_etree_generate        | 87.0 ms                                                | 81.0 ms: 1.07x faster                                                   |
| mdp                       | 2.74 sec                                               | 2.56 sec: 1.07x faster                                                  |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                    |
| pathlib                   | 17.1 ms                                                | 16.3 ms: 1.05x faster                                                   |
| xml_etree_process         | 60.4 ms                                                | 57.6 ms: 1.05x faster                                                   |
| telco                     | 8.45 ms                                                | 8.06 ms: 1.05x faster                                                   |
| fannkuch                  | 381 ms                                                 | 363 ms: 1.05x faster                                                    |
| gc_traversal              | 3.81 ms                                                | 3.65 ms: 1.04x faster                                                   |
| pprint_safe_repr          | 744 ms                                                 | 717 ms: 1.04x faster                                                    |
| xml_etree_iterparse       | 102 ms                                                 | 98.5 ms: 1.04x faster                                                   |
| regex_effbot              | 3.88 ms                                                | 3.75 ms: 1.04x faster                                                   |
| logging_simple            | 5.66 us                                                | 5.48 us: 1.03x faster                                                   |
| pyflate                   | 460 ms                                                 | 447 ms: 1.03x faster                                                    |
| pprint_pformat            | 1.51 sec                                               | 1.47 sec: 1.03x faster                                                  |
| html5lib                  | 64.5 ms                                                | 63.0 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 561 ms: 1.02x faster                                                    |
| logging_format            | 6.25 us                                                | 6.11 us: 1.02x faster                                                   |
| pickle_pure_python        | 300 us                                                 | 295 us: 1.02x faster                                                    |
| pycparser                 | 1.19 sec                                               | 1.18 sec: 1.01x faster                                                  |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                   |
| pidigits                  | 186 ms                                                 | 185 ms: 1.00x faster                                                    |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                    |
| sqlglot_transpile         | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                   |
| regex_v8                  | 25.3 ms                                                | 25.4 ms: 1.01x slower                                                   |
| json_dumps                | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                   |
| meteor_contest            | 108 ms                                                 | 108 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| tornado_http              | 91.5 ms                                                | 92.5 ms: 1.01x slower                                                   |
| unpickle_pure_python      | 213 us                                                 | 216 us: 1.01x slower                                                    |
| python_startup_no_site    | 6.99 ms                                                | 7.10 ms: 1.02x slower                                                   |
| comprehensions            | 16.4 us                                                | 16.7 us: 1.02x slower                                                   |
| bench_thread_pool         | 815 us                                                 | 832 us: 1.02x slower                                                    |
| 2to3                      | 265 ms                                                 | 271 ms: 1.02x slower                                                    |
| async_tree_io_tg          | 825 ms                                                 | 845 ms: 1.02x slower                                                    |
| go                        | 142 ms                                                 | 145 ms: 1.02x slower                                                    |
| bpe_tokeniser             | 4.69 sec                                               | 4.81 sec: 1.03x slower                                                  |
| generators                | 28.8 ms                                                | 29.6 ms: 1.03x slower                                                   |
| sqlglot_normalize         | 107 ms                                                 | 110 ms: 1.03x slower                                                    |
| sqlglot_optimize          | 53.9 ms                                                | 55.4 ms: 1.03x slower                                                   |
| django_template           | 34.4 ms                                                | 35.3 ms: 1.03x slower                                                   |
| asyncio_tcp               | 488 ms                                                 | 504 ms: 1.03x slower                                                    |
| json_loads                | 27.0 us                                                | 27.9 us: 1.03x slower                                                   |
| raytrace                  | 262 ms                                                 | 271 ms: 1.03x slower                                                    |
| regex_dna                 | 220 ms                                                 | 228 ms: 1.04x slower                                                    |
| regex_compile             | 131 ms                                                 | 136 ms: 1.04x slower                                                    |
| logging_silent            | 102 ns                                                 | 106 ns: 1.04x slower                                                    |
| coroutines                | 22.5 ms                                                | 23.6 ms: 1.05x slower                                                   |
| typing_runtime_protocols  | 159 us                                                 | 168 us: 1.06x slower                                                    |
| nqueens                   | 80.6 ms                                                | 85.7 ms: 1.06x slower                                                   |
| hexiom                    | 6.13 ms                                                | 6.52 ms: 1.06x slower                                                   |
| dulwich_log               | 63.0 ms                                                | 67.4 ms: 1.07x slower                                                   |
| scimark_lu                | 115 ms                                                 | 123 ms: 1.07x slower                                                    |
| sympy_expand              | 462 ms                                                 | 495 ms: 1.07x slower                                                    |
| sympy_str                 | 274 ms                                                 | 293 ms: 1.07x slower                                                    |
| async_generators          | 433 ms                                                 | 464 ms: 1.07x slower                                                    |
| dask                      | 338 ms                                                 | 362 ms: 1.07x slower                                                    |
| pylint                    | 313 ms                                                 | 336 ms: 1.07x slower                                                    |
| scimark_sor               | 122 ms                                                 | 132 ms: 1.08x slower                                                    |
| genshi_text               | 22.9 ms                                                | 24.8 ms: 1.08x slower                                                   |
| create_gc_cycles          | 1.61 ms                                                | 1.76 ms: 1.09x slower                                                   |
| sympy_integrate           | 19.9 ms                                                | 21.9 ms: 1.10x slower                                                   |
| sympy_sum                 | 150 ms                                                 | 165 ms: 1.10x slower                                                    |
| docutils                  | 2.58 sec                                               | 2.85 sec: 1.10x slower                                                  |
| coverage                  | 83.7 ms                                                | 93.2 ms: 1.11x slower                                                   |
| deltablue                 | 3.15 ms                                                | 3.55 ms: 1.13x slower                                                   |
| genshi_xml                | 50.3 ms                                                | 58.1 ms: 1.15x slower                                                   |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (7): json, async_tree_io, async_tree_cpu_io_mixed_tg, thrift, chaos, sqlglot_parse, bench_mp_pool
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 52.88% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x