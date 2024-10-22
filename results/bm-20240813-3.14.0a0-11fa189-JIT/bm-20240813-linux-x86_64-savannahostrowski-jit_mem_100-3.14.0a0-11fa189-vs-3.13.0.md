# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_mem_100
- machine: linux-x86_64
- commit hash: 11fa189
- commit date: 2024-08-13
- overall geometric mean: 1.01x faster
- HPT reliability: 65.19%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 293 ms: 1.11x slower                                                    |
| docutils       | 2.58 sec                                               | 2.87 sec: 1.11x slower                                                  |
| html5lib       | 64.5 ms                                                | 65.3 ms: 1.01x slower                                                   |
| tornado_http   | 91.5 ms                                                | 94.2 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 397 ms: 1.17x faster                                                    |
| async_tree_none           | 354 ms                                                 | 335 ms: 1.06x faster                                                    |
| async_tree_none_tg        | 320 ms                                                 | 305 ms: 1.05x faster                                                    |
| asyncio_websockets        | 555 ms                                                 | 559 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| coroutines                | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                   |
| asyncio_tcp               | 488 ms                                                 | 501 ms: 1.03x slower                                                    |
| async_generators          | 433 ms                                                 | 455 ms: 1.05x slower                                                    |
| async_tree_io_tg          | 825 ms                                                 | 872 ms: 1.06x slower                                                    |
| async_tree_io             | 843 ms                                                 | 918 ms: 1.09x slower                                                    |
| Geometric mean            | (ref)                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 74.0 ms: 1.06x faster                                                   |
| nbody          | 85.7 ms                                                | 81.7 ms: 1.05x faster                                                   |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.49 ms: 1.11x faster                                                   |
| regex_dna      | 220 ms                                                 | 211 ms: 1.04x faster                                                    |
| regex_v8       | 25.3 ms                                                | 24.4 ms: 1.04x faster                                                   |
| regex_compile  | 131 ms                                                 | 142 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|---------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.11 sec                                               | 1.89 sec: 1.12x faster                                                  |
| xml_etree_process   | 60.4 ms                                                | 59.0 ms: 1.02x faster                                                   |
| xml_etree_generate  | 87.0 ms                                                | 85.4 ms: 1.02x faster                                                   |
| xml_etree_parse     | 156 ms                                                 | 153 ms: 1.02x faster                                                    |
| xml_etree_iterparse | 102 ms                                                 | 103 ms: 1.01x slower                                                    |
| pickle_pure_python  | 300 us                                                 | 304 us: 1.01x slower                                                    |
| json_dumps          | 10.4 ms                                                | 10.6 ms: 1.01x slower                                                   |
| json_loads          | 27.0 us                                                | 28.6 us: 1.06x slower                                                   |
| Geometric mean      | (ref)                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                   |
| python_startup_no_site | 6.99 ms                                                | 7.09 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.90 ms: 1.12x faster                                                   |
| django_template | 34.4 ms                                                | 35.4 ms: 1.03x slower                                                   |
| genshi_text     | 22.9 ms                                                | 25.3 ms: 1.11x slower                                                   |
| genshi_xml      | 50.3 ms                                                | 56.3 ms: 1.12x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 26.6 us: 1.43x faster                                                   |
| deepcopy                  | 352 us                                                 | 265 us: 1.33x faster                                                    |
| deepcopy_reduce           | 3.17 us                                                | 2.66 us: 1.19x faster                                                   |
| richards                  | 48.1 ms                                                | 40.5 ms: 1.19x faster                                                   |
| richards_super            | 54.4 ms                                                | 45.9 ms: 1.19x faster                                                   |
| async_tree_memoization_tg | 465 ms                                                 | 397 ms: 1.17x faster                                                    |
| scimark_fft               | 369 ms                                                 | 318 ms: 1.16x faster                                                    |
| spectral_norm             | 115 ms                                                 | 99.9 ms: 1.15x faster                                                   |
| mako                      | 11.1 ms                                                | 9.90 ms: 1.12x faster                                                   |
| tomli_loads               | 2.11 sec                                               | 1.89 sec: 1.12x faster                                                  |
| regex_effbot              | 3.88 ms                                                | 3.49 ms: 1.11x faster                                                   |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.54 ms: 1.11x faster                                                   |
| crypto_pyaes              | 73.0 ms                                                | 66.8 ms: 1.09x faster                                                   |
| telco                     | 8.45 ms                                                | 7.75 ms: 1.09x faster                                                   |
| gc_traversal              | 3.81 ms                                                | 3.51 ms: 1.08x faster                                                   |
| scimark_sor               | 122 ms                                                 | 115 ms: 1.07x faster                                                    |
| pathlib                   | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                   |
| mdp                       | 2.74 sec                                               | 2.58 sec: 1.06x faster                                                  |
| float                     | 78.5 ms                                                | 74.0 ms: 1.06x faster                                                   |
| scimark_monte_carlo       | 66.3 ms                                                | 62.6 ms: 1.06x faster                                                   |
| async_tree_none           | 354 ms                                                 | 335 ms: 1.06x faster                                                    |
| scimark_lu                | 115 ms                                                 | 109 ms: 1.05x faster                                                    |
| nbody                     | 85.7 ms                                                | 81.7 ms: 1.05x faster                                                   |
| async_tree_none_tg        | 320 ms                                                 | 305 ms: 1.05x faster                                                    |
| regex_dna                 | 220 ms                                                 | 211 ms: 1.04x faster                                                    |
| fannkuch                  | 381 ms                                                 | 367 ms: 1.04x faster                                                    |
| regex_v8                  | 25.3 ms                                                | 24.4 ms: 1.04x faster                                                   |
| pycparser                 | 1.19 sec                                               | 1.16 sec: 1.03x faster                                                  |
| logging_silent            | 102 ns                                                 | 99.7 ns: 1.02x faster                                                   |
| xml_etree_process         | 60.4 ms                                                | 59.0 ms: 1.02x faster                                                   |
| logging_simple            | 5.66 us                                                | 5.56 us: 1.02x faster                                                   |
| pyflate                   | 460 ms                                                 | 451 ms: 1.02x faster                                                    |
| xml_etree_generate        | 87.0 ms                                                | 85.4 ms: 1.02x faster                                                   |
| logging_format            | 6.25 us                                                | 6.15 us: 1.02x faster                                                   |
| xml_etree_parse           | 156 ms                                                 | 153 ms: 1.02x faster                                                    |
| thrift                    | 796 us                                                 | 787 us: 1.01x faster                                                    |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.01x faster                                                    |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                   |
| pprint_safe_repr          | 744 ms                                                 | 738 ms: 1.01x faster                                                    |
| chaos                     | 58.4 ms                                                | 58.2 ms: 1.00x faster                                                   |
| xml_etree_iterparse       | 102 ms                                                 | 103 ms: 1.01x slower                                                    |
| deltablue                 | 3.15 ms                                                | 3.17 ms: 1.01x slower                                                   |
| asyncio_websockets        | 555 ms                                                 | 559 ms: 1.01x slower                                                    |
| pidigits                  | 186 ms                                                 | 188 ms: 1.01x slower                                                    |
| bench_thread_pool         | 815 us                                                 | 821 us: 1.01x slower                                                    |
| json                      | 5.20 ms                                                | 5.25 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| html5lib                  | 64.5 ms                                                | 65.3 ms: 1.01x slower                                                   |
| coroutines                | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                   |
| pickle_pure_python        | 300 us                                                 | 304 us: 1.01x slower                                                    |
| comprehensions            | 16.4 us                                                | 16.6 us: 1.01x slower                                                   |
| python_startup_no_site    | 6.99 ms                                                | 7.09 ms: 1.01x slower                                                   |
| json_dumps                | 10.4 ms                                                | 10.6 ms: 1.01x slower                                                   |
| coverage                  | 83.7 ms                                                | 85.6 ms: 1.02x slower                                                   |
| asyncio_tcp               | 488 ms                                                 | 501 ms: 1.03x slower                                                    |
| tornado_http              | 91.5 ms                                                | 94.2 ms: 1.03x slower                                                   |
| django_template           | 34.4 ms                                                | 35.4 ms: 1.03x slower                                                   |
| raytrace                  | 262 ms                                                 | 269 ms: 1.03x slower                                                    |
| bpe_tokeniser             | 4.69 sec                                               | 4.89 sec: 1.04x slower                                                  |
| pprint_pformat            | 1.51 sec                                               | 1.58 sec: 1.04x slower                                                  |
| go                        | 142 ms                                                 | 148 ms: 1.04x slower                                                    |
| async_generators          | 433 ms                                                 | 455 ms: 1.05x slower                                                    |
| async_tree_io_tg          | 825 ms                                                 | 872 ms: 1.06x slower                                                    |
| json_loads                | 27.0 us                                                | 28.6 us: 1.06x slower                                                   |
| sqlglot_normalize         | 107 ms                                                 | 114 ms: 1.06x slower                                                    |
| nqueens                   | 80.6 ms                                                | 85.7 ms: 1.06x slower                                                   |
| typing_runtime_protocols  | 159 us                                                 | 169 us: 1.06x slower                                                    |
| sqlglot_parse             | 1.27 ms                                                | 1.35 ms: 1.06x slower                                                   |
| create_gc_cycles          | 1.61 ms                                                | 1.74 ms: 1.08x slower                                                   |
| regex_compile             | 131 ms                                                 | 142 ms: 1.08x slower                                                    |
| sympy_str                 | 274 ms                                                 | 296 ms: 1.08x slower                                                    |
| async_tree_io             | 843 ms                                                 | 918 ms: 1.09x slower                                                    |
| sqlglot_transpile         | 1.57 ms                                                | 1.72 ms: 1.09x slower                                                   |
| sympy_expand              | 462 ms                                                 | 505 ms: 1.09x slower                                                    |
| sqlglot_optimize          | 53.9 ms                                                | 59.6 ms: 1.10x slower                                                   |
| genshi_text               | 22.9 ms                                                | 25.3 ms: 1.11x slower                                                   |
| 2to3                      | 265 ms                                                 | 293 ms: 1.11x slower                                                    |
| docutils                  | 2.58 sec                                               | 2.87 sec: 1.11x slower                                                  |
| hexiom                    | 6.13 ms                                                | 6.80 ms: 1.11x slower                                                   |
| genshi_xml                | 50.3 ms                                                | 56.3 ms: 1.12x slower                                                   |
| sympy_sum                 | 150 ms                                                 | 169 ms: 1.13x slower                                                    |
| sympy_integrate           | 19.9 ms                                                | 22.7 ms: 1.14x slower                                                   |
| pylint                    | 313 ms                                                 | 367 ms: 1.17x slower                                                    |
| generators                | 28.8 ms                                                | 34.8 ms: 1.21x slower                                                   |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (5): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, bench_mp_pool, unpickle_pure_python
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 65.19% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x