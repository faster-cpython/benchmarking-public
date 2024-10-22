# Results vs. 3.13.0

- fork: python
- ref: 0b0f7befaddb2b5eff28
- machine: linux-x86_64
- commit hash: 0b0f7be
- commit date: 2024-08-23
- overall geometric mean: 1.02x faster
- HPT reliability: 99.46%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 254 ms: 1.04x faster                                                  |
| docutils       | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                |
| html5lib       | 64.5 ms                                                | 65.6 ms: 1.02x slower                                                 |
| tornado_http   | 91.5 ms                                                | 90.4 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 402 ms: 1.16x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 391 ms: 1.13x faster                                                  |
| async_tree_none           | 354 ms                                                 | 322 ms: 1.10x faster                                                  |
| async_tree_none_tg        | 320 ms                                                 | 307 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 555 ms: 1.03x faster                                                  |
| asyncio_tcp               | 488 ms                                                 | 482 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                |
| coroutines                | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                 |
| async_tree_io_tg          | 825 ms                                                 | 895 ms: 1.08x slower                                                  |
| async_tree_io             | 843 ms                                                 | 930 ms: 1.10x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 77.3 ms: 1.01x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| nbody          | 85.7 ms                                                | 86.9 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.63 ms: 1.07x faster                                                 |
| regex_v8       | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                 |
| regex_compile  | 131 ms                                                 | 128 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 58.4 ms: 1.03x faster                                                 |
| xml_etree_generate   | 87.0 ms                                                | 84.5 ms: 1.03x faster                                                 |
| tomli_loads          | 2.11 sec                                               | 2.07 sec: 1.02x faster                                                |
| xml_etree_parse      | 156 ms                                                 | 155 ms: 1.01x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 212 us: 1.01x faster                                                  |
| pickle_pure_python   | 300 us                                                 | 302 us: 1.01x slower                                                  |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.03x slower                                                  |
| json_loads           | 27.0 us                                                | 28.3 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 22.6 ms: 1.01x faster                                                 |
| genshi_xml      | 50.3 ms                                                | 49.8 ms: 1.01x faster                                                 |
| django_template | 34.4 ms                                                | 34.1 ms: 1.01x faster                                                 |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 259 us: 1.36x faster                                                  |
| deepcopy_memo             | 38.0 us                                                | 29.6 us: 1.28x faster                                                 |
| deepcopy_reduce           | 3.17 us                                                | 2.67 us: 1.19x faster                                                 |
| async_tree_memoization_tg | 465 ms                                                 | 402 ms: 1.16x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 391 ms: 1.13x faster                                                  |
| async_tree_none           | 354 ms                                                 | 322 ms: 1.10x faster                                                  |
| pathlib                   | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                 |
| regex_effbot              | 3.88 ms                                                | 3.63 ms: 1.07x faster                                                 |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.72 ms: 1.06x faster                                                 |
| mdp                       | 2.74 sec                                               | 2.58 sec: 1.06x faster                                                |
| richards_super            | 54.4 ms                                                | 52.1 ms: 1.04x faster                                                 |
| richards                  | 48.1 ms                                                | 46.1 ms: 1.04x faster                                                 |
| async_tree_none_tg        | 320 ms                                                 | 307 ms: 1.04x faster                                                  |
| 2to3                      | 265 ms                                                 | 254 ms: 1.04x faster                                                  |
| pycparser                 | 1.19 sec                                               | 1.15 sec: 1.04x faster                                                |
| spectral_norm             | 115 ms                                                 | 110 ms: 1.04x faster                                                  |
| bench_thread_pool         | 815 us                                                 | 785 us: 1.04x faster                                                  |
| telco                     | 8.45 ms                                                | 8.15 ms: 1.04x faster                                                 |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 555 ms: 1.03x faster                                                  |
| xml_etree_process         | 60.4 ms                                                | 58.4 ms: 1.03x faster                                                 |
| generators                | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                 |
| pprint_safe_repr          | 744 ms                                                 | 722 ms: 1.03x faster                                                  |
| regex_v8                  | 25.3 ms                                                | 24.5 ms: 1.03x faster                                                 |
| xml_etree_generate        | 87.0 ms                                                | 84.5 ms: 1.03x faster                                                 |
| logging_simple            | 5.66 us                                                | 5.51 us: 1.03x faster                                                 |
| scimark_fft               | 369 ms                                                 | 358 ms: 1.03x faster                                                  |
| sympy_str                 | 274 ms                                                 | 266 ms: 1.03x faster                                                  |
| thrift                    | 796 us                                                 | 777 us: 1.02x faster                                                  |
| pprint_pformat            | 1.51 sec                                               | 1.48 sec: 1.02x faster                                                |
| nqueens                   | 80.6 ms                                                | 78.8 ms: 1.02x faster                                                 |
| gc_traversal              | 3.81 ms                                                | 3.72 ms: 1.02x faster                                                 |
| scimark_lu                | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| regex_compile             | 131 ms                                                 | 128 ms: 1.02x faster                                                  |
| sympy_sum                 | 150 ms                                                 | 147 ms: 1.02x faster                                                  |
| tomli_loads               | 2.11 sec                                               | 2.07 sec: 1.02x faster                                                |
| sympy_integrate           | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                 |
| sympy_expand              | 462 ms                                                 | 454 ms: 1.02x faster                                                  |
| logging_silent            | 102 ns                                                 | 101 ns: 1.01x faster                                                  |
| float                     | 78.5 ms                                                | 77.3 ms: 1.01x faster                                                 |
| crypto_pyaes              | 73.0 ms                                                | 71.9 ms: 1.01x faster                                                 |
| logging_format            | 6.25 us                                                | 6.17 us: 1.01x faster                                                 |
| asyncio_tcp               | 488 ms                                                 | 482 ms: 1.01x faster                                                  |
| tornado_http              | 91.5 ms                                                | 90.4 ms: 1.01x faster                                                 |
| genshi_text               | 22.9 ms                                                | 22.6 ms: 1.01x faster                                                 |
| genshi_xml                | 50.3 ms                                                | 49.8 ms: 1.01x faster                                                 |
| django_template           | 34.4 ms                                                | 34.1 ms: 1.01x faster                                                 |
| sqlglot_optimize          | 53.9 ms                                                | 53.4 ms: 1.01x faster                                                 |
| xml_etree_parse           | 156 ms                                                 | 155 ms: 1.01x faster                                                  |
| json_dumps                | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| raytrace                  | 262 ms                                                 | 260 ms: 1.01x faster                                                  |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| unpickle_pure_python      | 213 us                                                 | 212 us: 1.01x faster                                                  |
| comprehensions            | 16.4 us                                                | 16.3 us: 1.00x faster                                                 |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| sqlglot_normalize         | 107 ms                                                 | 108 ms: 1.00x slower                                                  |
| pickle_pure_python        | 300 us                                                 | 302 us: 1.01x slower                                                  |
| sqlglot_parse             | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                 |
| deltablue                 | 3.15 ms                                                | 3.18 ms: 1.01x slower                                                 |
| python_startup_no_site    | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                 |
| nbody                     | 85.7 ms                                                | 86.9 ms: 1.01x slower                                                 |
| coroutines                | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                 |
| coverage                  | 83.7 ms                                                | 85.1 ms: 1.02x slower                                                 |
| html5lib                  | 64.5 ms                                                | 65.6 ms: 1.02x slower                                                 |
| scimark_monte_carlo       | 66.3 ms                                                | 67.6 ms: 1.02x slower                                                 |
| mako                      | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                 |
| pyflate                   | 460 ms                                                 | 470 ms: 1.02x slower                                                  |
| json                      | 5.20 ms                                                | 5.32 ms: 1.02x slower                                                 |
| bpe_tokeniser             | 4.69 sec                                               | 4.81 sec: 1.02x slower                                                |
| xml_etree_iterparse       | 102 ms                                                 | 105 ms: 1.03x slower                                                  |
| scimark_sor               | 122 ms                                                 | 126 ms: 1.03x slower                                                  |
| docutils                  | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                |
| fannkuch                  | 381 ms                                                 | 398 ms: 1.05x slower                                                  |
| json_loads                | 27.0 us                                                | 28.3 us: 1.05x slower                                                 |
| async_tree_io_tg          | 825 ms                                                 | 895 ms: 1.08x slower                                                  |
| create_gc_cycles          | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                 |
| async_tree_io             | 843 ms                                                 | 930 ms: 1.10x slower                                                  |
| go                        | 142 ms                                                 | 161 ms: 1.14x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed_tg, typing_runtime_protocols, meteor_contest, sqlglot_transpile, async_generators, bench_mp_pool, hexiom, regex_dna, asyncio_websockets, chaos, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x