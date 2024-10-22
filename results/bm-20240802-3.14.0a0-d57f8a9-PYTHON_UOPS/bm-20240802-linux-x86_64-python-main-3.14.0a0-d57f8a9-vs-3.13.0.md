# Results vs. 3.13.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: d57f8a9
- commit date: 2024-08-02
- overall geometric mean: 1.14x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 265 ms                                                 | 319 ms: 1.20x slower                                  |
| docutils       | 2.58 sec                                               | 3.17 sec: 1.23x slower                                |
| html5lib       | 64.5 ms                                                | 73.9 ms: 1.15x slower                                 |
| tornado_http   | 91.5 ms                                                | 97.6 ms: 1.07x slower                                 |
| Geometric mean | (ref)                                                  | 1.16x slower                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 408 ms: 1.14x faster                                  |
| async_tree_none           | 354 ms                                                 | 345 ms: 1.03x faster                                  |
| async_tree_none_tg        | 320 ms                                                 | 314 ms: 1.02x faster                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.82 sec: 1.02x slower                                |
| coroutines                | 22.5 ms                                                | 23.2 ms: 1.03x slower                                 |
| asyncio_tcp               | 488 ms                                                 | 509 ms: 1.04x slower                                  |
| async_generators          | 433 ms                                                 | 459 ms: 1.06x slower                                  |
| async_tree_io_tg          | 825 ms                                                 | 886 ms: 1.07x slower                                  |
| async_tree_io             | 843 ms                                                 | 940 ms: 1.12x slower                                  |
| Geometric mean            | (ref)                                                  | 1.01x slower                                          |

Benchmark hidden because not significant (4): asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                  |
| float          | 78.5 ms                                                | 86.2 ms: 1.10x slower                                 |
| nbody          | 85.7 ms                                                | 122 ms: 1.42x slower                                  |
| Geometric mean | (ref)                                                  | 1.16x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.70 ms: 1.05x faster                                 |
| regex_v8       | 25.3 ms                                                | 24.8 ms: 1.02x faster                                 |
| regex_dna      | 220 ms                                                 | 224 ms: 1.02x slower                                  |
| regex_compile  | 131 ms                                                 | 184 ms: 1.41x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 149 ms: 1.04x faster                                  |
| json_dumps           | 10.4 ms                                                | 10.8 ms: 1.04x slower                                 |
| json_loads           | 27.0 us                                                | 28.3 us: 1.05x slower                                 |
| xml_etree_iterparse  | 102 ms                                                 | 109 ms: 1.07x slower                                  |
| xml_etree_process    | 60.4 ms                                                | 65.0 ms: 1.08x slower                                 |
| xml_etree_generate   | 87.0 ms                                                | 93.7 ms: 1.08x slower                                 |
| tomli_loads          | 2.11 sec                                               | 2.57 sec: 1.22x slower                                |
| unpickle_pure_python | 213 us                                                 | 272 us: 1.27x slower                                  |
| pickle_pure_python   | 300 us                                                 | 404 us: 1.35x slower                                  |
| Geometric mean       | (ref)                                                  | 1.12x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                 |
| python_startup_no_site | 6.99 ms                                                | 7.15 ms: 1.02x slower                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 34.4 ms                                                | 41.4 ms: 1.20x slower                                 |
| genshi_text     | 22.9 ms                                                | 28.0 ms: 1.22x slower                                 |
| mako            | 11.1 ms                                                | 13.9 ms: 1.25x slower                                 |
| genshi_xml      | 50.3 ms                                                | 64.1 ms: 1.27x slower                                 |
| Geometric mean  | (ref)                                                  | 1.24x slower                                          |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 408 ms: 1.14x faster                                  |
| deepcopy                  | 352 us                                                 | 333 us: 1.06x faster                                  |
| regex_effbot              | 3.88 ms                                                | 3.70 ms: 1.05x faster                                 |
| xml_etree_parse           | 156 ms                                                 | 149 ms: 1.04x faster                                  |
| gc_traversal              | 3.81 ms                                                | 3.65 ms: 1.04x faster                                 |
| pathlib                   | 17.1 ms                                                | 16.6 ms: 1.03x faster                                 |
| async_tree_none           | 354 ms                                                 | 345 ms: 1.03x faster                                  |
| regex_v8                  | 25.3 ms                                                | 24.8 ms: 1.02x faster                                 |
| async_tree_none_tg        | 320 ms                                                 | 314 ms: 1.02x faster                                  |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.00x faster                                 |
| json                      | 5.20 ms                                                | 5.25 ms: 1.01x slower                                 |
| thrift                    | 796 us                                                 | 805 us: 1.01x slower                                  |
| pidigits                  | 186 ms                                                 | 188 ms: 1.01x slower                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.82 sec: 1.02x slower                                |
| regex_dna                 | 220 ms                                                 | 224 ms: 1.02x slower                                  |
| deepcopy_reduce           | 3.17 us                                                | 3.24 us: 1.02x slower                                 |
| python_startup_no_site    | 6.99 ms                                                | 7.15 ms: 1.02x slower                                 |
| coroutines                | 22.5 ms                                                | 23.2 ms: 1.03x slower                                 |
| json_dumps                | 10.4 ms                                                | 10.8 ms: 1.04x slower                                 |
| telco                     | 8.45 ms                                                | 8.79 ms: 1.04x slower                                 |
| asyncio_tcp               | 488 ms                                                 | 509 ms: 1.04x slower                                  |
| json_loads                | 27.0 us                                                | 28.3 us: 1.05x slower                                 |
| bench_thread_pool         | 815 us                                                 | 862 us: 1.06x slower                                  |
| async_generators          | 433 ms                                                 | 459 ms: 1.06x slower                                  |
| tornado_http              | 91.5 ms                                                | 97.6 ms: 1.07x slower                                 |
| xml_etree_iterparse       | 102 ms                                                 | 109 ms: 1.07x slower                                  |
| async_tree_io_tg          | 825 ms                                                 | 886 ms: 1.07x slower                                  |
| xml_etree_process         | 60.4 ms                                                | 65.0 ms: 1.08x slower                                 |
| xml_etree_generate        | 87.0 ms                                                | 93.7 ms: 1.08x slower                                 |
| deepcopy_memo             | 38.0 us                                                | 41.0 us: 1.08x slower                                 |
| mdp                       | 2.74 sec                                               | 2.97 sec: 1.08x slower                                |
| float                     | 78.5 ms                                                | 86.2 ms: 1.10x slower                                 |
| create_gc_cycles          | 1.61 ms                                                | 1.77 ms: 1.10x slower                                 |
| async_tree_io             | 843 ms                                                 | 940 ms: 1.12x slower                                  |
| dask                      | 338 ms                                                 | 377 ms: 1.12x slower                                  |
| logging_simple            | 5.66 us                                                | 6.33 us: 1.12x slower                                 |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 5.71 ms: 1.14x slower                                 |
| meteor_contest            | 108 ms                                                 | 123 ms: 1.14x slower                                  |
| html5lib                  | 64.5 ms                                                | 73.9 ms: 1.15x slower                                 |
| pylint                    | 313 ms                                                 | 362 ms: 1.16x slower                                  |
| logging_format            | 6.25 us                                                | 7.27 us: 1.16x slower                                 |
| typing_runtime_protocols  | 159 us                                                 | 187 us: 1.18x slower                                  |
| bpe_tokeniser             | 4.69 sec                                               | 5.52 sec: 1.18x slower                                |
| richards_super            | 54.4 ms                                                | 64.0 ms: 1.18x slower                                 |
| scimark_fft               | 369 ms                                                 | 436 ms: 1.18x slower                                  |
| richards                  | 48.1 ms                                                | 56.9 ms: 1.18x slower                                 |
| scimark_lu                | 115 ms                                                 | 138 ms: 1.20x slower                                  |
| pycparser                 | 1.19 sec                                               | 1.43 sec: 1.20x slower                                |
| sympy_sum                 | 150 ms                                                 | 180 ms: 1.20x slower                                  |
| django_template           | 34.4 ms                                                | 41.4 ms: 1.20x slower                                 |
| 2to3                      | 265 ms                                                 | 319 ms: 1.20x slower                                  |
| sqlglot_optimize          | 53.9 ms                                                | 65.5 ms: 1.21x slower                                 |
| raytrace                  | 262 ms                                                 | 318 ms: 1.21x slower                                  |
| tomli_loads               | 2.11 sec                                               | 2.57 sec: 1.22x slower                                |
| sympy_str                 | 274 ms                                                 | 333 ms: 1.22x slower                                  |
| sympy_integrate           | 19.9 ms                                                | 24.3 ms: 1.22x slower                                 |
| sympy_expand              | 462 ms                                                 | 564 ms: 1.22x slower                                  |
| genshi_text               | 22.9 ms                                                | 28.0 ms: 1.22x slower                                 |
| docutils                  | 2.58 sec                                               | 3.17 sec: 1.23x slower                                |
| crypto_pyaes              | 73.0 ms                                                | 90.0 ms: 1.23x slower                                 |
| sqlglot_transpile         | 1.57 ms                                                | 1.96 ms: 1.25x slower                                 |
| mako                      | 11.1 ms                                                | 13.9 ms: 1.25x slower                                 |
| go                        | 142 ms                                                 | 177 ms: 1.25x slower                                  |
| pyflate                   | 460 ms                                                 | 574 ms: 1.25x slower                                  |
| spectral_norm             | 115 ms                                                 | 144 ms: 1.25x slower                                  |
| sqlglot_normalize         | 107 ms                                                 | 136 ms: 1.26x slower                                  |
| sqlglot_parse             | 1.27 ms                                                | 1.60 ms: 1.27x slower                                 |
| scimark_monte_carlo       | 66.3 ms                                                | 84.4 ms: 1.27x slower                                 |
| unpickle_pure_python      | 213 us                                                 | 272 us: 1.27x slower                                  |
| genshi_xml                | 50.3 ms                                                | 64.1 ms: 1.27x slower                                 |
| pprint_safe_repr          | 744 ms                                                 | 951 ms: 1.28x slower                                  |
| nqueens                   | 80.6 ms                                                | 103 ms: 1.28x slower                                  |
| deltablue                 | 3.15 ms                                                | 4.04 ms: 1.28x slower                                 |
| scimark_sor               | 122 ms                                                 | 158 ms: 1.29x slower                                  |
| fannkuch                  | 381 ms                                                 | 498 ms: 1.31x slower                                  |
| pprint_pformat            | 1.51 sec                                               | 1.98 sec: 1.31x slower                                |
| pickle_pure_python        | 300 us                                                 | 404 us: 1.35x slower                                  |
| chaos                     | 58.4 ms                                                | 79.5 ms: 1.36x slower                                 |
| regex_compile             | 131 ms                                                 | 184 ms: 1.41x slower                                  |
| nbody                     | 85.7 ms                                                | 122 ms: 1.42x slower                                  |
| logging_silent            | 102 ns                                                 | 146 ns: 1.43x slower                                  |
| comprehensions            | 16.4 us                                                | 23.8 us: 1.45x slower                                 |
| generators                | 28.8 ms                                                | 43.4 ms: 1.51x slower                                 |
| hexiom                    | 6.13 ms                                                | 9.64 ms: 1.57x slower                                 |
| Geometric mean            | (ref)                                                  | 1.14x slower                                          |

Benchmark hidden because not significant (6): coverage, asyncio_websockets, bench_mp_pool, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 1.02x