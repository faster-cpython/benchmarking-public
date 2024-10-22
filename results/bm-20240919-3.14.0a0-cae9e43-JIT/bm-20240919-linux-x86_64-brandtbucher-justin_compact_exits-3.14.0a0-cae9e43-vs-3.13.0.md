# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: cae9e43
- commit date: 2024-09-19
- overall geometric mean: 1.01x faster
- HPT reliability: 94.12%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 277 ms: 1.05x slower                                                        |
| docutils       | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                      |
| tornado_http   | 91.5 ms                                                | 94.0 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 371 ms: 1.25x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 380 ms: 1.16x faster                                                        |
| async_tree_none           | 354 ms                                                 | 320 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 536 ms: 1.07x faster                                                        |
| async_tree_none_tg        | 320 ms                                                 | 307 ms: 1.04x faster                                                        |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| asyncio_tcp               | 488 ms                                                 | 499 ms: 1.02x slower                                                        |
| coroutines                | 22.5 ms                                                | 23.1 ms: 1.03x slower                                                       |
| async_generators          | 433 ms                                                 | 458 ms: 1.06x slower                                                        |
| async_tree_io_tg          | 825 ms                                                 | 875 ms: 1.06x slower                                                        |
| async_tree_io             | 843 ms                                                 | 929 ms: 1.10x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.4 ms: 1.11x faster                                                       |
| nbody          | 85.7 ms                                                | 80.5 ms: 1.07x faster                                                       |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.63 ms: 1.07x faster                                                       |
| regex_v8       | 25.3 ms                                                | 24.0 ms: 1.05x faster                                                       |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                                        |
| regex_compile  | 131 ms                                                 | 137 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate  | 87.0 ms                                                | 76.0 ms: 1.14x faster                                                       |
| xml_etree_process   | 60.4 ms                                                | 53.7 ms: 1.13x faster                                                       |
| tomli_loads         | 2.11 sec                                               | 1.91 sec: 1.11x faster                                                      |
| xml_etree_parse     | 156 ms                                                 | 147 ms: 1.06x faster                                                        |
| xml_etree_iterparse | 102 ms                                                 | 97.4 ms: 1.05x faster                                                       |
| json_dumps          | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                       |
| pickle_dict         | 33.2 us                                                | 32.9 us: 1.01x faster                                                       |
| pickle_pure_python  | 300 us                                                 | 302 us: 1.01x slower                                                        |
| json_loads          | 27.0 us                                                | 27.2 us: 1.01x slower                                                       |
| pickle_list         | 5.01 us                                                | 5.18 us: 1.04x slower                                                       |
| unpickle_list       | 4.96 us                                                | 5.19 us: 1.05x slower                                                       |
| Geometric mean      | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (3): pickle, unpickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.72 ms: 1.14x faster                                                       |
| django_template | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                       |
| genshi_text     | 22.9 ms                                                | 24.4 ms: 1.07x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 56.4 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 26.7 us: 1.43x faster                                                       |
| deepcopy                  | 352 us                                                 | 254 us: 1.39x faster                                                        |
| async_tree_memoization_tg | 465 ms                                                 | 371 ms: 1.25x faster                                                        |
| scimark_fft               | 369 ms                                                 | 306 ms: 1.20x faster                                                        |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.21 ms: 1.19x faster                                                       |
| richards_super            | 54.4 ms                                                | 45.7 ms: 1.19x faster                                                       |
| deepcopy_reduce           | 3.17 us                                                | 2.67 us: 1.18x faster                                                       |
| richards                  | 48.1 ms                                                | 40.7 ms: 1.18x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 380 ms: 1.16x faster                                                        |
| spectral_norm             | 115 ms                                                 | 100 ms: 1.15x faster                                                        |
| xml_etree_generate        | 87.0 ms                                                | 76.0 ms: 1.14x faster                                                       |
| mako                      | 11.1 ms                                                | 9.72 ms: 1.14x faster                                                       |
| go                        | 142 ms                                                 | 125 ms: 1.13x faster                                                        |
| xml_etree_process         | 60.4 ms                                                | 53.7 ms: 1.13x faster                                                       |
| float                     | 78.5 ms                                                | 70.4 ms: 1.11x faster                                                       |
| tomli_loads               | 2.11 sec                                               | 1.91 sec: 1.11x faster                                                      |
| async_tree_none           | 354 ms                                                 | 320 ms: 1.11x faster                                                        |
| crypto_pyaes              | 73.0 ms                                                | 66.0 ms: 1.11x faster                                                       |
| mdp                       | 2.74 sec                                               | 2.52 sec: 1.09x faster                                                      |
| pathlib                   | 17.1 ms                                                | 15.7 ms: 1.08x faster                                                       |
| bpe_tokeniser             | 4.69 sec                                               | 4.38 sec: 1.07x faster                                                      |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 536 ms: 1.07x faster                                                        |
| regex_effbot              | 3.88 ms                                                | 3.63 ms: 1.07x faster                                                       |
| nbody                     | 85.7 ms                                                | 80.5 ms: 1.07x faster                                                       |
| telco                     | 8.45 ms                                                | 7.95 ms: 1.06x faster                                                       |
| xml_etree_parse           | 156 ms                                                 | 147 ms: 1.06x faster                                                        |
| scimark_monte_carlo       | 66.3 ms                                                | 62.7 ms: 1.06x faster                                                       |
| regex_v8                  | 25.3 ms                                                | 24.0 ms: 1.05x faster                                                       |
| scimark_sor               | 122 ms                                                 | 117 ms: 1.05x faster                                                        |
| xml_etree_iterparse       | 102 ms                                                 | 97.4 ms: 1.05x faster                                                       |
| scimark_lu                | 115 ms                                                 | 110 ms: 1.04x faster                                                        |
| sqlite_synth              | 2.85 us                                                | 2.73 us: 1.04x faster                                                       |
| async_tree_none_tg        | 320 ms                                                 | 307 ms: 1.04x faster                                                        |
| pprint_safe_repr          | 744 ms                                                 | 722 ms: 1.03x faster                                                        |
| json_dumps                | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                       |
| gc_traversal              | 3.81 ms                                                | 3.72 ms: 1.02x faster                                                       |
| json                      | 5.20 ms                                                | 5.09 ms: 1.02x faster                                                       |
| regex_dna                 | 220 ms                                                 | 215 ms: 1.02x faster                                                        |
| logging_format            | 6.25 us                                                | 6.14 us: 1.02x faster                                                       |
| pprint_pformat            | 1.51 sec                                               | 1.49 sec: 1.02x faster                                                      |
| logging_simple            | 5.66 us                                                | 5.57 us: 1.02x faster                                                       |
| thrift                    | 796 us                                                 | 787 us: 1.01x faster                                                        |
| pickle_dict               | 33.2 us                                                | 32.9 us: 1.01x faster                                                       |
| meteor_contest            | 108 ms                                                 | 107 ms: 1.01x faster                                                        |
| pyflate                   | 460 ms                                                 | 457 ms: 1.01x faster                                                        |
| deltablue                 | 3.15 ms                                                | 3.14 ms: 1.00x faster                                                       |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                       |
| pickle_pure_python        | 300 us                                                 | 302 us: 1.01x slower                                                        |
| json_loads                | 27.0 us                                                | 27.2 us: 1.01x slower                                                       |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| coverage                  | 83.7 ms                                                | 84.7 ms: 1.01x slower                                                       |
| logging_silent            | 102 ns                                                 | 103 ns: 1.01x slower                                                        |
| python_startup_no_site    | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                       |
| comprehensions            | 16.4 us                                                | 16.6 us: 1.01x slower                                                       |
| sqlglot_normalize         | 107 ms                                                 | 110 ms: 1.02x slower                                                        |
| asyncio_tcp               | 488 ms                                                 | 499 ms: 1.02x slower                                                        |
| coroutines                | 22.5 ms                                                | 23.1 ms: 1.03x slower                                                       |
| tornado_http              | 91.5 ms                                                | 94.0 ms: 1.03x slower                                                       |
| bench_thread_pool         | 815 us                                                 | 837 us: 1.03x slower                                                        |
| pickle_list               | 5.01 us                                                | 5.18 us: 1.04x slower                                                       |
| sqlglot_parse             | 1.27 ms                                                | 1.32 ms: 1.04x slower                                                       |
| regex_compile             | 131 ms                                                 | 137 ms: 1.04x slower                                                        |
| django_template           | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                       |
| 2to3                      | 265 ms                                                 | 277 ms: 1.05x slower                                                        |
| unpickle_list             | 4.96 us                                                | 5.19 us: 1.05x slower                                                       |
| sqlglot_optimize          | 53.9 ms                                                | 56.5 ms: 1.05x slower                                                       |
| raytrace                  | 262 ms                                                 | 275 ms: 1.05x slower                                                        |
| async_generators          | 433 ms                                                 | 458 ms: 1.06x slower                                                        |
| async_tree_io_tg          | 825 ms                                                 | 875 ms: 1.06x slower                                                        |
| genshi_text               | 22.9 ms                                                | 24.4 ms: 1.07x slower                                                       |
| dulwich_log               | 63.0 ms                                                | 67.3 ms: 1.07x slower                                                       |
| nqueens                   | 80.6 ms                                                | 86.8 ms: 1.08x slower                                                       |
| create_gc_cycles          | 1.61 ms                                                | 1.74 ms: 1.08x slower                                                       |
| sqlglot_transpile         | 1.57 ms                                                | 1.70 ms: 1.08x slower                                                       |
| sympy_str                 | 274 ms                                                 | 297 ms: 1.09x slower                                                        |
| sympy_expand              | 462 ms                                                 | 502 ms: 1.09x slower                                                        |
| async_tree_io             | 843 ms                                                 | 929 ms: 1.10x slower                                                        |
| genshi_xml                | 50.3 ms                                                | 56.4 ms: 1.12x slower                                                       |
| hexiom                    | 6.13 ms                                                | 6.87 ms: 1.12x slower                                                       |
| generators                | 28.8 ms                                                | 32.4 ms: 1.12x slower                                                       |
| docutils                  | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                      |
| sympy_integrate           | 19.9 ms                                                | 22.7 ms: 1.14x slower                                                       |
| sympy_sum                 | 150 ms                                                 | 171 ms: 1.15x slower                                                        |
| pylint                    | 313 ms                                                 | 360 ms: 1.15x slower                                                        |
| unpack_sequence           | 42.4 ns                                                | 109 ns: 2.57x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, fannkuch, pickle, unpickle_pure_python, asyncio_websockets, bench_mp_pool, chaos, typing_runtime_protocols, unpickle
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, html5lib, mypy2, pycparser

# HPT report

- Reliability score: 94.12% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x