# Results vs. 3.13.0

- fork: brandtbucher
- ref: ujb0_project
- machine: linux-x86_64
- commit hash: 8b9b14d
- commit date: 2024-09-03
- overall geometric mean: 1.04x slower
- HPT reliability: 96.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 296 ms: 1.12x slower                                                |
| docutils       | 2.58 sec                                               | 3.51 sec: 1.36x slower                                              |
| html5lib       | 64.5 ms                                                | 75.0 ms: 1.16x slower                                               |
| tornado_http   | 91.5 ms                                                | 117 ms: 1.28x slower                                                |
| Geometric mean | (ref)                                                  | 1.23x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 413 ms: 1.13x faster                                                |
| async_tree_none           | 354 ms                                                 | 340 ms: 1.04x faster                                                |
| async_tree_memoization    | 442 ms                                                 | 426 ms: 1.04x faster                                                |
| asyncio_websockets        | 555 ms                                                 | 559 ms: 1.01x slower                                                |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.82 sec: 1.02x slower                                              |
| async_generators          | 433 ms                                                 | 459 ms: 1.06x slower                                                |
| async_tree_io_tg          | 825 ms                                                 | 885 ms: 1.07x slower                                                |
| asyncio_tcp               | 488 ms                                                 | 529 ms: 1.08x slower                                                |
| coroutines                | 22.5 ms                                                | 24.5 ms: 1.09x slower                                               |
| async_tree_io             | 843 ms                                                 | 953 ms: 1.13x slower                                                |
| Geometric mean            | (ref)                                                  | 1.02x slower                                                        |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.1 ms: 1.14x faster                                               |
| nbody          | 85.7 ms                                                | 80.7 ms: 1.06x faster                                               |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.87 ms: 1.00x faster                                               |
| regex_v8       | 25.3 ms                                                | 26.4 ms: 1.04x slower                                               |
| regex_dna      | 220 ms                                                 | 230 ms: 1.05x slower                                                |
| regex_compile  | 131 ms                                                 | 155 ms: 1.18x slower                                                |
| Geometric mean | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 54.2 ms: 1.12x faster                                               |
| xml_etree_generate   | 87.0 ms                                                | 78.4 ms: 1.11x faster                                               |
| unpickle_pure_python | 213 us                                                 | 197 us: 1.08x faster                                                |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                |
| json_dumps           | 10.4 ms                                                | 9.96 ms: 1.05x faster                                               |
| xml_etree_iterparse  | 102 ms                                                 | 98.5 ms: 1.04x faster                                               |
| tomli_loads          | 2.11 sec                                               | 2.15 sec: 1.02x slower                                              |
| pickle_pure_python   | 300 us                                                 | 314 us: 1.05x slower                                                |
| json_loads           | 27.0 us                                                | 29.6 us: 1.10x slower                                               |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                               |
| python_startup_no_site | 6.99 ms                                                | 7.15 ms: 1.02x slower                                               |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.92 ms: 1.12x faster                                               |
| django_template | 34.4 ms                                                | 39.7 ms: 1.15x slower                                               |
| genshi_xml      | 50.3 ms                                                | 60.8 ms: 1.21x slower                                               |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                        |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 26.1 us: 1.46x faster                                               |
| deepcopy                  | 352 us                                                 | 261 us: 1.35x faster                                                |
| scimark_fft               | 369 ms                                                 | 313 ms: 1.18x faster                                                |
| scimark_monte_carlo       | 66.3 ms                                                | 58.2 ms: 1.14x faster                                               |
| float                     | 78.5 ms                                                | 69.1 ms: 1.14x faster                                               |
| deepcopy_reduce           | 3.17 us                                                | 2.79 us: 1.13x faster                                               |
| spectral_norm             | 115 ms                                                 | 102 ms: 1.13x faster                                                |
| async_tree_memoization_tg | 465 ms                                                 | 413 ms: 1.13x faster                                                |
| mako                      | 11.1 ms                                                | 9.92 ms: 1.12x faster                                               |
| xml_etree_process         | 60.4 ms                                                | 54.2 ms: 1.12x faster                                               |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.52 ms: 1.11x faster                                               |
| xml_etree_generate        | 87.0 ms                                                | 78.4 ms: 1.11x faster                                               |
| crypto_pyaes              | 73.0 ms                                                | 65.9 ms: 1.11x faster                                               |
| richards                  | 48.1 ms                                                | 43.9 ms: 1.10x faster                                               |
| pathlib                   | 17.1 ms                                                | 15.6 ms: 1.09x faster                                               |
| unpickle_pure_python      | 213 us                                                 | 197 us: 1.08x faster                                                |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                |
| nbody                     | 85.7 ms                                                | 80.7 ms: 1.06x faster                                               |
| gc_traversal              | 3.81 ms                                                | 3.60 ms: 1.06x faster                                               |
| json_dumps                | 10.4 ms                                                | 9.96 ms: 1.05x faster                                               |
| scimark_lu                | 115 ms                                                 | 110 ms: 1.04x faster                                                |
| async_tree_none           | 354 ms                                                 | 340 ms: 1.04x faster                                                |
| telco                     | 8.45 ms                                                | 8.13 ms: 1.04x faster                                               |
| bpe_tokeniser             | 4.69 sec                                               | 4.52 sec: 1.04x faster                                              |
| async_tree_memoization    | 442 ms                                                 | 426 ms: 1.04x faster                                                |
| fannkuch                  | 381 ms                                                 | 367 ms: 1.04x faster                                                |
| xml_etree_iterparse       | 102 ms                                                 | 98.5 ms: 1.04x faster                                               |
| richards_super            | 54.4 ms                                                | 52.5 ms: 1.04x faster                                               |
| logging_silent            | 102 ns                                                 | 99.8 ns: 1.02x faster                                               |
| meteor_contest            | 108 ms                                                 | 107 ms: 1.01x faster                                                |
| regex_effbot              | 3.88 ms                                                | 3.87 ms: 1.00x faster                                               |
| pidigits                  | 186 ms                                                 | 185 ms: 1.00x faster                                                |
| mdp                       | 2.74 sec                                               | 2.73 sec: 1.00x faster                                              |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.00x slower                                               |
| pyflate                   | 460 ms                                                 | 461 ms: 1.00x slower                                                |
| asyncio_websockets        | 555 ms                                                 | 559 ms: 1.01x slower                                                |
| json                      | 5.20 ms                                                | 5.25 ms: 1.01x slower                                               |
| typing_runtime_protocols  | 159 us                                                 | 161 us: 1.01x slower                                                |
| scimark_sor               | 122 ms                                                 | 124 ms: 1.02x slower                                                |
| pprint_pformat            | 1.51 sec                                               | 1.54 sec: 1.02x slower                                              |
| chaos                     | 58.4 ms                                                | 59.4 ms: 1.02x slower                                               |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.82 sec: 1.02x slower                                              |
| tomli_loads               | 2.11 sec                                               | 2.15 sec: 1.02x slower                                              |
| python_startup_no_site    | 6.99 ms                                                | 7.15 ms: 1.02x slower                                               |
| comprehensions            | 16.4 us                                                | 16.8 us: 1.02x slower                                               |
| coverage                  | 83.7 ms                                                | 86.6 ms: 1.03x slower                                               |
| nqueens                   | 80.6 ms                                                | 83.5 ms: 1.04x slower                                               |
| thrift                    | 796 us                                                 | 827 us: 1.04x slower                                                |
| bench_mp_pool             | 24.0 ms                                                | 25.0 ms: 1.04x slower                                               |
| regex_v8                  | 25.3 ms                                                | 26.4 ms: 1.04x slower                                               |
| pickle_pure_python        | 300 us                                                 | 314 us: 1.05x slower                                                |
| regex_dna                 | 220 ms                                                 | 230 ms: 1.05x slower                                                |
| logging_simple            | 5.66 us                                                | 5.95 us: 1.05x slower                                               |
| async_generators          | 433 ms                                                 | 459 ms: 1.06x slower                                                |
| logging_format            | 6.25 us                                                | 6.68 us: 1.07x slower                                               |
| async_tree_io_tg          | 825 ms                                                 | 885 ms: 1.07x slower                                                |
| asyncio_tcp               | 488 ms                                                 | 529 ms: 1.08x slower                                                |
| raytrace                  | 262 ms                                                 | 284 ms: 1.08x slower                                                |
| coroutines                | 22.5 ms                                                | 24.5 ms: 1.09x slower                                               |
| json_loads                | 27.0 us                                                | 29.6 us: 1.10x slower                                               |
| bench_thread_pool         | 815 us                                                 | 894 us: 1.10x slower                                                |
| pycparser                 | 1.19 sec                                               | 1.33 sec: 1.11x slower                                              |
| create_gc_cycles          | 1.61 ms                                                | 1.79 ms: 1.12x slower                                               |
| 2to3                      | 265 ms                                                 | 296 ms: 1.12x slower                                                |
| deltablue                 | 3.15 ms                                                | 3.53 ms: 1.12x slower                                               |
| async_tree_io             | 843 ms                                                 | 953 ms: 1.13x slower                                                |
| django_template           | 34.4 ms                                                | 39.7 ms: 1.15x slower                                               |
| html5lib                  | 64.5 ms                                                | 75.0 ms: 1.16x slower                                               |
| sqlglot_normalize         | 107 ms                                                 | 125 ms: 1.17x slower                                                |
| regex_compile             | 131 ms                                                 | 155 ms: 1.18x slower                                                |
| generators                | 28.8 ms                                                | 34.6 ms: 1.20x slower                                               |
| genshi_xml                | 50.3 ms                                                | 60.8 ms: 1.21x slower                                               |
| sympy_expand              | 462 ms                                                 | 559 ms: 1.21x slower                                                |
| hexiom                    | 6.13 ms                                                | 7.42 ms: 1.21x slower                                               |
| sqlglot_optimize          | 53.9 ms                                                | 67.1 ms: 1.24x slower                                               |
| sympy_str                 | 274 ms                                                 | 344 ms: 1.26x slower                                                |
| go                        | 142 ms                                                 | 179 ms: 1.27x slower                                                |
| tornado_http              | 91.5 ms                                                | 117 ms: 1.28x slower                                                |
| docutils                  | 2.58 sec                                               | 3.51 sec: 1.36x slower                                              |
| sqlglot_parse             | 1.27 ms                                                | 1.72 ms: 1.36x slower                                               |
| sympy_integrate           | 19.9 ms                                                | 27.4 ms: 1.38x slower                                               |
| sqlglot_transpile         | 1.57 ms                                                | 2.17 ms: 1.38x slower                                               |
| sympy_sum                 | 150 ms                                                 | 217 ms: 1.45x slower                                                |
| pylint                    | 313 ms                                                 | 480 ms: 1.54x slower                                                |
| Geometric mean            | (ref)                                                  | 1.04x slower                                                        |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_cpu_io_mixed, genshi_text, pprint_safe_repr, async_tree_cpu_io_mixed_tg
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 96.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.22x