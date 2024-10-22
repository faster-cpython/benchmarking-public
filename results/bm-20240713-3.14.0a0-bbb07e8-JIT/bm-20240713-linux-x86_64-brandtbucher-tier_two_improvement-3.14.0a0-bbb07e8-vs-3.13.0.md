# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.01x faster
- HPT reliability: 71.03%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 272 ms: 1.03x slower                                                        |
| docutils       | 2.58 sec                                               | 2.87 sec: 1.11x slower                                                      |
| html5lib       | 64.5 ms                                                | 66.0 ms: 1.02x slower                                                       |
| tornado_http   | 91.5 ms                                                | 93.0 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 372 ms: 1.25x faster                                                        |
| async_tree_none           | 354 ms                                                 | 321 ms: 1.10x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 403 ms: 1.10x faster                                                        |
| async_tree_none_tg        | 320 ms                                                 | 295 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 561 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 841 ms: 1.02x slower                                                        |
| asyncio_tcp               | 488 ms                                                 | 502 ms: 1.03x slower                                                        |
| async_generators          | 433 ms                                                 | 449 ms: 1.04x slower                                                        |
| coroutines                | 22.5 ms                                                | 23.5 ms: 1.04x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.3 ms: 1.13x faster                                                       |
| nbody          | 85.7 ms                                                | 79.2 ms: 1.08x faster                                                       |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.73 ms: 1.04x faster                                                       |
| regex_v8       | 25.3 ms                                                | 24.4 ms: 1.04x faster                                                       |
| regex_compile  | 131 ms                                                 | 135 ms: 1.03x slower                                                        |
| regex_dna      | 220 ms                                                 | 229 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.93 sec: 1.10x faster                                                      |
| xml_etree_generate   | 87.0 ms                                                | 80.6 ms: 1.08x faster                                                       |
| xml_etree_process    | 60.4 ms                                                | 57.0 ms: 1.06x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                        |
| xml_etree_iterparse  | 102 ms                                                 | 99.1 ms: 1.03x faster                                                       |
| pickle_pure_python   | 300 us                                                 | 297 us: 1.01x faster                                                        |
| json_dumps           | 10.4 ms                                                | 10.4 ms: 1.01x faster                                                       |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                        |
| json_loads           | 27.0 us                                                | 27.9 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                       |
| python_startup_no_site | 6.99 ms                                                | 7.09 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.86 ms: 1.13x faster                                                       |
| django_template | 34.4 ms                                                | 34.9 ms: 1.02x slower                                                       |
| genshi_text     | 22.9 ms                                                | 24.6 ms: 1.08x slower                                                       |
| genshi_xml      | 50.3 ms                                                | 56.3 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 28.9 us: 1.31x faster                                                       |
| deepcopy                  | 352 us                                                 | 278 us: 1.27x faster                                                        |
| async_tree_memoization_tg | 465 ms                                                 | 372 ms: 1.25x faster                                                        |
| scimark_fft               | 369 ms                                                 | 315 ms: 1.17x faster                                                        |
| richards                  | 48.1 ms                                                | 41.3 ms: 1.17x faster                                                       |
| richards_super            | 54.4 ms                                                | 47.6 ms: 1.14x faster                                                       |
| deepcopy_reduce           | 3.17 us                                                | 2.78 us: 1.14x faster                                                       |
| float                     | 78.5 ms                                                | 69.3 ms: 1.13x faster                                                       |
| mako                      | 11.1 ms                                                | 9.86 ms: 1.13x faster                                                       |
| spectral_norm             | 115 ms                                                 | 103 ms: 1.12x faster                                                        |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.50 ms: 1.12x faster                                                       |
| async_tree_none           | 354 ms                                                 | 321 ms: 1.10x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 403 ms: 1.10x faster                                                        |
| tomli_loads               | 2.11 sec                                               | 1.93 sec: 1.10x faster                                                      |
| scimark_monte_carlo       | 66.3 ms                                                | 60.9 ms: 1.09x faster                                                       |
| async_tree_none_tg        | 320 ms                                                 | 295 ms: 1.09x faster                                                        |
| nbody                     | 85.7 ms                                                | 79.2 ms: 1.08x faster                                                       |
| crypto_pyaes              | 73.0 ms                                                | 67.5 ms: 1.08x faster                                                       |
| xml_etree_generate        | 87.0 ms                                                | 80.6 ms: 1.08x faster                                                       |
| pyflate                   | 460 ms                                                 | 426 ms: 1.08x faster                                                        |
| gc_traversal              | 3.81 ms                                                | 3.55 ms: 1.07x faster                                                       |
| pathlib                   | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                       |
| xml_etree_process         | 60.4 ms                                                | 57.0 ms: 1.06x faster                                                       |
| xml_etree_parse           | 156 ms                                                 | 147 ms: 1.06x faster                                                        |
| pycparser                 | 1.19 sec                                               | 1.13 sec: 1.06x faster                                                      |
| telco                     | 8.45 ms                                                | 8.04 ms: 1.05x faster                                                       |
| fannkuch                  | 381 ms                                                 | 363 ms: 1.05x faster                                                        |
| regex_effbot              | 3.88 ms                                                | 3.73 ms: 1.04x faster                                                       |
| regex_v8                  | 25.3 ms                                                | 24.4 ms: 1.04x faster                                                       |
| pprint_pformat            | 1.51 sec                                               | 1.46 sec: 1.03x faster                                                      |
| pprint_safe_repr          | 744 ms                                                 | 720 ms: 1.03x faster                                                        |
| logging_simple            | 5.66 us                                                | 5.49 us: 1.03x faster                                                       |
| logging_format            | 6.25 us                                                | 6.07 us: 1.03x faster                                                       |
| xml_etree_iterparse       | 102 ms                                                 | 99.1 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 561 ms: 1.02x faster                                                        |
| meteor_contest            | 108 ms                                                 | 105 ms: 1.02x faster                                                        |
| bpe_tokeniser             | 4.69 sec                                               | 4.59 sec: 1.02x faster                                                      |
| pickle_pure_python        | 300 us                                                 | 297 us: 1.01x faster                                                        |
| json                      | 5.20 ms                                                | 5.15 ms: 1.01x faster                                                       |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                       |
| json_dumps                | 10.4 ms                                                | 10.4 ms: 1.01x faster                                                       |
| pidigits                  | 186 ms                                                 | 185 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| sqlglot_parse             | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                       |
| comprehensions            | 16.4 us                                                | 16.6 us: 1.01x slower                                                       |
| python_startup_no_site    | 6.99 ms                                                | 7.09 ms: 1.01x slower                                                       |
| django_template           | 34.4 ms                                                | 34.9 ms: 1.02x slower                                                       |
| go                        | 142 ms                                                 | 144 ms: 1.02x slower                                                        |
| tornado_http              | 91.5 ms                                                | 93.0 ms: 1.02x slower                                                       |
| unpickle_pure_python      | 213 us                                                 | 217 us: 1.02x slower                                                        |
| async_tree_io_tg          | 825 ms                                                 | 841 ms: 1.02x slower                                                        |
| sqlglot_transpile         | 1.57 ms                                                | 1.61 ms: 1.02x slower                                                       |
| html5lib                  | 64.5 ms                                                | 66.0 ms: 1.02x slower                                                       |
| raytrace                  | 262 ms                                                 | 268 ms: 1.02x slower                                                        |
| bench_thread_pool         | 815 us                                                 | 834 us: 1.02x slower                                                        |
| sqlglot_optimize          | 53.9 ms                                                | 55.3 ms: 1.03x slower                                                       |
| regex_compile             | 131 ms                                                 | 135 ms: 1.03x slower                                                        |
| 2to3                      | 265 ms                                                 | 272 ms: 1.03x slower                                                        |
| asyncio_tcp               | 488 ms                                                 | 502 ms: 1.03x slower                                                        |
| sqlglot_normalize         | 107 ms                                                 | 111 ms: 1.03x slower                                                        |
| json_loads                | 27.0 us                                                | 27.9 us: 1.03x slower                                                       |
| async_generators          | 433 ms                                                 | 449 ms: 1.04x slower                                                        |
| logging_silent            | 102 ns                                                 | 106 ns: 1.04x slower                                                        |
| regex_dna                 | 220 ms                                                 | 229 ms: 1.04x slower                                                        |
| coroutines                | 22.5 ms                                                | 23.5 ms: 1.04x slower                                                       |
| nqueens                   | 80.6 ms                                                | 84.3 ms: 1.05x slower                                                       |
| typing_runtime_protocols  | 159 us                                                 | 168 us: 1.05x slower                                                        |
| generators                | 28.8 ms                                                | 30.4 ms: 1.06x slower                                                       |
| scimark_sor               | 122 ms                                                 | 130 ms: 1.06x slower                                                        |
| dulwich_log               | 63.0 ms                                                | 67.2 ms: 1.07x slower                                                       |
| pylint                    | 313 ms                                                 | 335 ms: 1.07x slower                                                        |
| scimark_lu                | 115 ms                                                 | 123 ms: 1.07x slower                                                        |
| hexiom                    | 6.13 ms                                                | 6.58 ms: 1.07x slower                                                       |
| sympy_str                 | 274 ms                                                 | 294 ms: 1.08x slower                                                        |
| genshi_text               | 22.9 ms                                                | 24.6 ms: 1.08x slower                                                       |
| sympy_expand              | 462 ms                                                 | 497 ms: 1.08x slower                                                        |
| dask                      | 338 ms                                                 | 364 ms: 1.08x slower                                                        |
| create_gc_cycles          | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                       |
| docutils                  | 2.58 sec                                               | 2.87 sec: 1.11x slower                                                      |
| sympy_integrate           | 19.9 ms                                                | 22.1 ms: 1.11x slower                                                       |
| coverage                  | 83.7 ms                                                | 93.4 ms: 1.12x slower                                                       |
| genshi_xml                | 50.3 ms                                                | 56.3 ms: 1.12x slower                                                       |
| sympy_sum                 | 150 ms                                                 | 167 ms: 1.12x slower                                                        |
| deltablue                 | 3.15 ms                                                | 3.54 ms: 1.12x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, chaos, async_tree_io, bench_mp_pool, asyncio_websockets, mdp, thrift
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 71.03% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x