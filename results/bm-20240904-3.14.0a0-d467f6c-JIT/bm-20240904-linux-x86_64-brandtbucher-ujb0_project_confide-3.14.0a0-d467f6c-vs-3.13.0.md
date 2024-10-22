# Results vs. 3.13.0

- fork: brandtbucher
- ref: ujb0_project_confide
- machine: linux-x86_64
- commit hash: d467f6c
- commit date: 2024-09-04
- overall geometric mean: 1.03x slower
- HPT reliability: 94.60%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 294 ms: 1.11x slower                                                        |
| docutils       | 2.58 sec                                               | 3.52 sec: 1.36x slower                                                      |
| html5lib       | 64.5 ms                                                | 74.3 ms: 1.15x slower                                                       |
| tornado_http   | 91.5 ms                                                | 118 ms: 1.29x slower                                                        |
| Geometric mean | (ref)                                                  | 1.22x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 416 ms: 1.12x faster                                                        |
| async_tree_none           | 354 ms                                                 | 341 ms: 1.04x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 427 ms: 1.04x faster                                                        |
| asyncio_websockets        | 555 ms                                                 | 560 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.83 sec: 1.02x slower                                                      |
| async_generators          | 433 ms                                                 | 457 ms: 1.06x slower                                                        |
| coroutines                | 22.5 ms                                                | 23.8 ms: 1.06x slower                                                       |
| asyncio_tcp               | 488 ms                                                 | 530 ms: 1.09x slower                                                        |
| async_tree_io_tg          | 825 ms                                                 | 907 ms: 1.10x slower                                                        |
| async_tree_io             | 843 ms                                                 | 961 ms: 1.14x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.02x slower                                                                |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 68.7 ms: 1.14x faster                                                       |
| nbody          | 85.7 ms                                                | 79.9 ms: 1.07x faster                                                       |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.65 ms: 1.06x faster                                                       |
| regex_dna      | 220 ms                                                 | 218 ms: 1.01x faster                                                        |
| regex_v8       | 25.3 ms                                                | 26.1 ms: 1.03x slower                                                       |
| regex_compile  | 131 ms                                                 | 152 ms: 1.16x slower                                                        |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 213 us                                                 | 193 us: 1.11x faster                                                        |
| xml_etree_process    | 60.4 ms                                                | 54.7 ms: 1.10x faster                                                       |
| xml_etree_generate   | 87.0 ms                                                | 80.1 ms: 1.09x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.07x faster                                                        |
| json_dumps           | 10.4 ms                                                | 9.72 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 102 ms                                                 | 98.6 ms: 1.03x faster                                                       |
| tomli_loads          | 2.11 sec                                               | 2.15 sec: 1.02x slower                                                      |
| pickle_pure_python   | 300 us                                                 | 310 us: 1.03x slower                                                        |
| json_loads           | 27.0 us                                                | 29.6 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.16 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.58 ms: 1.16x faster                                                       |
| django_template | 34.4 ms                                                | 40.5 ms: 1.18x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 59.2 ms: 1.18x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 26.3 us: 1.45x faster                                                       |
| deepcopy                  | 352 us                                                 | 263 us: 1.34x faster                                                        |
| scimark_fft               | 369 ms                                                 | 307 ms: 1.20x faster                                                        |
| deepcopy_reduce           | 3.17 us                                                | 2.69 us: 1.18x faster                                                       |
| richards                  | 48.1 ms                                                | 41.4 ms: 1.16x faster                                                       |
| mako                      | 11.1 ms                                                | 9.58 ms: 1.16x faster                                                       |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.34 ms: 1.16x faster                                                       |
| richards_super            | 54.4 ms                                                | 47.1 ms: 1.16x faster                                                       |
| scimark_monte_carlo       | 66.3 ms                                                | 57.9 ms: 1.15x faster                                                       |
| float                     | 78.5 ms                                                | 68.7 ms: 1.14x faster                                                       |
| spectral_norm             | 115 ms                                                 | 101 ms: 1.14x faster                                                        |
| async_tree_memoization_tg | 465 ms                                                 | 416 ms: 1.12x faster                                                        |
| unpickle_pure_python      | 213 us                                                 | 193 us: 1.11x faster                                                        |
| crypto_pyaes              | 73.0 ms                                                | 66.0 ms: 1.11x faster                                                       |
| xml_etree_process         | 60.4 ms                                                | 54.7 ms: 1.10x faster                                                       |
| xml_etree_generate        | 87.0 ms                                                | 80.1 ms: 1.09x faster                                                       |
| telco                     | 8.45 ms                                                | 7.82 ms: 1.08x faster                                                       |
| pathlib                   | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                       |
| nbody                     | 85.7 ms                                                | 79.9 ms: 1.07x faster                                                       |
| xml_etree_parse           | 156 ms                                                 | 145 ms: 1.07x faster                                                        |
| pprint_safe_repr          | 744 ms                                                 | 695 ms: 1.07x faster                                                        |
| json_dumps                | 10.4 ms                                                | 9.72 ms: 1.07x faster                                                       |
| regex_effbot              | 3.88 ms                                                | 3.65 ms: 1.06x faster                                                       |
| scimark_lu                | 115 ms                                                 | 108 ms: 1.06x faster                                                        |
| mdp                       | 2.74 sec                                               | 2.59 sec: 1.06x faster                                                      |
| async_tree_none           | 354 ms                                                 | 341 ms: 1.04x faster                                                        |
| logging_silent            | 102 ns                                                 | 98.3 ns: 1.04x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 427 ms: 1.04x faster                                                        |
| bpe_tokeniser             | 4.69 sec                                               | 4.53 sec: 1.03x faster                                                      |
| xml_etree_iterparse       | 102 ms                                                 | 98.6 ms: 1.03x faster                                                       |
| pprint_pformat            | 1.51 sec                                               | 1.46 sec: 1.03x faster                                                      |
| scimark_sor               | 122 ms                                                 | 120 ms: 1.02x faster                                                        |
| regex_dna                 | 220 ms                                                 | 218 ms: 1.01x faster                                                        |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| gc_traversal              | 3.81 ms                                                | 3.82 ms: 1.00x slower                                                       |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                       |
| meteor_contest            | 108 ms                                                 | 108 ms: 1.01x slower                                                        |
| asyncio_websockets        | 555 ms                                                 | 560 ms: 1.01x slower                                                        |
| comprehensions            | 16.4 us                                                | 16.6 us: 1.01x slower                                                       |
| thrift                    | 796 us                                                 | 810 us: 1.02x slower                                                        |
| tomli_loads               | 2.11 sec                                               | 2.15 sec: 1.02x slower                                                      |
| json                      | 5.20 ms                                                | 5.31 ms: 1.02x slower                                                       |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.83 sec: 1.02x slower                                                      |
| python_startup_no_site    | 6.99 ms                                                | 7.16 ms: 1.03x slower                                                       |
| chaos                     | 58.4 ms                                                | 59.9 ms: 1.03x slower                                                       |
| regex_v8                  | 25.3 ms                                                | 26.1 ms: 1.03x slower                                                       |
| pickle_pure_python        | 300 us                                                 | 310 us: 1.03x slower                                                        |
| typing_runtime_protocols  | 159 us                                                 | 165 us: 1.04x slower                                                        |
| bench_mp_pool             | 24.0 ms                                                | 24.9 ms: 1.04x slower                                                       |
| nqueens                   | 80.6 ms                                                | 84.5 ms: 1.05x slower                                                       |
| coverage                  | 83.7 ms                                                | 87.9 ms: 1.05x slower                                                       |
| logging_format            | 6.25 us                                                | 6.59 us: 1.05x slower                                                       |
| pyflate                   | 460 ms                                                 | 484 ms: 1.05x slower                                                        |
| async_generators          | 433 ms                                                 | 457 ms: 1.06x slower                                                        |
| coroutines                | 22.5 ms                                                | 23.8 ms: 1.06x slower                                                       |
| logging_simple            | 5.66 us                                                | 6.00 us: 1.06x slower                                                       |
| raytrace                  | 262 ms                                                 | 284 ms: 1.09x slower                                                        |
| asyncio_tcp               | 488 ms                                                 | 530 ms: 1.09x slower                                                        |
| bench_thread_pool         | 815 us                                                 | 893 us: 1.10x slower                                                        |
| json_loads                | 27.0 us                                                | 29.6 us: 1.10x slower                                                       |
| async_tree_io_tg          | 825 ms                                                 | 907 ms: 1.10x slower                                                        |
| 2to3                      | 265 ms                                                 | 294 ms: 1.11x slower                                                        |
| create_gc_cycles          | 1.61 ms                                                | 1.81 ms: 1.13x slower                                                       |
| deltablue                 | 3.15 ms                                                | 3.56 ms: 1.13x slower                                                       |
| pycparser                 | 1.19 sec                                               | 1.35 sec: 1.13x slower                                                      |
| async_tree_io             | 843 ms                                                 | 961 ms: 1.14x slower                                                        |
| html5lib                  | 64.5 ms                                                | 74.3 ms: 1.15x slower                                                       |
| regex_compile             | 131 ms                                                 | 152 ms: 1.16x slower                                                        |
| sqlglot_normalize         | 107 ms                                                 | 125 ms: 1.16x slower                                                        |
| django_template           | 34.4 ms                                                | 40.5 ms: 1.18x slower                                                       |
| genshi_xml                | 50.3 ms                                                | 59.2 ms: 1.18x slower                                                       |
| generators                | 28.8 ms                                                | 34.1 ms: 1.18x slower                                                       |
| hexiom                    | 6.13 ms                                                | 7.40 ms: 1.21x slower                                                       |
| sympy_expand              | 462 ms                                                 | 559 ms: 1.21x slower                                                        |
| sqlglot_optimize          | 53.9 ms                                                | 67.6 ms: 1.25x slower                                                       |
| sympy_str                 | 274 ms                                                 | 345 ms: 1.26x slower                                                        |
| go                        | 142 ms                                                 | 181 ms: 1.28x slower                                                        |
| tornado_http              | 91.5 ms                                                | 118 ms: 1.29x slower                                                        |
| docutils                  | 2.58 sec                                               | 3.52 sec: 1.36x slower                                                      |
| sqlglot_parse             | 1.27 ms                                                | 1.75 ms: 1.38x slower                                                       |
| sympy_integrate           | 19.9 ms                                                | 27.5 ms: 1.38x slower                                                       |
| sqlglot_transpile         | 1.57 ms                                                | 2.19 ms: 1.39x slower                                                       |
| sympy_sum                 | 150 ms                                                 | 217 ms: 1.45x slower                                                        |
| pylint                    | 313 ms                                                 | 483 ms: 1.54x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.03x slower                                                                |

Benchmark hidden because not significant (5): genshi_text, fannkuch, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_cpu_io_mixed_tg
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 94.60% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.22x