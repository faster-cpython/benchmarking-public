# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: 6125ff0
- commit date: 2024-07-13
- overall geometric mean: 1.00x faster
- HPT reliability: 50.26%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 275 ms: 1.04x slower                                                        |
| docutils       | 2.58 sec                                               | 2.89 sec: 1.12x slower                                                      |
| html5lib       | 64.5 ms                                                | 65.2 ms: 1.01x slower                                                       |
| tornado_http   | 91.5 ms                                                | 93.3 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 381 ms: 1.22x faster                                                        |
| async_tree_none           | 354 ms                                                 | 325 ms: 1.09x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 412 ms: 1.07x faster                                                        |
| async_tree_none_tg        | 320 ms                                                 | 300 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 565 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| asyncio_tcp               | 488 ms                                                 | 503 ms: 1.03x slower                                                        |
| async_tree_io_tg          | 825 ms                                                 | 851 ms: 1.03x slower                                                        |
| coroutines                | 22.5 ms                                                | 23.4 ms: 1.04x slower                                                       |
| async_generators          | 433 ms                                                 | 459 ms: 1.06x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                                |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.2 ms: 1.12x faster                                                       |
| nbody          | 85.7 ms                                                | 79.9 ms: 1.07x faster                                                       |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.80 ms: 1.02x faster                                                       |
| regex_dna      | 220 ms                                                 | 219 ms: 1.00x faster                                                        |
| regex_v8       | 25.3 ms                                                | 25.7 ms: 1.02x slower                                                       |
| regex_compile  | 131 ms                                                 | 136 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                      |
| xml_etree_generate   | 87.0 ms                                                | 81.5 ms: 1.07x faster                                                       |
| xml_etree_process    | 60.4 ms                                                | 57.0 ms: 1.06x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                        |
| xml_etree_iterparse  | 102 ms                                                 | 99.1 ms: 1.03x faster                                                       |
| pickle_pure_python   | 300 us                                                 | 298 us: 1.01x faster                                                        |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                       |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                        |
| json_loads           | 27.0 us                                                | 27.9 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.11 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.79 ms: 1.13x faster                                                       |
| django_template | 34.4 ms                                                | 35.7 ms: 1.04x slower                                                       |
| genshi_text     | 22.9 ms                                                | 26.2 ms: 1.14x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 59.3 ms: 1.18x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 28.5 us: 1.33x faster                                                       |
| deepcopy                  | 352 us                                                 | 275 us: 1.28x faster                                                        |
| async_tree_memoization_tg | 465 ms                                                 | 381 ms: 1.22x faster                                                        |
| deepcopy_reduce           | 3.17 us                                                | 2.72 us: 1.16x faster                                                       |
| scimark_fft               | 369 ms                                                 | 319 ms: 1.15x faster                                                        |
| mako                      | 11.1 ms                                                | 9.79 ms: 1.13x faster                                                       |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.49 ms: 1.12x faster                                                       |
| float                     | 78.5 ms                                                | 70.2 ms: 1.12x faster                                                       |
| richards                  | 48.1 ms                                                | 43.9 ms: 1.10x faster                                                       |
| crypto_pyaes              | 73.0 ms                                                | 66.6 ms: 1.09x faster                                                       |
| spectral_norm             | 115 ms                                                 | 105 ms: 1.09x faster                                                        |
| async_tree_none           | 354 ms                                                 | 325 ms: 1.09x faster                                                        |
| tomli_loads               | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                      |
| richards_super            | 54.4 ms                                                | 50.2 ms: 1.08x faster                                                       |
| scimark_monte_carlo       | 66.3 ms                                                | 61.6 ms: 1.08x faster                                                       |
| nbody                     | 85.7 ms                                                | 79.9 ms: 1.07x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 412 ms: 1.07x faster                                                        |
| xml_etree_generate        | 87.0 ms                                                | 81.5 ms: 1.07x faster                                                       |
| async_tree_none_tg        | 320 ms                                                 | 300 ms: 1.07x faster                                                        |
| pprint_safe_repr          | 744 ms                                                 | 701 ms: 1.06x faster                                                        |
| xml_etree_process         | 60.4 ms                                                | 57.0 ms: 1.06x faster                                                       |
| telco                     | 8.45 ms                                                | 8.01 ms: 1.05x faster                                                       |
| xml_etree_parse           | 156 ms                                                 | 148 ms: 1.05x faster                                                        |
| pprint_pformat            | 1.51 sec                                               | 1.45 sec: 1.04x faster                                                      |
| pathlib                   | 17.1 ms                                                | 16.4 ms: 1.04x faster                                                       |
| pyflate                   | 460 ms                                                 | 442 ms: 1.04x faster                                                        |
| fannkuch                  | 381 ms                                                 | 368 ms: 1.04x faster                                                        |
| xml_etree_iterparse       | 102 ms                                                 | 99.1 ms: 1.03x faster                                                       |
| logging_format            | 6.25 us                                                | 6.12 us: 1.02x faster                                                       |
| mdp                       | 2.74 sec                                               | 2.68 sec: 1.02x faster                                                      |
| regex_effbot              | 3.88 ms                                                | 3.80 ms: 1.02x faster                                                       |
| meteor_contest            | 108 ms                                                 | 105 ms: 1.02x faster                                                        |
| gc_traversal              | 3.81 ms                                                | 3.73 ms: 1.02x faster                                                       |
| bpe_tokeniser             | 4.69 sec                                               | 4.60 sec: 1.02x faster                                                      |
| logging_simple            | 5.66 us                                                | 5.56 us: 1.02x faster                                                       |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 565 ms: 1.02x faster                                                        |
| json                      | 5.20 ms                                                | 5.12 ms: 1.02x faster                                                       |
| pickle_pure_python        | 300 us                                                 | 298 us: 1.01x faster                                                        |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                       |
| regex_dna                 | 220 ms                                                 | 219 ms: 1.00x faster                                                        |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| html5lib                  | 64.5 ms                                                | 65.2 ms: 1.01x slower                                                       |
| json_dumps                | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                       |
| sqlglot_parse             | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                       |
| regex_v8                  | 25.3 ms                                                | 25.7 ms: 1.02x slower                                                       |
| python_startup_no_site    | 6.99 ms                                                | 7.11 ms: 1.02x slower                                                       |
| unpickle_pure_python      | 213 us                                                 | 217 us: 1.02x slower                                                        |
| comprehensions            | 16.4 us                                                | 16.7 us: 1.02x slower                                                       |
| tornado_http              | 91.5 ms                                                | 93.3 ms: 1.02x slower                                                       |
| bench_thread_pool         | 815 us                                                 | 832 us: 1.02x slower                                                        |
| asyncio_tcp               | 488 ms                                                 | 503 ms: 1.03x slower                                                        |
| async_tree_io_tg          | 825 ms                                                 | 851 ms: 1.03x slower                                                        |
| sqlglot_transpile         | 1.57 ms                                                | 1.62 ms: 1.03x slower                                                       |
| regex_compile             | 131 ms                                                 | 136 ms: 1.03x slower                                                        |
| json_loads                | 27.0 us                                                | 27.9 us: 1.04x slower                                                       |
| go                        | 142 ms                                                 | 147 ms: 1.04x slower                                                        |
| django_template           | 34.4 ms                                                | 35.7 ms: 1.04x slower                                                       |
| raytrace                  | 262 ms                                                 | 271 ms: 1.04x slower                                                        |
| coroutines                | 22.5 ms                                                | 23.4 ms: 1.04x slower                                                       |
| 2to3                      | 265 ms                                                 | 275 ms: 1.04x slower                                                        |
| sqlglot_optimize          | 53.9 ms                                                | 56.3 ms: 1.04x slower                                                       |
| logging_silent            | 102 ns                                                 | 107 ns: 1.05x slower                                                        |
| scimark_sor               | 122 ms                                                 | 129 ms: 1.05x slower                                                        |
| async_generators          | 433 ms                                                 | 459 ms: 1.06x slower                                                        |
| nqueens                   | 80.6 ms                                                | 85.7 ms: 1.06x slower                                                       |
| hexiom                    | 6.13 ms                                                | 6.55 ms: 1.07x slower                                                       |
| sqlglot_normalize         | 107 ms                                                 | 115 ms: 1.07x slower                                                        |
| dulwich_log               | 63.0 ms                                                | 67.5 ms: 1.07x slower                                                       |
| dask                      | 338 ms                                                 | 363 ms: 1.07x slower                                                        |
| typing_runtime_protocols  | 159 us                                                 | 172 us: 1.08x slower                                                        |
| sympy_str                 | 274 ms                                                 | 296 ms: 1.08x slower                                                        |
| sympy_expand              | 462 ms                                                 | 502 ms: 1.09x slower                                                        |
| create_gc_cycles          | 1.61 ms                                                | 1.76 ms: 1.09x slower                                                       |
| pylint                    | 313 ms                                                 | 342 ms: 1.09x slower                                                        |
| scimark_lu                | 115 ms                                                 | 127 ms: 1.10x slower                                                        |
| coverage                  | 83.7 ms                                                | 93.0 ms: 1.11x slower                                                       |
| docutils                  | 2.58 sec                                               | 2.89 sec: 1.12x slower                                                      |
| sympy_sum                 | 150 ms                                                 | 168 ms: 1.12x slower                                                        |
| sympy_integrate           | 19.9 ms                                                | 22.4 ms: 1.12x slower                                                       |
| deltablue                 | 3.15 ms                                                | 3.59 ms: 1.14x slower                                                       |
| genshi_text               | 22.9 ms                                                | 26.2 ms: 1.14x slower                                                       |
| genshi_xml                | 50.3 ms                                                | 59.3 ms: 1.18x slower                                                       |
| generators                | 28.8 ms                                                | 38.6 ms: 1.34x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (7): pycparser, async_tree_cpu_io_mixed_tg, asyncio_websockets, bench_mp_pool, chaos, thrift, async_tree_io
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 50.26% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x