# Results vs. 3.13.0

- fork: python
- ref: b5e142ba7c2063efe9bb
- machine: linux-x86_64
- commit hash: b5e142b
- commit date: 2024-08-06
- overall geometric mean: 1.01x faster
- HPT reliability: 75.21%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 275 ms: 1.04x slower                                                  |
| docutils       | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                |
| html5lib       | 64.5 ms                                                | 63.8 ms: 1.01x faster                                                 |
| tornado_http   | 91.5 ms                                                | 92.6 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 394 ms: 1.18x faster                                                  |
| async_tree_none            | 354 ms                                                 | 327 ms: 1.08x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 422 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 536 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                 |
| asyncio_tcp                | 488 ms                                                 | 498 ms: 1.02x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 864 ms: 1.05x slower                                                  |
| async_generators           | 433 ms                                                 | 453 ms: 1.05x slower                                                  |
| async_tree_io              | 843 ms                                                 | 910 ms: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.5 ms: 1.11x faster                                                 |
| nbody          | 85.7 ms                                                | 79.1 ms: 1.08x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 24.4 ms: 1.04x faster                                                 |
| regex_effbot   | 3.88 ms                                                | 3.83 ms: 1.02x faster                                                 |
| regex_dna      | 220 ms                                                 | 223 ms: 1.01x slower                                                  |
| regex_compile  | 131 ms                                                 | 135 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.91 sec: 1.10x faster                                                |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| xml_etree_generate   | 87.0 ms                                                | 81.6 ms: 1.07x faster                                                 |
| xml_etree_process    | 60.4 ms                                                | 57.2 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 102 ms                                                 | 99.2 ms: 1.03x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                  |
| json_loads           | 27.0 us                                                | 27.7 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.85 ms: 1.13x faster                                                 |
| django_template | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 53.4 ms: 1.06x slower                                                 |
| genshi_text     | 22.9 ms                                                | 24.5 ms: 1.07x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 29.1 us: 1.31x faster                                                 |
| deepcopy                   | 352 us                                                 | 273 us: 1.29x faster                                                  |
| scimark_fft                | 369 ms                                                 | 307 ms: 1.20x faster                                                  |
| async_tree_memoization_tg  | 465 ms                                                 | 394 ms: 1.18x faster                                                  |
| richards                   | 48.1 ms                                                | 41.2 ms: 1.17x faster                                                 |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.15x faster                                                  |
| richards_super             | 54.4 ms                                                | 47.5 ms: 1.14x faster                                                 |
| deepcopy_reduce            | 3.17 us                                                | 2.78 us: 1.14x faster                                                 |
| mako                       | 11.1 ms                                                | 9.85 ms: 1.13x faster                                                 |
| float                      | 78.5 ms                                                | 70.5 ms: 1.11x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.55 ms: 1.10x faster                                                 |
| tomli_loads                | 2.11 sec                                               | 1.91 sec: 1.10x faster                                                |
| scimark_monte_carlo        | 66.3 ms                                                | 60.7 ms: 1.09x faster                                                 |
| crypto_pyaes               | 73.0 ms                                                | 66.8 ms: 1.09x faster                                                 |
| nbody                      | 85.7 ms                                                | 79.1 ms: 1.08x faster                                                 |
| async_tree_none            | 354 ms                                                 | 327 ms: 1.08x faster                                                  |
| mdp                        | 2.74 sec                                               | 2.56 sec: 1.07x faster                                                |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| xml_etree_generate         | 87.0 ms                                                | 81.6 ms: 1.07x faster                                                 |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                                  |
| pyflate                    | 460 ms                                                 | 432 ms: 1.06x faster                                                  |
| telco                      | 8.45 ms                                                | 7.97 ms: 1.06x faster                                                 |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                 |
| scimark_lu                 | 115 ms                                                 | 109 ms: 1.06x faster                                                  |
| xml_etree_process          | 60.4 ms                                                | 57.2 ms: 1.06x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 422 ms: 1.05x faster                                                  |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.05x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.52 sec: 1.04x faster                                                |
| regex_v8                   | 25.3 ms                                                | 24.4 ms: 1.04x faster                                                 |
| pprint_safe_repr           | 744 ms                                                 | 722 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 102 ms                                                 | 99.2 ms: 1.03x faster                                                 |
| fannkuch                   | 381 ms                                                 | 371 ms: 1.03x faster                                                  |
| json                       | 5.20 ms                                                | 5.09 ms: 1.02x faster                                                 |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.02x faster                                                  |
| logging_simple             | 5.66 us                                                | 5.57 us: 1.02x faster                                                 |
| regex_effbot               | 3.88 ms                                                | 3.83 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 536 ms: 1.01x faster                                                  |
| pprint_pformat             | 1.51 sec                                               | 1.49 sec: 1.01x faster                                                |
| logging_format             | 6.25 us                                                | 6.17 us: 1.01x faster                                                 |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| comprehensions             | 16.4 us                                                | 16.2 us: 1.01x faster                                                 |
| html5lib                   | 64.5 ms                                                | 63.8 ms: 1.01x faster                                                 |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| bench_thread_pool          | 815 us                                                 | 822 us: 1.01x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| tornado_http               | 91.5 ms                                                | 92.6 ms: 1.01x slower                                                 |
| gc_traversal               | 3.81 ms                                                | 3.85 ms: 1.01x slower                                                 |
| regex_dna                  | 220 ms                                                 | 223 ms: 1.01x slower                                                  |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                 |
| asyncio_tcp                | 488 ms                                                 | 498 ms: 1.02x slower                                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                 |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                  |
| python_startup_no_site     | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                 |
| json_loads                 | 27.0 us                                                | 27.7 us: 1.03x slower                                                 |
| regex_compile              | 131 ms                                                 | 135 ms: 1.03x slower                                                  |
| raytrace                   | 262 ms                                                 | 269 ms: 1.03x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.62 ms: 1.03x slower                                                 |
| go                         | 142 ms                                                 | 146 ms: 1.03x slower                                                  |
| sqlglot_optimize           | 53.9 ms                                                | 55.9 ms: 1.04x slower                                                 |
| 2to3                       | 265 ms                                                 | 275 ms: 1.04x slower                                                  |
| nqueens                    | 80.6 ms                                                | 84.0 ms: 1.04x slower                                                 |
| async_tree_io_tg           | 825 ms                                                 | 864 ms: 1.05x slower                                                  |
| django_template            | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                 |
| async_generators           | 433 ms                                                 | 453 ms: 1.05x slower                                                  |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.05x slower                                                  |
| genshi_xml                 | 50.3 ms                                                | 53.4 ms: 1.06x slower                                                 |
| genshi_text                | 22.9 ms                                                | 24.5 ms: 1.07x slower                                                 |
| typing_runtime_protocols   | 159 us                                                 | 171 us: 1.07x slower                                                  |
| async_tree_io              | 843 ms                                                 | 910 ms: 1.08x slower                                                  |
| sympy_str                  | 274 ms                                                 | 298 ms: 1.09x slower                                                  |
| hexiom                     | 6.13 ms                                                | 6.71 ms: 1.10x slower                                                 |
| coverage                   | 83.7 ms                                                | 91.8 ms: 1.10x slower                                                 |
| sympy_expand               | 462 ms                                                 | 508 ms: 1.10x slower                                                  |
| create_gc_cycles           | 1.61 ms                                                | 1.78 ms: 1.11x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                |
| sympy_integrate            | 19.9 ms                                                | 22.6 ms: 1.14x slower                                                 |
| pylint                     | 313 ms                                                 | 356 ms: 1.14x slower                                                  |
| deltablue                  | 3.15 ms                                                | 3.58 ms: 1.14x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 170 ms: 1.14x slower                                                  |
| generators                 | 28.8 ms                                                | 32.9 ms: 1.14x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, pycparser, chaos, asyncio_websockets, pickle_pure_python, python_startup, bench_mp_pool, thrift
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 75.21% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x