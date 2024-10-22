# Results vs. 3.13.0

- fork: brandtbucher
- ref: deopt_tracing_32
- machine: linux-x86_64
- commit hash: a7a7e7f
- commit date: 2024-09-13
- overall geometric mean: 1.00x slower
- HPT reliability: 81.14%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 279 ms: 1.05x slower                                                    |
| docutils       | 2.58 sec                                               | 2.95 sec: 1.14x slower                                                  |
| tornado_http   | 91.5 ms                                                | 94.6 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x slower                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 387 ms: 1.20x faster                                                    |
| async_tree_none           | 354 ms                                                 | 315 ms: 1.12x faster                                                    |
| async_tree_memoization    | 442 ms                                                 | 394 ms: 1.12x faster                                                    |
| async_tree_none_tg        | 320 ms                                                 | 307 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 565 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                  |
| asyncio_tcp               | 488 ms                                                 | 498 ms: 1.02x slower                                                    |
| async_generators          | 433 ms                                                 | 455 ms: 1.05x slower                                                    |
| async_tree_io_tg          | 825 ms                                                 | 869 ms: 1.05x slower                                                    |
| coroutines                | 22.5 ms                                                | 24.9 ms: 1.10x slower                                                   |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.4 ms: 1.13x faster                                                   |
| nbody          | 85.7 ms                                                | 81.9 ms: 1.05x faster                                                   |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.73 ms: 1.04x faster                                                   |
| regex_v8       | 25.3 ms                                                | 25.1 ms: 1.01x faster                                                   |
| regex_dna      | 220 ms                                                 | 221 ms: 1.00x slower                                                    |
| regex_compile  | 131 ms                                                 | 142 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|---------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate  | 87.0 ms                                                | 77.5 ms: 1.12x faster                                                   |
| xml_etree_process   | 60.4 ms                                                | 54.7 ms: 1.10x faster                                                   |
| tomli_loads         | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                  |
| xml_etree_parse     | 156 ms                                                 | 147 ms: 1.06x faster                                                    |
| json_dumps          | 10.4 ms                                                | 10.1 ms: 1.04x faster                                                   |
| xml_etree_iterparse | 102 ms                                                 | 99.7 ms: 1.02x faster                                                   |
| pickle              | 11.6 us                                                | 11.3 us: 1.02x faster                                                   |
| pickle_dict         | 33.2 us                                                | 33.2 us: 1.00x slower                                                   |
| pickle_list         | 5.01 us                                                | 5.04 us: 1.01x slower                                                   |
| pickle_pure_python  | 300 us                                                 | 304 us: 1.01x slower                                                    |
| unpickle_list       | 4.96 us                                                | 5.30 us: 1.07x slower                                                   |
| Geometric mean      | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (3): unpickle_pure_python, json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                   |
| python_startup_no_site | 6.99 ms                                                | 7.08 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.79 ms: 1.13x faster                                                   |
| django_template | 34.4 ms                                                | 35.8 ms: 1.04x slower                                                   |
| genshi_text     | 22.9 ms                                                | 25.1 ms: 1.10x slower                                                   |
| genshi_xml      | 50.3 ms                                                | 59.4 ms: 1.18x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 27.0 us: 1.41x faster                                                   |
| deepcopy                  | 352 us                                                 | 264 us: 1.34x faster                                                    |
| deepcopy_reduce           | 3.17 us                                                | 2.62 us: 1.21x faster                                                   |
| scimark_fft               | 369 ms                                                 | 307 ms: 1.20x faster                                                    |
| async_tree_memoization_tg | 465 ms                                                 | 387 ms: 1.20x faster                                                    |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.21 ms: 1.20x faster                                                   |
| richards                  | 48.1 ms                                                | 41.1 ms: 1.17x faster                                                   |
| richards_super            | 54.4 ms                                                | 47.3 ms: 1.15x faster                                                   |
| spectral_norm             | 115 ms                                                 | 100 ms: 1.15x faster                                                    |
| mako                      | 11.1 ms                                                | 9.79 ms: 1.13x faster                                                   |
| float                     | 78.5 ms                                                | 69.4 ms: 1.13x faster                                                   |
| async_tree_none           | 354 ms                                                 | 315 ms: 1.12x faster                                                    |
| xml_etree_generate        | 87.0 ms                                                | 77.5 ms: 1.12x faster                                                   |
| async_tree_memoization    | 442 ms                                                 | 394 ms: 1.12x faster                                                    |
| crypto_pyaes              | 73.0 ms                                                | 65.3 ms: 1.12x faster                                                   |
| xml_etree_process         | 60.4 ms                                                | 54.7 ms: 1.10x faster                                                   |
| tomli_loads               | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                  |
| mdp                       | 2.74 sec                                               | 2.52 sec: 1.09x faster                                                  |
| telco                     | 8.45 ms                                                | 7.93 ms: 1.07x faster                                                   |
| xml_etree_parse           | 156 ms                                                 | 147 ms: 1.06x faster                                                    |
| scimark_monte_carlo       | 66.3 ms                                                | 62.6 ms: 1.06x faster                                                   |
| pathlib                   | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                   |
| bpe_tokeniser             | 4.69 sec                                               | 4.45 sec: 1.05x faster                                                  |
| json                      | 5.20 ms                                                | 4.95 ms: 1.05x faster                                                   |
| scimark_sor               | 122 ms                                                 | 117 ms: 1.05x faster                                                    |
| go                        | 142 ms                                                 | 135 ms: 1.05x faster                                                    |
| nbody                     | 85.7 ms                                                | 81.9 ms: 1.05x faster                                                   |
| async_tree_none_tg        | 320 ms                                                 | 307 ms: 1.04x faster                                                    |
| gc_traversal              | 3.81 ms                                                | 3.65 ms: 1.04x faster                                                   |
| regex_effbot              | 3.88 ms                                                | 3.73 ms: 1.04x faster                                                   |
| json_dumps                | 10.4 ms                                                | 10.1 ms: 1.04x faster                                                   |
| scimark_lu                | 115 ms                                                 | 111 ms: 1.03x faster                                                    |
| pprint_safe_repr          | 744 ms                                                 | 720 ms: 1.03x faster                                                    |
| sqlite_synth              | 2.85 us                                                | 2.77 us: 1.03x faster                                                   |
| logging_format            | 6.25 us                                                | 6.10 us: 1.03x faster                                                   |
| xml_etree_iterparse       | 102 ms                                                 | 99.7 ms: 1.02x faster                                                   |
| pprint_pformat            | 1.51 sec                                               | 1.48 sec: 1.02x faster                                                  |
| pickle                    | 11.6 us                                                | 11.3 us: 1.02x faster                                                   |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 565 ms: 1.02x faster                                                    |
| logging_simple            | 5.66 us                                                | 5.58 us: 1.02x faster                                                   |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.01x faster                                                    |
| thrift                    | 796 us                                                 | 789 us: 1.01x faster                                                    |
| regex_v8                  | 25.3 ms                                                | 25.1 ms: 1.01x faster                                                   |
| pidigits                  | 186 ms                                                 | 185 ms: 1.00x faster                                                    |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                   |
| pickle_dict               | 33.2 us                                                | 33.2 us: 1.00x slower                                                   |
| regex_dna                 | 220 ms                                                 | 221 ms: 1.00x slower                                                    |
| pickle_list               | 5.01 us                                                | 5.04 us: 1.01x slower                                                   |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                  |
| pickle_pure_python        | 300 us                                                 | 304 us: 1.01x slower                                                    |
| python_startup_no_site    | 6.99 ms                                                | 7.08 ms: 1.01x slower                                                   |
| typing_runtime_protocols  | 159 us                                                 | 161 us: 1.01x slower                                                    |
| pycparser                 | 1.19 sec                                               | 1.21 sec: 1.02x slower                                                  |
| asyncio_tcp               | 488 ms                                                 | 498 ms: 1.02x slower                                                    |
| bench_thread_pool         | 815 us                                                 | 835 us: 1.02x slower                                                    |
| tornado_http              | 91.5 ms                                                | 94.6 ms: 1.03x slower                                                   |
| django_template           | 34.4 ms                                                | 35.8 ms: 1.04x slower                                                   |
| async_generators          | 433 ms                                                 | 455 ms: 1.05x slower                                                    |
| nqueens                   | 80.6 ms                                                | 84.8 ms: 1.05x slower                                                   |
| 2to3                      | 265 ms                                                 | 279 ms: 1.05x slower                                                    |
| async_tree_io_tg          | 825 ms                                                 | 869 ms: 1.05x slower                                                    |
| raytrace                  | 262 ms                                                 | 276 ms: 1.05x slower                                                    |
| dulwich_log               | 63.0 ms                                                | 66.7 ms: 1.06x slower                                                   |
| sqlglot_parse             | 1.27 ms                                                | 1.35 ms: 1.06x slower                                                   |
| sqlglot_normalize         | 107 ms                                                 | 115 ms: 1.07x slower                                                    |
| unpickle_list             | 4.96 us                                                | 5.30 us: 1.07x slower                                                   |
| coverage                  | 83.7 ms                                                | 89.6 ms: 1.07x slower                                                   |
| regex_compile             | 131 ms                                                 | 142 ms: 1.08x slower                                                    |
| sqlglot_transpile         | 1.57 ms                                                | 1.72 ms: 1.09x slower                                                   |
| sqlglot_optimize          | 53.9 ms                                                | 59.0 ms: 1.09x slower                                                   |
| genshi_text               | 22.9 ms                                                | 25.1 ms: 1.10x slower                                                   |
| create_gc_cycles          | 1.61 ms                                                | 1.77 ms: 1.10x slower                                                   |
| coroutines                | 22.5 ms                                                | 24.9 ms: 1.10x slower                                                   |
| sympy_str                 | 274 ms                                                 | 305 ms: 1.12x slower                                                    |
| sympy_expand              | 462 ms                                                 | 517 ms: 1.12x slower                                                    |
| hexiom                    | 6.13 ms                                                | 6.89 ms: 1.12x slower                                                   |
| deltablue                 | 3.15 ms                                                | 3.55 ms: 1.13x slower                                                   |
| docutils                  | 2.58 sec                                               | 2.95 sec: 1.14x slower                                                  |
| generators                | 28.8 ms                                                | 33.2 ms: 1.15x slower                                                   |
| sympy_integrate           | 19.9 ms                                                | 23.0 ms: 1.16x slower                                                   |
| sympy_sum                 | 150 ms                                                 | 174 ms: 1.16x slower                                                    |
| genshi_xml                | 50.3 ms                                                | 59.4 ms: 1.18x slower                                                   |
| pylint                    | 313 ms                                                 | 379 ms: 1.21x slower                                                    |
| unpack_sequence           | 42.4 ns                                                | 110 ns: 2.61x slower                                                    |
| Geometric mean            | (ref)                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (13): fannkuch, unpickle_pure_python, pyflate, logging_silent, bench_mp_pool, comprehensions, asyncio_websockets, chaos, html5lib, json_loads, async_tree_cpu_io_mixed_tg, async_tree_io, unpickle
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 81.14% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x