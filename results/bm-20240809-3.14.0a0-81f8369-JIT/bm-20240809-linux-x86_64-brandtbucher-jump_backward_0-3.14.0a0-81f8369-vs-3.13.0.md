# Results vs. 3.13.0

- fork: brandtbucher
- ref: jump_backward_0
- machine: linux-x86_64
- commit hash: 81f8369
- commit date: 2024-08-09
- overall geometric mean: 1.01x slower
- HPT reliability: 60.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 283 ms: 1.07x slower                                                   |
| docutils       | 2.58 sec                                               | 3.08 sec: 1.19x slower                                                 |
| html5lib       | 64.5 ms                                                | 64.2 ms: 1.01x faster                                                  |
| tornado_http   | 91.5 ms                                                | 107 ms: 1.17x slower                                                   |
| Geometric mean | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 400 ms: 1.16x faster                                                   |
| async_tree_none           | 354 ms                                                 | 333 ms: 1.06x faster                                                   |
| async_tree_none_tg        | 320 ms                                                 | 307 ms: 1.04x faster                                                   |
| asyncio_websockets        | 555 ms                                                 | 559 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.83 sec: 1.02x slower                                                 |
| async_generators          | 433 ms                                                 | 457 ms: 1.06x slower                                                   |
| async_tree_io_tg          | 825 ms                                                 | 881 ms: 1.07x slower                                                   |
| asyncio_tcp               | 488 ms                                                 | 530 ms: 1.09x slower                                                   |
| async_tree_io             | 843 ms                                                 | 921 ms: 1.09x slower                                                   |
| coroutines                | 22.5 ms                                                | 25.2 ms: 1.12x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.0 ms: 1.14x faster                                                  |
| nbody          | 85.7 ms                                                | 79.6 ms: 1.08x faster                                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.60 ms: 1.08x faster                                                  |
| regex_v8       | 25.3 ms                                                | 24.2 ms: 1.04x faster                                                  |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                   |
| regex_compile  | 131 ms                                                 | 138 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|---------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_process   | 60.4 ms                                                | 54.7 ms: 1.10x faster                                                  |
| tomli_loads         | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                 |
| xml_etree_generate  | 87.0 ms                                                | 80.0 ms: 1.09x faster                                                  |
| xml_etree_parse     | 156 ms                                                 | 146 ms: 1.07x faster                                                   |
| xml_etree_iterparse | 102 ms                                                 | 99.2 ms: 1.03x faster                                                  |
| pickle_pure_python  | 300 us                                                 | 293 us: 1.02x faster                                                   |
| json_loads          | 27.0 us                                                | 27.2 us: 1.01x slower                                                  |
| Geometric mean      | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (2): json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                  |
| python_startup_no_site | 6.99 ms                                                | 7.16 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.84 ms: 1.13x faster                                                  |
| genshi_text     | 22.9 ms                                                | 23.9 ms: 1.05x slower                                                  |
| genshi_xml      | 50.3 ms                                                | 55.1 ms: 1.09x slower                                                  |
| django_template | 34.4 ms                                                | 39.3 ms: 1.14x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                           |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 28.8 us: 1.32x faster                                                  |
| deepcopy                  | 352 us                                                 | 270 us: 1.30x faster                                                   |
| scimark_fft               | 369 ms                                                 | 313 ms: 1.18x faster                                                   |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.30 ms: 1.17x faster                                                  |
| async_tree_memoization_tg | 465 ms                                                 | 400 ms: 1.16x faster                                                   |
| float                     | 78.5 ms                                                | 69.0 ms: 1.14x faster                                                  |
| deepcopy_reduce           | 3.17 us                                                | 2.80 us: 1.13x faster                                                  |
| mako                      | 11.1 ms                                                | 9.84 ms: 1.13x faster                                                  |
| spectral_norm             | 115 ms                                                 | 103 ms: 1.12x faster                                                   |
| scimark_monte_carlo       | 66.3 ms                                                | 59.8 ms: 1.11x faster                                                  |
| xml_etree_process         | 60.4 ms                                                | 54.7 ms: 1.10x faster                                                  |
| crypto_pyaes              | 73.0 ms                                                | 66.6 ms: 1.09x faster                                                  |
| telco                     | 8.45 ms                                                | 7.75 ms: 1.09x faster                                                  |
| tomli_loads               | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                 |
| xml_etree_generate        | 87.0 ms                                                | 80.0 ms: 1.09x faster                                                  |
| scimark_sor               | 122 ms                                                 | 113 ms: 1.08x faster                                                   |
| regex_effbot              | 3.88 ms                                                | 3.60 ms: 1.08x faster                                                  |
| nbody                     | 85.7 ms                                                | 79.6 ms: 1.08x faster                                                  |
| pathlib                   | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                  |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                   |
| async_tree_none           | 354 ms                                                 | 333 ms: 1.06x faster                                                   |
| richards_super            | 54.4 ms                                                | 51.7 ms: 1.05x faster                                                  |
| scimark_lu                | 115 ms                                                 | 109 ms: 1.05x faster                                                   |
| richards                  | 48.1 ms                                                | 46.0 ms: 1.05x faster                                                  |
| regex_v8                  | 25.3 ms                                                | 24.2 ms: 1.04x faster                                                  |
| async_tree_none_tg        | 320 ms                                                 | 307 ms: 1.04x faster                                                   |
| logging_silent            | 102 ns                                                 | 98.3 ns: 1.04x faster                                                  |
| regex_dna                 | 220 ms                                                 | 212 ms: 1.04x faster                                                   |
| pyflate                   | 460 ms                                                 | 444 ms: 1.04x faster                                                   |
| json                      | 5.20 ms                                                | 5.03 ms: 1.03x faster                                                  |
| bpe_tokeniser             | 4.69 sec                                               | 4.54 sec: 1.03x faster                                                 |
| xml_etree_iterparse       | 102 ms                                                 | 99.2 ms: 1.03x faster                                                  |
| gc_traversal              | 3.81 ms                                                | 3.71 ms: 1.03x faster                                                  |
| mdp                       | 2.74 sec                                               | 2.67 sec: 1.03x faster                                                 |
| fannkuch                  | 381 ms                                                 | 372 ms: 1.02x faster                                                   |
| pickle_pure_python        | 300 us                                                 | 293 us: 1.02x faster                                                   |
| logging_format            | 6.25 us                                                | 6.12 us: 1.02x faster                                                  |
| pprint_safe_repr          | 744 ms                                                 | 728 ms: 1.02x faster                                                   |
| comprehensions            | 16.4 us                                                | 16.1 us: 1.02x faster                                                  |
| chaos                     | 58.4 ms                                                | 57.7 ms: 1.01x faster                                                  |
| html5lib                  | 64.5 ms                                                | 64.2 ms: 1.01x faster                                                  |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                  |
| asyncio_websockets        | 555 ms                                                 | 559 ms: 1.01x slower                                                   |
| json_loads                | 27.0 us                                                | 27.2 us: 1.01x slower                                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.83 sec: 1.02x slower                                                 |
| python_startup_no_site    | 6.99 ms                                                | 7.16 ms: 1.02x slower                                                  |
| thrift                    | 796 us                                                 | 823 us: 1.03x slower                                                   |
| genshi_text               | 22.9 ms                                                | 23.9 ms: 1.05x slower                                                  |
| regex_compile             | 131 ms                                                 | 138 ms: 1.05x slower                                                   |
| async_generators          | 433 ms                                                 | 457 ms: 1.06x slower                                                   |
| go                        | 142 ms                                                 | 150 ms: 1.06x slower                                                   |
| nqueens                   | 80.6 ms                                                | 85.4 ms: 1.06x slower                                                  |
| raytrace                  | 262 ms                                                 | 277 ms: 1.06x slower                                                   |
| async_tree_io_tg          | 825 ms                                                 | 881 ms: 1.07x slower                                                   |
| typing_runtime_protocols  | 159 us                                                 | 170 us: 1.07x slower                                                   |
| 2to3                      | 265 ms                                                 | 283 ms: 1.07x slower                                                   |
| sqlglot_normalize         | 107 ms                                                 | 115 ms: 1.07x slower                                                   |
| sqlglot_optimize          | 53.9 ms                                                | 58.1 ms: 1.08x slower                                                  |
| bench_thread_pool         | 815 us                                                 | 883 us: 1.08x slower                                                   |
| asyncio_tcp               | 488 ms                                                 | 530 ms: 1.09x slower                                                   |
| sqlglot_parse             | 1.27 ms                                                | 1.37 ms: 1.09x slower                                                  |
| async_tree_io             | 843 ms                                                 | 921 ms: 1.09x slower                                                   |
| genshi_xml                | 50.3 ms                                                | 55.1 ms: 1.09x slower                                                  |
| sqlglot_transpile         | 1.57 ms                                                | 1.73 ms: 1.10x slower                                                  |
| coverage                  | 83.7 ms                                                | 92.7 ms: 1.11x slower                                                  |
| create_gc_cycles          | 1.61 ms                                                | 1.79 ms: 1.11x slower                                                  |
| hexiom                    | 6.13 ms                                                | 6.83 ms: 1.12x slower                                                  |
| coroutines                | 22.5 ms                                                | 25.2 ms: 1.12x slower                                                  |
| django_template           | 34.4 ms                                                | 39.3 ms: 1.14x slower                                                  |
| sympy_expand              | 462 ms                                                 | 530 ms: 1.15x slower                                                   |
| sympy_str                 | 274 ms                                                 | 320 ms: 1.17x slower                                                   |
| tornado_http              | 91.5 ms                                                | 107 ms: 1.17x slower                                                   |
| docutils                  | 2.58 sec                                               | 3.08 sec: 1.19x slower                                                 |
| generators                | 28.8 ms                                                | 35.1 ms: 1.22x slower                                                  |
| sympy_integrate           | 19.9 ms                                                | 25.0 ms: 1.26x slower                                                  |
| pylint                    | 313 ms                                                 | 401 ms: 1.28x slower                                                   |
| sympy_sum                 | 150 ms                                                 | 197 ms: 1.32x slower                                                   |
| deltablue                 | 3.15 ms                                                | 4.24 ms: 1.34x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (10): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, json_dumps, pycparser, logging_simple, meteor_contest, bench_mp_pool, pprint_pformat, unpickle_pure_python
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 60.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.15x