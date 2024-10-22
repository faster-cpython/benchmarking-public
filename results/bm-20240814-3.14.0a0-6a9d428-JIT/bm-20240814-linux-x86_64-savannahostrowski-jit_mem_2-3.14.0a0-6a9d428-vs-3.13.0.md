# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_mem_2
- machine: linux-x86_64
- commit hash: 6a9d428
- commit date: 2024-08-14
- overall geometric mean: 1.01x faster
- HPT reliability: 52.17%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 282 ms: 1.06x slower                                                  |
| docutils       | 2.58 sec                                               | 2.96 sec: 1.15x slower                                                |
| html5lib       | 64.5 ms                                                | 67.0 ms: 1.04x slower                                                 |
| tornado_http   | 91.5 ms                                                | 94.5 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 397 ms: 1.17x faster                                                  |
| async_tree_none           | 354 ms                                                 | 330 ms: 1.07x faster                                                  |
| async_tree_none_tg        | 320 ms                                                 | 305 ms: 1.05x faster                                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                |
| asyncio_tcp               | 488 ms                                                 | 493 ms: 1.01x slower                                                  |
| coroutines                | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                 |
| async_generators          | 433 ms                                                 | 457 ms: 1.05x slower                                                  |
| async_tree_io_tg          | 825 ms                                                 | 879 ms: 1.06x slower                                                  |
| async_tree_io             | 843 ms                                                 | 917 ms: 1.09x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.7 ms: 1.09x faster                                                 |
| nbody          | 85.7 ms                                                | 80.3 ms: 1.07x faster                                                 |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.69 ms: 1.05x faster                                                 |
| regex_v8       | 25.3 ms                                                | 24.3 ms: 1.04x faster                                                 |
| regex_dna      | 220 ms                                                 | 220 ms: 1.00x slower                                                  |
| regex_compile  | 131 ms                                                 | 142 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 102 ms                                                 | 98.7 ms: 1.03x faster                                                 |
| xml_etree_process    | 60.4 ms                                                | 58.7 ms: 1.03x faster                                                 |
| xml_etree_generate   | 87.0 ms                                                | 85.3 ms: 1.02x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 211 us: 1.01x faster                                                  |
| pickle_pure_python   | 300 us                                                 | 298 us: 1.01x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| json_loads           | 27.0 us                                                | 28.6 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.4 ms: 1.01x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.08 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                 |
| django_template | 34.4 ms                                                | 36.8 ms: 1.07x slower                                                 |
| genshi_text     | 22.9 ms                                                | 24.6 ms: 1.07x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 56.3 ms: 1.12x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 27.0 us: 1.41x faster                                                 |
| deepcopy                  | 352 us                                                 | 263 us: 1.34x faster                                                  |
| scimark_fft               | 369 ms                                                 | 305 ms: 1.21x faster                                                  |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.24 ms: 1.18x faster                                                 |
| richards_super            | 54.4 ms                                                | 46.1 ms: 1.18x faster                                                 |
| deepcopy_reduce           | 3.17 us                                                | 2.70 us: 1.17x faster                                                 |
| richards                  | 48.1 ms                                                | 41.1 ms: 1.17x faster                                                 |
| async_tree_memoization_tg | 465 ms                                                 | 397 ms: 1.17x faster                                                  |
| spectral_norm             | 115 ms                                                 | 99.2 ms: 1.16x faster                                                 |
| mako                      | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                 |
| float                     | 78.5 ms                                                | 71.7 ms: 1.09x faster                                                 |
| tomli_loads               | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                |
| gc_traversal              | 3.81 ms                                                | 3.51 ms: 1.09x faster                                                 |
| telco                     | 8.45 ms                                                | 7.84 ms: 1.08x faster                                                 |
| mdp                       | 2.74 sec                                               | 2.55 sec: 1.08x faster                                                |
| async_tree_none           | 354 ms                                                 | 330 ms: 1.07x faster                                                  |
| nbody                     | 85.7 ms                                                | 80.3 ms: 1.07x faster                                                 |
| scimark_monte_carlo       | 66.3 ms                                                | 62.1 ms: 1.07x faster                                                 |
| crypto_pyaes              | 73.0 ms                                                | 68.6 ms: 1.06x faster                                                 |
| pathlib                   | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                 |
| xml_etree_parse           | 156 ms                                                 | 147 ms: 1.06x faster                                                  |
| regex_effbot              | 3.88 ms                                                | 3.69 ms: 1.05x faster                                                 |
| async_tree_none_tg        | 320 ms                                                 | 305 ms: 1.05x faster                                                  |
| scimark_lu                | 115 ms                                                 | 110 ms: 1.04x faster                                                  |
| regex_v8                  | 25.3 ms                                                | 24.3 ms: 1.04x faster                                                 |
| scimark_sor               | 122 ms                                                 | 118 ms: 1.04x faster                                                  |
| xml_etree_iterparse       | 102 ms                                                 | 98.7 ms: 1.03x faster                                                 |
| xml_etree_process         | 60.4 ms                                                | 58.7 ms: 1.03x faster                                                 |
| fannkuch                  | 381 ms                                                 | 371 ms: 1.03x faster                                                  |
| pprint_safe_repr          | 744 ms                                                 | 729 ms: 1.02x faster                                                  |
| xml_etree_generate        | 87.0 ms                                                | 85.3 ms: 1.02x faster                                                 |
| pyflate                   | 460 ms                                                 | 451 ms: 1.02x faster                                                  |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| python_startup            | 10.6 ms                                                | 10.4 ms: 1.01x faster                                                 |
| deltablue                 | 3.15 ms                                                | 3.11 ms: 1.01x faster                                                 |
| unpickle_pure_python      | 213 us                                                 | 211 us: 1.01x faster                                                  |
| thrift                    | 796 us                                                 | 788 us: 1.01x faster                                                  |
| chaos                     | 58.4 ms                                                | 57.9 ms: 1.01x faster                                                 |
| logging_simple            | 5.66 us                                                | 5.62 us: 1.01x faster                                                 |
| logging_format            | 6.25 us                                                | 6.21 us: 1.01x faster                                                 |
| pickle_pure_python        | 300 us                                                 | 298 us: 1.01x faster                                                  |
| json_dumps                | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| pidigits                  | 186 ms                                                 | 185 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                |
| regex_dna                 | 220 ms                                                 | 220 ms: 1.00x slower                                                  |
| logging_silent            | 102 ns                                                 | 103 ns: 1.01x slower                                                  |
| bench_thread_pool         | 815 us                                                 | 821 us: 1.01x slower                                                  |
| asyncio_tcp               | 488 ms                                                 | 493 ms: 1.01x slower                                                  |
| raytrace                  | 262 ms                                                 | 264 ms: 1.01x slower                                                  |
| comprehensions            | 16.4 us                                                | 16.6 us: 1.01x slower                                                 |
| python_startup_no_site    | 6.99 ms                                                | 7.08 ms: 1.01x slower                                                 |
| coverage                  | 83.7 ms                                                | 85.0 ms: 1.02x slower                                                 |
| coroutines                | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                 |
| go                        | 142 ms                                                 | 145 ms: 1.02x slower                                                  |
| json                      | 5.20 ms                                                | 5.33 ms: 1.03x slower                                                 |
| tornado_http              | 91.5 ms                                                | 94.5 ms: 1.03x slower                                                 |
| html5lib                  | 64.5 ms                                                | 67.0 ms: 1.04x slower                                                 |
| bpe_tokeniser             | 4.69 sec                                               | 4.90 sec: 1.05x slower                                                |
| sqlglot_parse             | 1.27 ms                                                | 1.33 ms: 1.05x slower                                                 |
| sqlglot_normalize         | 107 ms                                                 | 113 ms: 1.05x slower                                                  |
| async_generators          | 433 ms                                                 | 457 ms: 1.05x slower                                                  |
| json_loads                | 27.0 us                                                | 28.6 us: 1.06x slower                                                 |
| async_tree_io_tg          | 825 ms                                                 | 879 ms: 1.06x slower                                                  |
| 2to3                      | 265 ms                                                 | 282 ms: 1.06x slower                                                  |
| typing_runtime_protocols  | 159 us                                                 | 170 us: 1.07x slower                                                  |
| django_template           | 34.4 ms                                                | 36.8 ms: 1.07x slower                                                 |
| create_gc_cycles          | 1.61 ms                                                | 1.73 ms: 1.07x slower                                                 |
| genshi_text               | 22.9 ms                                                | 24.6 ms: 1.07x slower                                                 |
| sqlglot_transpile         | 1.57 ms                                                | 1.70 ms: 1.08x slower                                                 |
| sympy_str                 | 274 ms                                                 | 296 ms: 1.08x slower                                                  |
| regex_compile             | 131 ms                                                 | 142 ms: 1.08x slower                                                  |
| sqlglot_optimize          | 53.9 ms                                                | 58.5 ms: 1.09x slower                                                 |
| sympy_expand              | 462 ms                                                 | 501 ms: 1.09x slower                                                  |
| nqueens                   | 80.6 ms                                                | 87.7 ms: 1.09x slower                                                 |
| async_tree_io             | 843 ms                                                 | 917 ms: 1.09x slower                                                  |
| genshi_xml                | 50.3 ms                                                | 56.3 ms: 1.12x slower                                                 |
| hexiom                    | 6.13 ms                                                | 6.86 ms: 1.12x slower                                                 |
| sympy_integrate           | 19.9 ms                                                | 22.7 ms: 1.14x slower                                                 |
| sympy_sum                 | 150 ms                                                 | 171 ms: 1.14x slower                                                  |
| docutils                  | 2.58 sec                                               | 2.96 sec: 1.15x slower                                                |
| pylint                    | 313 ms                                                 | 365 ms: 1.17x slower                                                  |
| generators                | 28.8 ms                                                | 34.6 ms: 1.20x slower                                                 |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (7): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, bench_mp_pool, pprint_pformat, pycparser
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 52.17% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x