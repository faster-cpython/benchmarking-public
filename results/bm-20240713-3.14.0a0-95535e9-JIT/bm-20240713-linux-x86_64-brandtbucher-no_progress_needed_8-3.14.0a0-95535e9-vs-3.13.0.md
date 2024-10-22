# Results vs. 3.13.0

- fork: brandtbucher
- ref: no_progress_needed_8
- machine: linux-x86_64
- commit hash: 95535e9
- commit date: 2024-07-13
- overall geometric mean: 1.01x faster
- HPT reliability: 52.36%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 277 ms: 1.05x slower                                                        |
| docutils       | 2.58 sec                                               | 3.02 sec: 1.17x slower                                                      |
| html5lib       | 64.5 ms                                                | 64.9 ms: 1.01x slower                                                       |
| tornado_http   | 91.5 ms                                                | 93.6 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 382 ms: 1.22x faster                                                        |
| async_tree_none           | 354 ms                                                 | 328 ms: 1.08x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 410 ms: 1.08x faster                                                        |
| async_tree_none_tg        | 320 ms                                                 | 300 ms: 1.07x faster                                                        |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                      |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.01x slower                                                        |
| asyncio_tcp               | 488 ms                                                 | 499 ms: 1.02x slower                                                        |
| async_generators          | 433 ms                                                 | 449 ms: 1.04x slower                                                        |
| coroutines                | 22.5 ms                                                | 23.5 ms: 1.05x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                                |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.0 ms: 1.12x faster                                                       |
| nbody          | 85.7 ms                                                | 79.7 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 25.7 ms: 1.02x slower                                                       |
| regex_dna      | 220 ms                                                 | 227 ms: 1.03x slower                                                        |
| regex_compile  | 131 ms                                                 | 138 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads         | 2.11 sec                                               | 1.89 sec: 1.12x faster                                                      |
| xml_etree_generate  | 87.0 ms                                                | 81.4 ms: 1.07x faster                                                       |
| xml_etree_parse     | 156 ms                                                 | 149 ms: 1.05x faster                                                        |
| xml_etree_process   | 60.4 ms                                                | 57.8 ms: 1.05x faster                                                       |
| xml_etree_iterparse | 102 ms                                                 | 98.7 ms: 1.03x faster                                                       |
| json_dumps          | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| pickle_pure_python  | 300 us                                                 | 303 us: 1.01x slower                                                        |
| json_loads          | 27.0 us                                                | 27.9 us: 1.03x slower                                                       |
| Geometric mean      | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.11 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.85 ms: 1.13x faster                                                       |
| django_template | 34.4 ms                                                | 34.8 ms: 1.01x slower                                                       |
| genshi_text     | 22.9 ms                                                | 25.0 ms: 1.09x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 56.6 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 27.3 us: 1.40x faster                                                       |
| deepcopy                  | 352 us                                                 | 264 us: 1.33x faster                                                        |
| richards                  | 48.1 ms                                                | 36.3 ms: 1.33x faster                                                       |
| richards_super            | 54.4 ms                                                | 41.1 ms: 1.33x faster                                                       |
| async_tree_memoization_tg | 465 ms                                                 | 382 ms: 1.22x faster                                                        |
| deepcopy_reduce           | 3.17 us                                                | 2.66 us: 1.19x faster                                                       |
| scimark_fft               | 369 ms                                                 | 316 ms: 1.17x faster                                                        |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.33 ms: 1.16x faster                                                       |
| mako                      | 11.1 ms                                                | 9.85 ms: 1.13x faster                                                       |
| float                     | 78.5 ms                                                | 70.0 ms: 1.12x faster                                                       |
| spectral_norm             | 115 ms                                                 | 103 ms: 1.12x faster                                                        |
| tomli_loads               | 2.11 sec                                               | 1.89 sec: 1.12x faster                                                      |
| crypto_pyaes              | 73.0 ms                                                | 66.9 ms: 1.09x faster                                                       |
| async_tree_none           | 354 ms                                                 | 328 ms: 1.08x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 410 ms: 1.08x faster                                                        |
| nbody                     | 85.7 ms                                                | 79.7 ms: 1.08x faster                                                       |
| scimark_monte_carlo       | 66.3 ms                                                | 62.0 ms: 1.07x faster                                                       |
| xml_etree_generate        | 87.0 ms                                                | 81.4 ms: 1.07x faster                                                       |
| async_tree_none_tg        | 320 ms                                                 | 300 ms: 1.07x faster                                                        |
| gc_traversal              | 3.81 ms                                                | 3.58 ms: 1.06x faster                                                       |
| pathlib                   | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                       |
| telco                     | 8.45 ms                                                | 8.01 ms: 1.06x faster                                                       |
| fannkuch                  | 381 ms                                                 | 361 ms: 1.05x faster                                                        |
| xml_etree_parse           | 156 ms                                                 | 149 ms: 1.05x faster                                                        |
| xml_etree_process         | 60.4 ms                                                | 57.8 ms: 1.05x faster                                                       |
| logging_simple            | 5.66 us                                                | 5.47 us: 1.04x faster                                                       |
| xml_etree_iterparse       | 102 ms                                                 | 98.7 ms: 1.03x faster                                                       |
| logging_format            | 6.25 us                                                | 6.06 us: 1.03x faster                                                       |
| chaos                     | 58.4 ms                                                | 57.1 ms: 1.02x faster                                                       |
| pyflate                   | 460 ms                                                 | 449 ms: 1.02x faster                                                        |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.01x faster                                                        |
| json_dumps                | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| pycparser                 | 1.19 sec                                               | 1.18 sec: 1.01x faster                                                      |
| logging_silent            | 102 ns                                                 | 101 ns: 1.01x faster                                                        |
| mdp                       | 2.74 sec                                               | 2.72 sec: 1.01x faster                                                      |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                      |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.01x slower                                                        |
| html5lib                  | 64.5 ms                                                | 64.9 ms: 1.01x slower                                                       |
| bpe_tokeniser             | 4.69 sec                                               | 4.73 sec: 1.01x slower                                                      |
| pickle_pure_python        | 300 us                                                 | 303 us: 1.01x slower                                                        |
| django_template           | 34.4 ms                                                | 34.8 ms: 1.01x slower                                                       |
| thrift                    | 796 us                                                 | 807 us: 1.01x slower                                                        |
| scimark_lu                | 115 ms                                                 | 117 ms: 1.01x slower                                                        |
| bench_thread_pool         | 815 us                                                 | 826 us: 1.01x slower                                                        |
| comprehensions            | 16.4 us                                                | 16.7 us: 1.02x slower                                                       |
| python_startup_no_site    | 6.99 ms                                                | 7.11 ms: 1.02x slower                                                       |
| regex_v8                  | 25.3 ms                                                | 25.7 ms: 1.02x slower                                                       |
| go                        | 142 ms                                                 | 144 ms: 1.02x slower                                                        |
| sqlglot_parse             | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                       |
| tornado_http              | 91.5 ms                                                | 93.6 ms: 1.02x slower                                                       |
| asyncio_tcp               | 488 ms                                                 | 499 ms: 1.02x slower                                                        |
| raytrace                  | 262 ms                                                 | 268 ms: 1.02x slower                                                        |
| scimark_sor               | 122 ms                                                 | 126 ms: 1.03x slower                                                        |
| json_loads                | 27.0 us                                                | 27.9 us: 1.03x slower                                                       |
| regex_dna                 | 220 ms                                                 | 227 ms: 1.03x slower                                                        |
| async_generators          | 433 ms                                                 | 449 ms: 1.04x slower                                                        |
| sqlglot_normalize         | 107 ms                                                 | 111 ms: 1.04x slower                                                        |
| coroutines                | 22.5 ms                                                | 23.5 ms: 1.05x slower                                                       |
| typing_runtime_protocols  | 159 us                                                 | 167 us: 1.05x slower                                                        |
| 2to3                      | 265 ms                                                 | 277 ms: 1.05x slower                                                        |
| regex_compile             | 131 ms                                                 | 138 ms: 1.05x slower                                                        |
| sqlglot_transpile         | 1.57 ms                                                | 1.65 ms: 1.05x slower                                                       |
| dulwich_log               | 63.0 ms                                                | 66.6 ms: 1.06x slower                                                       |
| sympy_str                 | 274 ms                                                 | 290 ms: 1.06x slower                                                        |
| sqlglot_optimize          | 53.9 ms                                                | 57.4 ms: 1.06x slower                                                       |
| sympy_expand              | 462 ms                                                 | 493 ms: 1.07x slower                                                        |
| dask                      | 338 ms                                                 | 361 ms: 1.07x slower                                                        |
| generators                | 28.8 ms                                                | 30.8 ms: 1.07x slower                                                       |
| nqueens                   | 80.6 ms                                                | 86.6 ms: 1.07x slower                                                       |
| hexiom                    | 6.13 ms                                                | 6.58 ms: 1.07x slower                                                       |
| create_gc_cycles          | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                       |
| deltablue                 | 3.15 ms                                                | 3.43 ms: 1.09x slower                                                       |
| genshi_text               | 22.9 ms                                                | 25.0 ms: 1.09x slower                                                       |
| coverage                  | 83.7 ms                                                | 92.2 ms: 1.10x slower                                                       |
| sympy_integrate           | 19.9 ms                                                | 21.9 ms: 1.10x slower                                                       |
| sympy_sum                 | 150 ms                                                 | 168 ms: 1.12x slower                                                        |
| genshi_xml                | 50.3 ms                                                | 56.6 ms: 1.12x slower                                                       |
| docutils                  | 2.58 sec                                               | 3.02 sec: 1.17x slower                                                      |
| pylint                    | 313 ms                                                 | 373 ms: 1.19x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed, pprint_safe_repr, regex_effbot, pprint_pformat, json, unpickle_pure_python, pidigits, async_tree_cpu_io_mixed_tg, bench_mp_pool, async_tree_io_tg, async_tree_io
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 52.36% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x