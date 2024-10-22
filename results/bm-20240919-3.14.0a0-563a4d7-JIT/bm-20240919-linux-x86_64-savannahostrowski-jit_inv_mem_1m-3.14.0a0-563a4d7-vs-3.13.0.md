# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_inv_mem_1m
- machine: linux-x86_64
- commit hash: 563a4d7
- commit date: 2024-09-19
- overall geometric mean: 1.01x slower
- HPT reliability: 67.06%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 277 ms: 1.05x slower                                                       |
| docutils       | 2.58 sec                                               | 2.96 sec: 1.14x slower                                                     |
| html5lib       | 64.5 ms                                                | 65.1 ms: 1.01x slower                                                      |
| tornado_http   | 91.5 ms                                                | 94.6 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.06x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 388 ms: 1.20x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 394 ms: 1.12x faster                                                       |
| async_tree_none           | 354 ms                                                 | 317 ms: 1.12x faster                                                       |
| async_tree_none_tg        | 320 ms                                                 | 308 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 565 ms: 1.02x faster                                                       |
| asyncio_tcp               | 488 ms                                                 | 487 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                     |
| coroutines                | 22.5 ms                                                | 23.4 ms: 1.04x slower                                                      |
| async_generators          | 433 ms                                                 | 453 ms: 1.05x slower                                                       |
| async_tree_io_tg          | 825 ms                                                 | 873 ms: 1.06x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.7 ms: 1.13x faster                                                      |
| nbody          | 85.7 ms                                                | 81.3 ms: 1.05x faster                                                      |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.76 ms: 1.03x faster                                                      |
| regex_v8       | 25.3 ms                                                | 24.7 ms: 1.02x faster                                                      |
| regex_dna      | 220 ms                                                 | 218 ms: 1.01x faster                                                       |
| regex_compile  | 131 ms                                                 | 144 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 78.0 ms: 1.12x faster                                                      |
| xml_etree_process    | 60.4 ms                                                | 54.5 ms: 1.11x faster                                                      |
| tomli_loads          | 2.11 sec                                               | 1.95 sec: 1.08x faster                                                     |
| xml_etree_parse      | 156 ms                                                 | 144 ms: 1.08x faster                                                       |
| json_dumps           | 10.4 ms                                                | 9.88 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 102 ms                                                 | 98.8 ms: 1.03x faster                                                      |
| json_loads           | 27.0 us                                                | 26.9 us: 1.00x faster                                                      |
| pickle_list          | 5.01 us                                                | 5.07 us: 1.01x slower                                                      |
| pickle_pure_python   | 300 us                                                 | 305 us: 1.02x slower                                                       |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                       |
| pickle_dict          | 33.2 us                                                | 34.9 us: 1.05x slower                                                      |
| unpickle_list        | 4.96 us                                                | 5.31 us: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (2): pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                      |
| python_startup_no_site | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.79 ms: 1.13x faster                                                      |
| django_template | 34.4 ms                                                | 36.1 ms: 1.05x slower                                                      |
| genshi_text     | 22.9 ms                                                | 25.8 ms: 1.13x slower                                                      |
| genshi_xml      | 50.3 ms                                                | 61.2 ms: 1.21x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 27.5 us: 1.38x faster                                                      |
| deepcopy                  | 352 us                                                 | 269 us: 1.31x faster                                                       |
| async_tree_memoization_tg | 465 ms                                                 | 388 ms: 1.20x faster                                                       |
| scimark_fft               | 369 ms                                                 | 309 ms: 1.19x faster                                                       |
| deepcopy_reduce           | 3.17 us                                                | 2.74 us: 1.16x faster                                                      |
| richards                  | 48.1 ms                                                | 41.9 ms: 1.15x faster                                                      |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.39 ms: 1.15x faster                                                      |
| richards_super            | 54.4 ms                                                | 47.7 ms: 1.14x faster                                                      |
| spectral_norm             | 115 ms                                                 | 101 ms: 1.14x faster                                                       |
| mako                      | 11.1 ms                                                | 9.79 ms: 1.13x faster                                                      |
| float                     | 78.5 ms                                                | 69.7 ms: 1.13x faster                                                      |
| async_tree_memoization    | 442 ms                                                 | 394 ms: 1.12x faster                                                       |
| async_tree_none           | 354 ms                                                 | 317 ms: 1.12x faster                                                       |
| xml_etree_generate        | 87.0 ms                                                | 78.0 ms: 1.12x faster                                                      |
| xml_etree_process         | 60.4 ms                                                | 54.5 ms: 1.11x faster                                                      |
| crypto_pyaes              | 73.0 ms                                                | 66.3 ms: 1.10x faster                                                      |
| tomli_loads               | 2.11 sec                                               | 1.95 sec: 1.08x faster                                                     |
| xml_etree_parse           | 156 ms                                                 | 144 ms: 1.08x faster                                                       |
| go                        | 142 ms                                                 | 133 ms: 1.07x faster                                                       |
| pathlib                   | 17.1 ms                                                | 16.0 ms: 1.06x faster                                                      |
| telco                     | 8.45 ms                                                | 7.98 ms: 1.06x faster                                                      |
| nbody                     | 85.7 ms                                                | 81.3 ms: 1.05x faster                                                      |
| json_dumps                | 10.4 ms                                                | 9.88 ms: 1.05x faster                                                      |
| scimark_monte_carlo       | 66.3 ms                                                | 63.4 ms: 1.05x faster                                                      |
| bpe_tokeniser             | 4.69 sec                                               | 4.49 sec: 1.04x faster                                                     |
| scimark_sor               | 122 ms                                                 | 117 ms: 1.04x faster                                                       |
| sqlite_synth              | 2.85 us                                                | 2.73 us: 1.04x faster                                                      |
| async_tree_none_tg        | 320 ms                                                 | 308 ms: 1.04x faster                                                       |
| regex_effbot              | 3.88 ms                                                | 3.76 ms: 1.03x faster                                                      |
| json                      | 5.20 ms                                                | 5.03 ms: 1.03x faster                                                      |
| scimark_lu                | 115 ms                                                 | 111 ms: 1.03x faster                                                       |
| xml_etree_iterparse       | 102 ms                                                 | 98.8 ms: 1.03x faster                                                      |
| regex_v8                  | 25.3 ms                                                | 24.7 ms: 1.02x faster                                                      |
| fannkuch                  | 381 ms                                                 | 374 ms: 1.02x faster                                                       |
| gc_traversal              | 3.81 ms                                                | 3.74 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 565 ms: 1.02x faster                                                       |
| logging_format            | 6.25 us                                                | 6.18 us: 1.01x faster                                                      |
| thrift                    | 796 us                                                 | 788 us: 1.01x faster                                                       |
| mdp                       | 2.74 sec                                               | 2.71 sec: 1.01x faster                                                     |
| regex_dna                 | 220 ms                                                 | 218 ms: 1.01x faster                                                       |
| json_loads                | 27.0 us                                                | 26.9 us: 1.00x faster                                                      |
| pidigits                  | 186 ms                                                 | 185 ms: 1.00x faster                                                       |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                      |
| asyncio_tcp               | 488 ms                                                 | 487 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                     |
| html5lib                  | 64.5 ms                                                | 65.1 ms: 1.01x slower                                                      |
| python_startup_no_site    | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                      |
| pickle_list               | 5.01 us                                                | 5.07 us: 1.01x slower                                                      |
| pickle_pure_python        | 300 us                                                 | 305 us: 1.02x slower                                                       |
| unpickle_pure_python      | 213 us                                                 | 217 us: 1.02x slower                                                       |
| pyflate                   | 460 ms                                                 | 470 ms: 1.02x slower                                                       |
| pprint_pformat            | 1.51 sec                                               | 1.56 sec: 1.03x slower                                                     |
| deltablue                 | 3.15 ms                                                | 3.24 ms: 1.03x slower                                                      |
| logging_silent            | 102 ns                                                 | 105 ns: 1.03x slower                                                       |
| bench_thread_pool         | 815 us                                                 | 840 us: 1.03x slower                                                       |
| tornado_http              | 91.5 ms                                                | 94.6 ms: 1.03x slower                                                      |
| coroutines                | 22.5 ms                                                | 23.4 ms: 1.04x slower                                                      |
| comprehensions            | 16.4 us                                                | 17.1 us: 1.04x slower                                                      |
| sqlglot_normalize         | 107 ms                                                 | 112 ms: 1.05x slower                                                       |
| 2to3                      | 265 ms                                                 | 277 ms: 1.05x slower                                                       |
| typing_runtime_protocols  | 159 us                                                 | 167 us: 1.05x slower                                                       |
| async_generators          | 433 ms                                                 | 453 ms: 1.05x slower                                                       |
| django_template           | 34.4 ms                                                | 36.1 ms: 1.05x slower                                                      |
| coverage                  | 83.7 ms                                                | 88.0 ms: 1.05x slower                                                      |
| pickle_dict               | 33.2 us                                                | 34.9 us: 1.05x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 873 ms: 1.06x slower                                                       |
| sqlglot_parse             | 1.27 ms                                                | 1.35 ms: 1.06x slower                                                      |
| raytrace                  | 262 ms                                                 | 279 ms: 1.07x slower                                                       |
| unpickle_list             | 4.96 us                                                | 5.31 us: 1.07x slower                                                      |
| sqlglot_transpile         | 1.57 ms                                                | 1.70 ms: 1.08x slower                                                      |
| create_gc_cycles          | 1.61 ms                                                | 1.74 ms: 1.08x slower                                                      |
| sqlglot_optimize          | 53.9 ms                                                | 58.4 ms: 1.08x slower                                                      |
| dulwich_log               | 63.0 ms                                                | 68.5 ms: 1.09x slower                                                      |
| regex_compile             | 131 ms                                                 | 144 ms: 1.10x slower                                                       |
| nqueens                   | 80.6 ms                                                | 88.8 ms: 1.10x slower                                                      |
| sympy_expand              | 462 ms                                                 | 513 ms: 1.11x slower                                                       |
| sympy_str                 | 274 ms                                                 | 305 ms: 1.12x slower                                                       |
| genshi_text               | 22.9 ms                                                | 25.8 ms: 1.13x slower                                                      |
| docutils                  | 2.58 sec                                               | 2.96 sec: 1.14x slower                                                     |
| hexiom                    | 6.13 ms                                                | 7.07 ms: 1.15x slower                                                      |
| sympy_integrate           | 19.9 ms                                                | 23.1 ms: 1.16x slower                                                      |
| sympy_sum                 | 150 ms                                                 | 174 ms: 1.17x slower                                                       |
| pylint                    | 313 ms                                                 | 377 ms: 1.21x slower                                                       |
| genshi_xml                | 50.3 ms                                                | 61.2 ms: 1.21x slower                                                      |
| generators                | 28.8 ms                                                | 36.2 ms: 1.26x slower                                                      |
| unpack_sequence           | 42.4 ns                                                | 113 ns: 2.67x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (11): pycparser, bench_mp_pool, meteor_contest, pickle, asyncio_websockets, unpickle, logging_simple, pprint_safe_repr, chaos, async_tree_cpu_io_mixed_tg, async_tree_io
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 67.06% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x