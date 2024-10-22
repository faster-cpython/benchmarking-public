# Results vs. 3.13.0

- fork: brandtbucher
- ref: faster_jit_builds
- machine: linux-x86_64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.01x faster
- HPT reliability: 54.79%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 272 ms: 1.03x slower                                                     |
| docutils       | 2.58 sec                                               | 2.91 sec: 1.13x slower                                                   |
| html5lib       | 64.5 ms                                                | 65.8 ms: 1.02x slower                                                    |
| tornado_http   | 91.5 ms                                                | 93.3 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                  | 1.05x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|---------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 394 ms: 1.18x faster                                                     |
| async_tree_none           | 354 ms                                                 | 328 ms: 1.08x faster                                                     |
| async_tree_memoization    | 442 ms                                                 | 416 ms: 1.06x faster                                                     |
| async_tree_none_tg        | 320 ms                                                 | 302 ms: 1.06x faster                                                     |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                   |
| asyncio_tcp               | 488 ms                                                 | 498 ms: 1.02x slower                                                     |
| coroutines                | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                    |
| async_generators          | 433 ms                                                 | 452 ms: 1.04x slower                                                     |
| async_tree_io_tg          | 825 ms                                                 | 874 ms: 1.06x slower                                                     |
| async_tree_io             | 843 ms                                                 | 904 ms: 1.07x slower                                                     |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.6 ms: 1.11x faster                                                    |
| nbody          | 85.7 ms                                                | 80.1 ms: 1.07x faster                                                    |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.82 ms: 1.02x faster                                                    |
| regex_v8       | 25.3 ms                                                | 25.8 ms: 1.02x slower                                                    |
| regex_compile  | 131 ms                                                 | 134 ms: 1.02x slower                                                     |
| regex_dna      | 220 ms                                                 | 229 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                   |
| xml_etree_generate   | 87.0 ms                                                | 81.3 ms: 1.07x faster                                                    |
| xml_etree_process    | 60.4 ms                                                | 56.8 ms: 1.06x faster                                                    |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                     |
| xml_etree_iterparse  | 102 ms                                                 | 100 ms: 1.02x faster                                                     |
| pickle_pure_python   | 300 us                                                 | 297 us: 1.01x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                     |
| json_loads           | 27.0 us                                                | 27.8 us: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                    |
| python_startup_no_site | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.82 ms: 1.13x faster                                                    |
| django_template | 34.4 ms                                                | 35.6 ms: 1.03x slower                                                    |
| genshi_text     | 22.9 ms                                                | 24.8 ms: 1.08x slower                                                    |
| genshi_xml      | 50.3 ms                                                | 58.4 ms: 1.16x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                             |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|---------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 28.3 us: 1.34x faster                                                    |
| deepcopy                  | 352 us                                                 | 273 us: 1.29x faster                                                     |
| richards                  | 48.1 ms                                                | 40.4 ms: 1.19x faster                                                    |
| async_tree_memoization_tg | 465 ms                                                 | 394 ms: 1.18x faster                                                     |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.30 ms: 1.17x faster                                                    |
| scimark_fft               | 369 ms                                                 | 316 ms: 1.17x faster                                                     |
| richards_super            | 54.4 ms                                                | 46.9 ms: 1.16x faster                                                    |
| spectral_norm             | 115 ms                                                 | 101 ms: 1.14x faster                                                     |
| mako                      | 11.1 ms                                                | 9.82 ms: 1.13x faster                                                    |
| deepcopy_reduce           | 3.17 us                                                | 2.81 us: 1.13x faster                                                    |
| float                     | 78.5 ms                                                | 70.6 ms: 1.11x faster                                                    |
| crypto_pyaes              | 73.0 ms                                                | 66.3 ms: 1.10x faster                                                    |
| tomli_loads               | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                   |
| async_tree_none           | 354 ms                                                 | 328 ms: 1.08x faster                                                     |
| telco                     | 8.45 ms                                                | 7.84 ms: 1.08x faster                                                    |
| pathlib                   | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                    |
| scimark_monte_carlo       | 66.3 ms                                                | 61.8 ms: 1.07x faster                                                    |
| nbody                     | 85.7 ms                                                | 80.1 ms: 1.07x faster                                                    |
| xml_etree_generate        | 87.0 ms                                                | 81.3 ms: 1.07x faster                                                    |
| async_tree_memoization    | 442 ms                                                 | 416 ms: 1.06x faster                                                     |
| xml_etree_process         | 60.4 ms                                                | 56.8 ms: 1.06x faster                                                    |
| async_tree_none_tg        | 320 ms                                                 | 302 ms: 1.06x faster                                                     |
| mdp                       | 2.74 sec                                               | 2.60 sec: 1.06x faster                                                   |
| xml_etree_parse           | 156 ms                                                 | 148 ms: 1.05x faster                                                     |
| pprint_safe_repr          | 744 ms                                                 | 707 ms: 1.05x faster                                                     |
| pyflate                   | 460 ms                                                 | 439 ms: 1.05x faster                                                     |
| bpe_tokeniser             | 4.69 sec                                               | 4.50 sec: 1.04x faster                                                   |
| fannkuch                  | 381 ms                                                 | 367 ms: 1.04x faster                                                     |
| logging_simple            | 5.66 us                                                | 5.46 us: 1.04x faster                                                    |
| logging_format            | 6.25 us                                                | 6.03 us: 1.04x faster                                                    |
| pprint_pformat            | 1.51 sec                                               | 1.46 sec: 1.04x faster                                                   |
| meteor_contest            | 108 ms                                                 | 105 ms: 1.02x faster                                                     |
| xml_etree_iterparse       | 102 ms                                                 | 100 ms: 1.02x faster                                                     |
| regex_effbot              | 3.88 ms                                                | 3.82 ms: 1.02x faster                                                    |
| pycparser                 | 1.19 sec                                               | 1.18 sec: 1.01x faster                                                   |
| pickle_pure_python        | 300 us                                                 | 297 us: 1.01x faster                                                     |
| gc_traversal              | 3.81 ms                                                | 3.78 ms: 1.01x faster                                                    |
| pidigits                  | 186 ms                                                 | 185 ms: 1.00x faster                                                     |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                    |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                   |
| comprehensions            | 16.4 us                                                | 16.5 us: 1.01x slower                                                    |
| sqlglot_parse             | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                    |
| unpickle_pure_python      | 213 us                                                 | 216 us: 1.01x slower                                                     |
| logging_silent            | 102 ns                                                 | 103 ns: 1.01x slower                                                     |
| bench_thread_pool         | 815 us                                                 | 826 us: 1.01x slower                                                     |
| sqlglot_transpile         | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                    |
| tornado_http              | 91.5 ms                                                | 93.3 ms: 1.02x slower                                                    |
| regex_v8                  | 25.3 ms                                                | 25.8 ms: 1.02x slower                                                    |
| html5lib                  | 64.5 ms                                                | 65.8 ms: 1.02x slower                                                    |
| asyncio_tcp               | 488 ms                                                 | 498 ms: 1.02x slower                                                     |
| regex_compile             | 131 ms                                                 | 134 ms: 1.02x slower                                                     |
| 2to3                      | 265 ms                                                 | 272 ms: 1.03x slower                                                     |
| python_startup_no_site    | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                    |
| json_loads                | 27.0 us                                                | 27.8 us: 1.03x slower                                                    |
| coroutines                | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                    |
| raytrace                  | 262 ms                                                 | 270 ms: 1.03x slower                                                     |
| django_template           | 34.4 ms                                                | 35.6 ms: 1.03x slower                                                    |
| sqlglot_optimize          | 53.9 ms                                                | 56.2 ms: 1.04x slower                                                    |
| regex_dna                 | 220 ms                                                 | 229 ms: 1.04x slower                                                     |
| async_generators          | 433 ms                                                 | 452 ms: 1.04x slower                                                     |
| go                        | 142 ms                                                 | 149 ms: 1.05x slower                                                     |
| async_tree_io_tg          | 825 ms                                                 | 874 ms: 1.06x slower                                                     |
| typing_runtime_protocols  | 159 us                                                 | 169 us: 1.06x slower                                                     |
| scimark_sor               | 122 ms                                                 | 130 ms: 1.06x slower                                                     |
| sqlglot_normalize         | 107 ms                                                 | 114 ms: 1.07x slower                                                     |
| nqueens                   | 80.6 ms                                                | 86.0 ms: 1.07x slower                                                    |
| async_tree_io             | 843 ms                                                 | 904 ms: 1.07x slower                                                     |
| hexiom                    | 6.13 ms                                                | 6.59 ms: 1.08x slower                                                    |
| sympy_str                 | 274 ms                                                 | 294 ms: 1.08x slower                                                     |
| dask                      | 338 ms                                                 | 365 ms: 1.08x slower                                                     |
| genshi_text               | 22.9 ms                                                | 24.8 ms: 1.08x slower                                                    |
| sympy_expand              | 462 ms                                                 | 501 ms: 1.09x slower                                                     |
| create_gc_cycles          | 1.61 ms                                                | 1.77 ms: 1.10x slower                                                    |
| coverage                  | 83.7 ms                                                | 93.0 ms: 1.11x slower                                                    |
| scimark_lu                | 115 ms                                                 | 128 ms: 1.12x slower                                                     |
| sympy_integrate           | 19.9 ms                                                | 22.3 ms: 1.12x slower                                                    |
| pylint                    | 313 ms                                                 | 351 ms: 1.12x slower                                                     |
| docutils                  | 2.58 sec                                               | 2.91 sec: 1.13x slower                                                   |
| sympy_sum                 | 150 ms                                                 | 169 ms: 1.13x slower                                                     |
| deltablue                 | 3.15 ms                                                | 3.65 ms: 1.16x slower                                                    |
| genshi_xml                | 50.3 ms                                                | 58.4 ms: 1.16x slower                                                    |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, json, generators, bench_mp_pool, chaos, json_dumps, asyncio_websockets, thrift
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 54.79% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x