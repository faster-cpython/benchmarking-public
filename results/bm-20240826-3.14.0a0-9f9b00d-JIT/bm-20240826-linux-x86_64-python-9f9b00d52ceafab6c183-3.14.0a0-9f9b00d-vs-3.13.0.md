# Results vs. 3.13.0

- fork: python
- ref: 9f9b00d52ceafab6c183
- machine: linux-x86_64
- commit hash: 9f9b00d
- commit date: 2024-08-26
- overall geometric mean: 1.01x faster
- HPT reliability: 67.18%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 277 ms: 1.04x slower                                                  |
| docutils       | 2.58 sec                                               | 3.06 sec: 1.18x slower                                                |
| html5lib       | 64.5 ms                                                | 67.2 ms: 1.04x slower                                                 |
| tornado_http   | 91.5 ms                                                | 94.7 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 402 ms: 1.16x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 400 ms: 1.11x faster                                                  |
| async_tree_none           | 354 ms                                                 | 325 ms: 1.09x faster                                                  |
| async_tree_none_tg        | 320 ms                                                 | 310 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 561 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                |
| asyncio_tcp               | 488 ms                                                 | 493 ms: 1.01x slower                                                  |
| coroutines                | 22.5 ms                                                | 23.1 ms: 1.03x slower                                                 |
| async_generators          | 433 ms                                                 | 459 ms: 1.06x slower                                                  |
| async_tree_io_tg          | 825 ms                                                 | 891 ms: 1.08x slower                                                  |
| async_tree_io             | 843 ms                                                 | 938 ms: 1.11x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.2 ms: 1.12x faster                                                 |
| nbody          | 85.7 ms                                                | 82.7 ms: 1.04x faster                                                 |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.72 ms: 1.04x faster                                                 |
| regex_dna      | 220 ms                                                 | 219 ms: 1.00x faster                                                  |
| regex_compile  | 131 ms                                                 | 141 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.4 ms: 1.12x faster                                                 |
| xml_etree_process    | 60.4 ms                                                | 54.9 ms: 1.10x faster                                                 |
| tomli_loads          | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 102 ms                                                 | 98.4 ms: 1.04x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                  |
| json_loads           | 27.0 us                                                | 28.6 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.16 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.87 ms: 1.12x faster                                                 |
| django_template | 34.4 ms                                                | 36.6 ms: 1.06x slower                                                 |
| genshi_text     | 22.9 ms                                                | 24.4 ms: 1.07x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 55.9 ms: 1.11x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 26.9 us: 1.42x faster                                                 |
| deepcopy                  | 352 us                                                 | 266 us: 1.33x faster                                                  |
| richards                  | 48.1 ms                                                | 39.3 ms: 1.22x faster                                                 |
| scimark_fft               | 369 ms                                                 | 305 ms: 1.21x faster                                                  |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.16 ms: 1.21x faster                                                 |
| richards_super            | 54.4 ms                                                | 45.5 ms: 1.19x faster                                                 |
| deepcopy_reduce           | 3.17 us                                                | 2.68 us: 1.18x faster                                                 |
| async_tree_memoization_tg | 465 ms                                                 | 402 ms: 1.16x faster                                                  |
| spectral_norm             | 115 ms                                                 | 101 ms: 1.14x faster                                                  |
| mako                      | 11.1 ms                                                | 9.87 ms: 1.12x faster                                                 |
| xml_etree_generate        | 87.0 ms                                                | 77.4 ms: 1.12x faster                                                 |
| float                     | 78.5 ms                                                | 70.2 ms: 1.12x faster                                                 |
| crypto_pyaes              | 73.0 ms                                                | 65.9 ms: 1.11x faster                                                 |
| async_tree_memoization    | 442 ms                                                 | 400 ms: 1.11x faster                                                  |
| xml_etree_process         | 60.4 ms                                                | 54.9 ms: 1.10x faster                                                 |
| tomli_loads               | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                |
| async_tree_none           | 354 ms                                                 | 325 ms: 1.09x faster                                                  |
| pathlib                   | 17.1 ms                                                | 15.7 ms: 1.09x faster                                                 |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| scimark_sor               | 122 ms                                                 | 115 ms: 1.06x faster                                                  |
| telco                     | 8.45 ms                                                | 8.01 ms: 1.05x faster                                                 |
| scimark_lu                | 115 ms                                                 | 109 ms: 1.05x faster                                                  |
| pyflate                   | 460 ms                                                 | 436 ms: 1.05x faster                                                  |
| bpe_tokeniser             | 4.69 sec                                               | 4.45 sec: 1.05x faster                                                |
| scimark_monte_carlo       | 66.3 ms                                                | 63.0 ms: 1.05x faster                                                 |
| regex_effbot              | 3.88 ms                                                | 3.72 ms: 1.04x faster                                                 |
| xml_etree_iterparse       | 102 ms                                                 | 98.4 ms: 1.04x faster                                                 |
| nbody                     | 85.7 ms                                                | 82.7 ms: 1.04x faster                                                 |
| async_tree_none_tg        | 320 ms                                                 | 310 ms: 1.03x faster                                                  |
| meteor_contest            | 108 ms                                                 | 104 ms: 1.03x faster                                                  |
| json_dumps                | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                 |
| fannkuch                  | 381 ms                                                 | 370 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 561 ms: 1.02x faster                                                  |
| logging_format            | 6.25 us                                                | 6.11 us: 1.02x faster                                                 |
| mdp                       | 2.74 sec                                               | 2.69 sec: 1.02x faster                                                |
| logging_simple            | 5.66 us                                                | 5.56 us: 1.02x faster                                                 |
| thrift                    | 796 us                                                 | 789 us: 1.01x faster                                                  |
| pprint_pformat            | 1.51 sec                                               | 1.50 sec: 1.01x faster                                                |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| regex_dna                 | 220 ms                                                 | 219 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                |
| bench_thread_pool         | 815 us                                                 | 822 us: 1.01x slower                                                  |
| pidigits                  | 186 ms                                                 | 188 ms: 1.01x slower                                                  |
| asyncio_tcp               | 488 ms                                                 | 493 ms: 1.01x slower                                                  |
| gc_traversal              | 3.81 ms                                                | 3.87 ms: 1.02x slower                                                 |
| deltablue                 | 3.15 ms                                                | 3.20 ms: 1.02x slower                                                 |
| unpickle_pure_python      | 213 us                                                 | 217 us: 1.02x slower                                                  |
| coverage                  | 83.7 ms                                                | 85.2 ms: 1.02x slower                                                 |
| pycparser                 | 1.19 sec                                               | 1.22 sec: 1.02x slower                                                |
| json                      | 5.20 ms                                                | 5.31 ms: 1.02x slower                                                 |
| python_startup_no_site    | 6.99 ms                                                | 7.16 ms: 1.02x slower                                                 |
| coroutines                | 22.5 ms                                                | 23.1 ms: 1.03x slower                                                 |
| comprehensions            | 16.4 us                                                | 16.8 us: 1.03x slower                                                 |
| typing_runtime_protocols  | 159 us                                                 | 165 us: 1.03x slower                                                  |
| tornado_http              | 91.5 ms                                                | 94.7 ms: 1.03x slower                                                 |
| html5lib                  | 64.5 ms                                                | 67.2 ms: 1.04x slower                                                 |
| 2to3                      | 265 ms                                                 | 277 ms: 1.04x slower                                                  |
| sqlglot_normalize         | 107 ms                                                 | 113 ms: 1.05x slower                                                  |
| raytrace                  | 262 ms                                                 | 277 ms: 1.06x slower                                                  |
| json_loads                | 27.0 us                                                | 28.6 us: 1.06x slower                                                 |
| async_generators          | 433 ms                                                 | 459 ms: 1.06x slower                                                  |
| sqlglot_parse             | 1.27 ms                                                | 1.34 ms: 1.06x slower                                                 |
| django_template           | 34.4 ms                                                | 36.6 ms: 1.06x slower                                                 |
| genshi_text               | 22.9 ms                                                | 24.4 ms: 1.07x slower                                                 |
| nqueens                   | 80.6 ms                                                | 86.7 ms: 1.08x slower                                                 |
| regex_compile             | 131 ms                                                 | 141 ms: 1.08x slower                                                  |
| async_tree_io_tg          | 825 ms                                                 | 891 ms: 1.08x slower                                                  |
| sqlglot_optimize          | 53.9 ms                                                | 58.3 ms: 1.08x slower                                                 |
| sqlglot_transpile         | 1.57 ms                                                | 1.70 ms: 1.08x slower                                                 |
| sympy_str                 | 274 ms                                                 | 300 ms: 1.10x slower                                                  |
| sympy_expand              | 462 ms                                                 | 507 ms: 1.10x slower                                                  |
| create_gc_cycles          | 1.61 ms                                                | 1.77 ms: 1.10x slower                                                 |
| genshi_xml                | 50.3 ms                                                | 55.9 ms: 1.11x slower                                                 |
| async_tree_io             | 843 ms                                                 | 938 ms: 1.11x slower                                                  |
| hexiom                    | 6.13 ms                                                | 6.85 ms: 1.12x slower                                                 |
| generators                | 28.8 ms                                                | 33.1 ms: 1.15x slower                                                 |
| sympy_integrate           | 19.9 ms                                                | 22.9 ms: 1.15x slower                                                 |
| sympy_sum                 | 150 ms                                                 | 173 ms: 1.16x slower                                                  |
| docutils                  | 2.58 sec                                               | 3.06 sec: 1.18x slower                                                |
| pylint                    | 313 ms                                                 | 374 ms: 1.20x slower                                                  |
| go                        | 142 ms                                                 | 171 ms: 1.21x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (8): pprint_safe_repr, async_tree_cpu_io_mixed_tg, logging_silent, chaos, asyncio_websockets, regex_v8, bench_mp_pool, pickle_pure_python
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 67.18% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x