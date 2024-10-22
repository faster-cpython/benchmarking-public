# Results vs. 3.13.0

- fork: brandtbucher
- ref: cache_dynamic_exits
- machine: linux-x86_64
- commit hash: 55bff1c
- commit date: 2024-08-28
- overall geometric mean: 1.01x faster
- HPT reliability: 77.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 274 ms: 1.03x slower                                                       |
| docutils       | 2.58 sec                                               | 3.05 sec: 1.18x slower                                                     |
| html5lib       | 64.5 ms                                                | 66.8 ms: 1.04x slower                                                      |
| tornado_http   | 91.5 ms                                                | 94.3 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.07x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 403 ms: 1.15x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 398 ms: 1.11x faster                                                       |
| async_tree_none           | 354 ms                                                 | 322 ms: 1.10x faster                                                       |
| async_tree_none_tg        | 320 ms                                                 | 307 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 561 ms: 1.02x faster                                                       |
| asyncio_tcp               | 488 ms                                                 | 491 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                     |
| async_generators          | 433 ms                                                 | 461 ms: 1.06x slower                                                       |
| async_tree_io_tg          | 825 ms                                                 | 897 ms: 1.09x slower                                                       |
| async_tree_io             | 843 ms                                                 | 933 ms: 1.11x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.5 ms: 1.11x faster                                                      |
| nbody          | 85.7 ms                                                | 79.7 ms: 1.08x faster                                                      |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.56 ms: 1.09x faster                                                      |
| regex_v8       | 25.3 ms                                                | 24.4 ms: 1.04x faster                                                      |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                                       |
| regex_compile  | 131 ms                                                 | 143 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 76.6 ms: 1.14x faster                                                      |
| xml_etree_process    | 60.4 ms                                                | 54.2 ms: 1.11x faster                                                      |
| tomli_loads          | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                     |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                       |
| json_dumps           | 10.4 ms                                                | 9.99 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 102 ms                                                 | 98.3 ms: 1.04x faster                                                      |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                       |
| pickle_pure_python   | 300 us                                                 | 305 us: 1.02x slower                                                       |
| json_loads           | 27.0 us                                                | 28.6 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                      |
| python_startup_no_site | 6.99 ms                                                | 7.14 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.87 ms: 1.13x faster                                                      |
| genshi_text     | 22.9 ms                                                | 23.8 ms: 1.04x slower                                                      |
| django_template | 34.4 ms                                                | 37.7 ms: 1.09x slower                                                      |
| genshi_xml      | 50.3 ms                                                | 56.4 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 27.1 us: 1.40x faster                                                      |
| deepcopy                  | 352 us                                                 | 269 us: 1.31x faster                                                       |
| richards                  | 48.1 ms                                                | 39.6 ms: 1.21x faster                                                      |
| richards_super            | 54.4 ms                                                | 45.4 ms: 1.20x faster                                                      |
| scimark_fft               | 369 ms                                                 | 311 ms: 1.18x faster                                                       |
| deepcopy_reduce           | 3.17 us                                                | 2.69 us: 1.18x faster                                                      |
| async_tree_memoization_tg | 465 ms                                                 | 403 ms: 1.15x faster                                                       |
| xml_etree_generate        | 87.0 ms                                                | 76.6 ms: 1.14x faster                                                      |
| spectral_norm             | 115 ms                                                 | 101 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.44 ms: 1.13x faster                                                      |
| mako                      | 11.1 ms                                                | 9.87 ms: 1.13x faster                                                      |
| xml_etree_process         | 60.4 ms                                                | 54.2 ms: 1.11x faster                                                      |
| float                     | 78.5 ms                                                | 70.5 ms: 1.11x faster                                                      |
| async_tree_memoization    | 442 ms                                                 | 398 ms: 1.11x faster                                                       |
| crypto_pyaes              | 73.0 ms                                                | 65.9 ms: 1.11x faster                                                      |
| async_tree_none           | 354 ms                                                 | 322 ms: 1.10x faster                                                       |
| regex_effbot              | 3.88 ms                                                | 3.56 ms: 1.09x faster                                                      |
| telco                     | 8.45 ms                                                | 7.75 ms: 1.09x faster                                                      |
| tomli_loads               | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                     |
| mdp                       | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                     |
| pathlib                   | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                      |
| nbody                     | 85.7 ms                                                | 79.7 ms: 1.08x faster                                                      |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                       |
| bpe_tokeniser             | 4.69 sec                                               | 4.43 sec: 1.06x faster                                                     |
| scimark_monte_carlo       | 66.3 ms                                                | 62.6 ms: 1.06x faster                                                      |
| async_tree_none_tg        | 320 ms                                                 | 307 ms: 1.04x faster                                                       |
| json_dumps                | 10.4 ms                                                | 9.99 ms: 1.04x faster                                                      |
| xml_etree_iterparse       | 102 ms                                                 | 98.3 ms: 1.04x faster                                                      |
| regex_v8                  | 25.3 ms                                                | 24.4 ms: 1.04x faster                                                      |
| pyflate                   | 460 ms                                                 | 445 ms: 1.03x faster                                                       |
| logging_format            | 6.25 us                                                | 6.06 us: 1.03x faster                                                      |
| logging_simple            | 5.66 us                                                | 5.49 us: 1.03x faster                                                      |
| fannkuch                  | 381 ms                                                 | 370 ms: 1.03x faster                                                       |
| pprint_safe_repr          | 744 ms                                                 | 726 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 561 ms: 1.02x faster                                                       |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.02x faster                                                       |
| pycparser                 | 1.19 sec                                               | 1.18 sec: 1.02x faster                                                     |
| gc_traversal              | 3.81 ms                                                | 3.75 ms: 1.02x faster                                                      |
| regex_dna                 | 220 ms                                                 | 217 ms: 1.01x faster                                                       |
| thrift                    | 796 us                                                 | 788 us: 1.01x faster                                                       |
| scimark_lu                | 115 ms                                                 | 114 ms: 1.01x faster                                                       |
| pprint_pformat            | 1.51 sec                                               | 1.50 sec: 1.01x faster                                                     |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                      |
| pidigits                  | 186 ms                                                 | 185 ms: 1.00x faster                                                       |
| bench_thread_pool         | 815 us                                                 | 820 us: 1.01x slower                                                       |
| asyncio_tcp               | 488 ms                                                 | 491 ms: 1.01x slower                                                       |
| unpickle_pure_python      | 213 us                                                 | 215 us: 1.01x slower                                                       |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                     |
| logging_silent            | 102 ns                                                 | 103 ns: 1.01x slower                                                       |
| pickle_pure_python        | 300 us                                                 | 305 us: 1.02x slower                                                       |
| deltablue                 | 3.15 ms                                                | 3.20 ms: 1.02x slower                                                      |
| comprehensions            | 16.4 us                                                | 16.7 us: 1.02x slower                                                      |
| json                      | 5.20 ms                                                | 5.30 ms: 1.02x slower                                                      |
| python_startup_no_site    | 6.99 ms                                                | 7.14 ms: 1.02x slower                                                      |
| coverage                  | 83.7 ms                                                | 86.2 ms: 1.03x slower                                                      |
| tornado_http              | 91.5 ms                                                | 94.3 ms: 1.03x slower                                                      |
| typing_runtime_protocols  | 159 us                                                 | 164 us: 1.03x slower                                                       |
| 2to3                      | 265 ms                                                 | 274 ms: 1.03x slower                                                       |
| html5lib                  | 64.5 ms                                                | 66.8 ms: 1.04x slower                                                      |
| scimark_sor               | 122 ms                                                 | 127 ms: 1.04x slower                                                       |
| genshi_text               | 22.9 ms                                                | 23.8 ms: 1.04x slower                                                      |
| nqueens                   | 80.6 ms                                                | 83.8 ms: 1.04x slower                                                      |
| sqlglot_normalize         | 107 ms                                                 | 113 ms: 1.06x slower                                                       |
| json_loads                | 27.0 us                                                | 28.6 us: 1.06x slower                                                      |
| async_generators          | 433 ms                                                 | 461 ms: 1.06x slower                                                       |
| sqlglot_parse             | 1.27 ms                                                | 1.35 ms: 1.07x slower                                                      |
| raytrace                  | 262 ms                                                 | 281 ms: 1.07x slower                                                       |
| sqlglot_optimize          | 53.9 ms                                                | 58.0 ms: 1.08x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 897 ms: 1.09x slower                                                       |
| regex_compile             | 131 ms                                                 | 143 ms: 1.09x slower                                                       |
| sqlglot_transpile         | 1.57 ms                                                | 1.71 ms: 1.09x slower                                                      |
| sympy_str                 | 274 ms                                                 | 299 ms: 1.09x slower                                                       |
| django_template           | 34.4 ms                                                | 37.7 ms: 1.09x slower                                                      |
| create_gc_cycles          | 1.61 ms                                                | 1.78 ms: 1.11x slower                                                      |
| async_tree_io             | 843 ms                                                 | 933 ms: 1.11x slower                                                       |
| sympy_expand              | 462 ms                                                 | 514 ms: 1.11x slower                                                       |
| genshi_xml                | 50.3 ms                                                | 56.4 ms: 1.12x slower                                                      |
| sympy_integrate           | 19.9 ms                                                | 22.3 ms: 1.12x slower                                                      |
| sympy_sum                 | 150 ms                                                 | 169 ms: 1.13x slower                                                       |
| hexiom                    | 6.13 ms                                                | 6.95 ms: 1.13x slower                                                      |
| pylint                    | 313 ms                                                 | 367 ms: 1.17x slower                                                       |
| generators                | 28.8 ms                                                | 33.9 ms: 1.17x slower                                                      |
| docutils                  | 2.58 sec                                               | 3.05 sec: 1.18x slower                                                     |
| go                        | 142 ms                                                 | 171 ms: 1.21x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed_tg, coroutines, chaos, asyncio_websockets, bench_mp_pool
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 77.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x