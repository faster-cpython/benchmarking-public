# Results vs. 3.13.0

- fork: brandtbucher
- ref: ujb0_project_warmup
- machine: linux-x86_64
- commit hash: 8d668dd
- commit date: 2024-09-10
- overall geometric mean: 1.04x slower
- HPT reliability: 98.73%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 289 ms: 1.09x slower                                                       |
| docutils       | 2.58 sec                                               | 3.48 sec: 1.35x slower                                                     |
| html5lib       | 64.5 ms                                                | 74.4 ms: 1.15x slower                                                      |
| tornado_http   | 91.5 ms                                                | 114 ms: 1.25x slower                                                       |
| Geometric mean | (ref)                                                  | 1.21x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 411 ms: 1.13x faster                                                       |
| async_tree_none           | 354 ms                                                 | 338 ms: 1.05x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 423 ms: 1.05x faster                                                       |
| async_tree_none_tg        | 320 ms                                                 | 316 ms: 1.01x faster                                                       |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                       |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                     |
| async_generators          | 433 ms                                                 | 457 ms: 1.06x slower                                                       |
| coroutines                | 22.5 ms                                                | 24.1 ms: 1.07x slower                                                      |
| asyncio_tcp               | 488 ms                                                 | 525 ms: 1.07x slower                                                       |
| async_tree_io_tg          | 825 ms                                                 | 913 ms: 1.11x slower                                                       |
| async_tree_io             | 843 ms                                                 | 953 ms: 1.13x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.02x slower                                                               |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 68.4 ms: 1.15x faster                                                      |
| nbody          | 85.7 ms                                                | 79.8 ms: 1.07x faster                                                      |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.72 ms: 1.04x faster                                                      |
| regex_dna      | 220 ms                                                 | 219 ms: 1.01x faster                                                       |
| regex_v8       | 25.3 ms                                                | 25.8 ms: 1.02x slower                                                      |
| regex_compile  | 131 ms                                                 | 151 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                  | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 54.4 ms: 1.11x faster                                                      |
| xml_etree_generate   | 87.0 ms                                                | 78.7 ms: 1.11x faster                                                      |
| unpickle_pure_python | 213 us                                                 | 196 us: 1.09x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                       |
| json_dumps           | 10.4 ms                                                | 9.95 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 102 ms                                                 | 98.0 ms: 1.04x faster                                                      |
| tomli_loads          | 2.11 sec                                               | 2.13 sec: 1.01x slower                                                     |
| pickle_dict          | 33.2 us                                                | 34.2 us: 1.03x slower                                                      |
| pickle_list          | 5.01 us                                                | 5.17 us: 1.03x slower                                                      |
| unpickle_list        | 4.96 us                                                | 5.23 us: 1.05x slower                                                      |
| pickle_pure_python   | 300 us                                                 | 319 us: 1.06x slower                                                       |
| json_loads           | 27.0 us                                                | 29.7 us: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.7 ms: 1.01x slower                                                      |
| python_startup_no_site | 6.99 ms                                                | 7.15 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.86 ms: 1.13x faster                                                      |
| genshi_text     | 22.9 ms                                                | 23.1 ms: 1.01x slower                                                      |
| django_template | 34.4 ms                                                | 40.4 ms: 1.17x slower                                                      |
| genshi_xml      | 50.3 ms                                                | 62.3 ms: 1.24x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.07x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 27.3 us: 1.39x faster                                                      |
| deepcopy                  | 352 us                                                 | 280 us: 1.26x faster                                                       |
| scimark_fft               | 369 ms                                                 | 310 ms: 1.19x faster                                                       |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.27 ms: 1.18x faster                                                      |
| deepcopy_reduce           | 3.17 us                                                | 2.74 us: 1.15x faster                                                      |
| float                     | 78.5 ms                                                | 68.4 ms: 1.15x faster                                                      |
| async_tree_memoization_tg | 465 ms                                                 | 411 ms: 1.13x faster                                                       |
| scimark_monte_carlo       | 66.3 ms                                                | 58.8 ms: 1.13x faster                                                      |
| mako                      | 11.1 ms                                                | 9.86 ms: 1.13x faster                                                      |
| spectral_norm             | 115 ms                                                 | 103 ms: 1.11x faster                                                       |
| xml_etree_process         | 60.4 ms                                                | 54.4 ms: 1.11x faster                                                      |
| telco                     | 8.45 ms                                                | 7.62 ms: 1.11x faster                                                      |
| xml_etree_generate        | 87.0 ms                                                | 78.7 ms: 1.11x faster                                                      |
| unpickle_pure_python      | 213 us                                                 | 196 us: 1.09x faster                                                       |
| crypto_pyaes              | 73.0 ms                                                | 67.2 ms: 1.09x faster                                                      |
| pathlib                   | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                      |
| nbody                     | 85.7 ms                                                | 79.8 ms: 1.07x faster                                                      |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                       |
| gc_traversal              | 3.81 ms                                                | 3.55 ms: 1.07x faster                                                      |
| pyflate                   | 460 ms                                                 | 436 ms: 1.05x faster                                                       |
| async_tree_none           | 354 ms                                                 | 338 ms: 1.05x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 423 ms: 1.05x faster                                                       |
| json_dumps                | 10.4 ms                                                | 9.95 ms: 1.05x faster                                                      |
| scimark_lu                | 115 ms                                                 | 110 ms: 1.05x faster                                                       |
| regex_effbot              | 3.88 ms                                                | 3.72 ms: 1.04x faster                                                      |
| xml_etree_iterparse       | 102 ms                                                 | 98.0 ms: 1.04x faster                                                      |
| bpe_tokeniser             | 4.69 sec                                               | 4.55 sec: 1.03x faster                                                     |
| scimark_sor               | 122 ms                                                 | 119 ms: 1.03x faster                                                       |
| sqlite_synth              | 2.85 us                                                | 2.79 us: 1.02x faster                                                      |
| async_tree_none_tg        | 320 ms                                                 | 316 ms: 1.01x faster                                                       |
| fannkuch                  | 381 ms                                                 | 376 ms: 1.01x faster                                                       |
| mdp                       | 2.74 sec                                               | 2.72 sec: 1.01x faster                                                     |
| regex_dna                 | 220 ms                                                 | 219 ms: 1.01x faster                                                       |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                       |
| tomli_loads               | 2.11 sec                                               | 2.13 sec: 1.01x slower                                                     |
| genshi_text               | 22.9 ms                                                | 23.1 ms: 1.01x slower                                                      |
| typing_runtime_protocols  | 159 us                                                 | 161 us: 1.01x slower                                                       |
| json                      | 5.20 ms                                                | 5.25 ms: 1.01x slower                                                      |
| python_startup            | 10.6 ms                                                | 10.7 ms: 1.01x slower                                                      |
| meteor_contest            | 108 ms                                                 | 109 ms: 1.02x slower                                                       |
| thrift                    | 796 us                                                 | 809 us: 1.02x slower                                                       |
| bench_mp_pool             | 24.0 ms                                                | 24.4 ms: 1.02x slower                                                      |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                     |
| regex_v8                  | 25.3 ms                                                | 25.8 ms: 1.02x slower                                                      |
| comprehensions            | 16.4 us                                                | 16.7 us: 1.02x slower                                                      |
| python_startup_no_site    | 6.99 ms                                                | 7.15 ms: 1.02x slower                                                      |
| richards_super            | 54.4 ms                                                | 55.8 ms: 1.02x slower                                                      |
| chaos                     | 58.4 ms                                                | 59.9 ms: 1.03x slower                                                      |
| logging_simple            | 5.66 us                                                | 5.83 us: 1.03x slower                                                      |
| pickle_dict               | 33.2 us                                                | 34.2 us: 1.03x slower                                                      |
| pickle_list               | 5.01 us                                                | 5.17 us: 1.03x slower                                                      |
| nqueens                   | 80.6 ms                                                | 83.3 ms: 1.03x slower                                                      |
| coverage                  | 83.7 ms                                                | 86.8 ms: 1.04x slower                                                      |
| pprint_safe_repr          | 744 ms                                                 | 776 ms: 1.04x slower                                                       |
| logging_format            | 6.25 us                                                | 6.53 us: 1.04x slower                                                      |
| unpickle_list             | 4.96 us                                                | 5.23 us: 1.05x slower                                                      |
| async_generators          | 433 ms                                                 | 457 ms: 1.06x slower                                                       |
| pickle_pure_python        | 300 us                                                 | 319 us: 1.06x slower                                                       |
| coroutines                | 22.5 ms                                                | 24.1 ms: 1.07x slower                                                      |
| asyncio_tcp               | 488 ms                                                 | 525 ms: 1.07x slower                                                       |
| raytrace                  | 262 ms                                                 | 281 ms: 1.08x slower                                                       |
| 2to3                      | 265 ms                                                 | 289 ms: 1.09x slower                                                       |
| bench_thread_pool         | 815 us                                                 | 892 us: 1.09x slower                                                       |
| pprint_pformat            | 1.51 sec                                               | 1.66 sec: 1.10x slower                                                     |
| json_loads                | 27.0 us                                                | 29.7 us: 1.10x slower                                                      |
| create_gc_cycles          | 1.61 ms                                                | 1.78 ms: 1.10x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 913 ms: 1.11x slower                                                       |
| pycparser                 | 1.19 sec                                               | 1.35 sec: 1.13x slower                                                     |
| async_tree_io             | 843 ms                                                 | 953 ms: 1.13x slower                                                       |
| deltablue                 | 3.15 ms                                                | 3.59 ms: 1.14x slower                                                      |
| regex_compile             | 131 ms                                                 | 151 ms: 1.15x slower                                                       |
| html5lib                  | 64.5 ms                                                | 74.4 ms: 1.15x slower                                                      |
| django_template           | 34.4 ms                                                | 40.4 ms: 1.17x slower                                                      |
| sqlglot_normalize         | 107 ms                                                 | 126 ms: 1.18x slower                                                       |
| sqlglot_optimize          | 53.9 ms                                                | 64.0 ms: 1.19x slower                                                      |
| sympy_expand              | 462 ms                                                 | 554 ms: 1.20x slower                                                       |
| generators                | 28.8 ms                                                | 34.7 ms: 1.21x slower                                                      |
| hexiom                    | 6.13 ms                                                | 7.49 ms: 1.22x slower                                                      |
| sympy_str                 | 274 ms                                                 | 336 ms: 1.23x slower                                                       |
| genshi_xml                | 50.3 ms                                                | 62.3 ms: 1.24x slower                                                      |
| go                        | 142 ms                                                 | 176 ms: 1.24x slower                                                       |
| tornado_http              | 91.5 ms                                                | 114 ms: 1.25x slower                                                       |
| sympy_integrate           | 19.9 ms                                                | 25.3 ms: 1.27x slower                                                      |
| sqlglot_transpile         | 1.57 ms                                                | 2.08 ms: 1.32x slower                                                      |
| sqlglot_parse             | 1.27 ms                                                | 1.68 ms: 1.33x slower                                                      |
| docutils                  | 2.58 sec                                               | 3.48 sec: 1.35x slower                                                     |
| sympy_sum                 | 150 ms                                                 | 209 ms: 1.40x slower                                                       |
| pylint                    | 313 ms                                                 | 454 ms: 1.45x slower                                                       |
| unpack_sequence           | 42.4 ns                                                | 105 ns: 2.48x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.04x slower                                                               |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, logging_silent, unpickle, pickle, richards, async_tree_cpu_io_mixed_tg
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 98.73% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.17x