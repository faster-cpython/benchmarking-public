# Results vs. 3.13.0

- fork: brandtbucher
- ref: tracing_jumps
- machine: linux-x86_64
- commit hash: 84bca09
- commit date: 2024-07-17
- overall geometric mean: 1.01x faster
- HPT reliability: 50.26%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 275 ms: 1.04x slower                                                 |
| docutils       | 2.58 sec                                               | 2.88 sec: 1.11x slower                                               |
| html5lib       | 64.5 ms                                                | 63.3 ms: 1.02x faster                                                |
| tornado_http   | 91.5 ms                                                | 93.2 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.04x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 378 ms: 1.23x faster                                                 |
| async_tree_none           | 354 ms                                                 | 325 ms: 1.09x faster                                                 |
| async_tree_memoization    | 442 ms                                                 | 407 ms: 1.09x faster                                                 |
| async_tree_none_tg        | 320 ms                                                 | 300 ms: 1.07x faster                                                 |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 564 ms: 1.02x faster                                                 |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                               |
| async_tree_io_tg          | 825 ms                                                 | 844 ms: 1.02x slower                                                 |
| coroutines                | 22.5 ms                                                | 23.1 ms: 1.02x slower                                                |
| asyncio_tcp               | 488 ms                                                 | 504 ms: 1.03x slower                                                 |
| async_generators          | 433 ms                                                 | 450 ms: 1.04x slower                                                 |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.2 ms: 1.12x faster                                                |
| nbody          | 85.7 ms                                                | 79.5 ms: 1.08x faster                                                |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.82 ms: 1.02x faster                                                |
| regex_v8       | 25.3 ms                                                | 25.7 ms: 1.02x slower                                                |
| regex_compile  | 131 ms                                                 | 134 ms: 1.02x slower                                                 |
| regex_dna      | 220 ms                                                 | 226 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 79.6 ms: 1.09x faster                                                |
| tomli_loads          | 2.11 sec                                               | 1.95 sec: 1.08x faster                                               |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                 |
| xml_etree_process    | 60.4 ms                                                | 56.8 ms: 1.06x faster                                                |
| xml_etree_iterparse  | 102 ms                                                 | 98.6 ms: 1.03x faster                                                |
| pickle_pure_python   | 300 us                                                 | 293 us: 1.02x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                 |
| json_loads           | 27.0 us                                                | 27.6 us: 1.02x slower                                                |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                |
| python_startup_no_site | 6.99 ms                                                | 7.14 ms: 1.02x slower                                                |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.82 ms: 1.13x faster                                                |
| django_template | 34.4 ms                                                | 35.6 ms: 1.04x slower                                                |
| genshi_text     | 22.9 ms                                                | 23.9 ms: 1.04x slower                                                |
| genshi_xml      | 50.3 ms                                                | 53.4 ms: 1.06x slower                                                |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                         |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 28.7 us: 1.32x faster                                                |
| deepcopy                  | 352 us                                                 | 276 us: 1.28x faster                                                 |
| async_tree_memoization_tg | 465 ms                                                 | 378 ms: 1.23x faster                                                 |
| scimark_fft               | 369 ms                                                 | 309 ms: 1.19x faster                                                 |
| richards                  | 48.1 ms                                                | 41.3 ms: 1.17x faster                                                |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.35 ms: 1.16x faster                                                |
| richards_super            | 54.4 ms                                                | 47.2 ms: 1.15x faster                                                |
| deepcopy_reduce           | 3.17 us                                                | 2.77 us: 1.14x faster                                                |
| spectral_norm             | 115 ms                                                 | 101 ms: 1.14x faster                                                 |
| mako                      | 11.1 ms                                                | 9.82 ms: 1.13x faster                                                |
| float                     | 78.5 ms                                                | 70.2 ms: 1.12x faster                                                |
| xml_etree_generate        | 87.0 ms                                                | 79.6 ms: 1.09x faster                                                |
| async_tree_none           | 354 ms                                                 | 325 ms: 1.09x faster                                                 |
| scimark_monte_carlo       | 66.3 ms                                                | 60.9 ms: 1.09x faster                                                |
| async_tree_memoization    | 442 ms                                                 | 407 ms: 1.09x faster                                                 |
| tomli_loads               | 2.11 sec                                               | 1.95 sec: 1.08x faster                                               |
| nbody                     | 85.7 ms                                                | 79.5 ms: 1.08x faster                                                |
| pathlib                   | 17.1 ms                                                | 15.9 ms: 1.08x faster                                                |
| crypto_pyaes              | 73.0 ms                                                | 67.9 ms: 1.07x faster                                                |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                 |
| async_tree_none_tg        | 320 ms                                                 | 300 ms: 1.07x faster                                                 |
| xml_etree_process         | 60.4 ms                                                | 56.8 ms: 1.06x faster                                                |
| fannkuch                  | 381 ms                                                 | 360 ms: 1.06x faster                                                 |
| pyflate                   | 460 ms                                                 | 434 ms: 1.06x faster                                                 |
| telco                     | 8.45 ms                                                | 8.03 ms: 1.05x faster                                                |
| gc_traversal              | 3.81 ms                                                | 3.66 ms: 1.04x faster                                                |
| xml_etree_iterparse       | 102 ms                                                 | 98.6 ms: 1.03x faster                                                |
| pprint_safe_repr          | 744 ms                                                 | 720 ms: 1.03x faster                                                 |
| logging_simple            | 5.66 us                                                | 5.49 us: 1.03x faster                                                |
| pprint_pformat            | 1.51 sec                                               | 1.47 sec: 1.03x faster                                               |
| pickle_pure_python        | 300 us                                                 | 293 us: 1.02x faster                                                 |
| logging_format            | 6.25 us                                                | 6.12 us: 1.02x faster                                                |
| html5lib                  | 64.5 ms                                                | 63.3 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 564 ms: 1.02x faster                                                 |
| regex_effbot              | 3.88 ms                                                | 3.82 ms: 1.02x faster                                                |
| chaos                     | 58.4 ms                                                | 57.5 ms: 1.02x faster                                                |
| comprehensions            | 16.4 us                                                | 16.2 us: 1.01x faster                                                |
| json_dumps                | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.01x faster                                                 |
| pycparser                 | 1.19 sec                                               | 1.18 sec: 1.01x faster                                               |
| pidigits                  | 186 ms                                                 | 185 ms: 1.00x faster                                                 |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                |
| mdp                       | 2.74 sec                                               | 2.73 sec: 1.00x faster                                               |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                               |
| bench_thread_pool         | 815 us                                                 | 828 us: 1.02x slower                                                 |
| regex_v8                  | 25.3 ms                                                | 25.7 ms: 1.02x slower                                                |
| unpickle_pure_python      | 213 us                                                 | 217 us: 1.02x slower                                                 |
| tornado_http              | 91.5 ms                                                | 93.2 ms: 1.02x slower                                                |
| sqlglot_parse             | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                |
| regex_compile             | 131 ms                                                 | 134 ms: 1.02x slower                                                 |
| python_startup_no_site    | 6.99 ms                                                | 7.14 ms: 1.02x slower                                                |
| async_tree_io_tg          | 825 ms                                                 | 844 ms: 1.02x slower                                                 |
| json_loads                | 27.0 us                                                | 27.6 us: 1.02x slower                                                |
| bpe_tokeniser             | 4.69 sec                                               | 4.81 sec: 1.02x slower                                               |
| coroutines                | 22.5 ms                                                | 23.1 ms: 1.02x slower                                                |
| go                        | 142 ms                                                 | 145 ms: 1.03x slower                                                 |
| sqlglot_transpile         | 1.57 ms                                                | 1.62 ms: 1.03x slower                                                |
| sqlglot_optimize          | 53.9 ms                                                | 55.4 ms: 1.03x slower                                                |
| regex_dna                 | 220 ms                                                 | 226 ms: 1.03x slower                                                 |
| asyncio_tcp               | 488 ms                                                 | 504 ms: 1.03x slower                                                 |
| django_template           | 34.4 ms                                                | 35.6 ms: 1.04x slower                                                |
| 2to3                      | 265 ms                                                 | 275 ms: 1.04x slower                                                 |
| raytrace                  | 262 ms                                                 | 272 ms: 1.04x slower                                                 |
| async_generators          | 433 ms                                                 | 450 ms: 1.04x slower                                                 |
| genshi_text               | 22.9 ms                                                | 23.9 ms: 1.04x slower                                                |
| scimark_sor               | 122 ms                                                 | 129 ms: 1.05x slower                                                 |
| sqlglot_normalize         | 107 ms                                                 | 113 ms: 1.05x slower                                                 |
| logging_silent            | 102 ns                                                 | 108 ns: 1.05x slower                                                 |
| genshi_xml                | 50.3 ms                                                | 53.4 ms: 1.06x slower                                                |
| scimark_lu                | 115 ms                                                 | 122 ms: 1.06x slower                                                 |
| nqueens                   | 80.6 ms                                                | 85.6 ms: 1.06x slower                                                |
| typing_runtime_protocols  | 159 us                                                 | 170 us: 1.06x slower                                                 |
| dask                      | 338 ms                                                 | 361 ms: 1.07x slower                                                 |
| sympy_expand              | 462 ms                                                 | 496 ms: 1.08x slower                                                 |
| sympy_str                 | 274 ms                                                 | 295 ms: 1.08x slower                                                 |
| pylint                    | 313 ms                                                 | 338 ms: 1.08x slower                                                 |
| dulwich_log               | 63.0 ms                                                | 68.3 ms: 1.08x slower                                                |
| hexiom                    | 6.13 ms                                                | 6.68 ms: 1.09x slower                                                |
| create_gc_cycles          | 1.61 ms                                                | 1.76 ms: 1.09x slower                                                |
| sympy_sum                 | 150 ms                                                 | 165 ms: 1.11x slower                                                 |
| docutils                  | 2.58 sec                                               | 2.88 sec: 1.11x slower                                               |
| coverage                  | 83.7 ms                                                | 93.6 ms: 1.12x slower                                                |
| sympy_integrate           | 19.9 ms                                                | 22.3 ms: 1.12x slower                                                |
| deltablue                 | 3.15 ms                                                | 3.65 ms: 1.16x slower                                                |
| generators                | 28.8 ms                                                | 45.4 ms: 1.57x slower                                                |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (6): json, thrift, async_tree_cpu_io_mixed_tg, bench_mp_pool, async_tree_io, asyncio_websockets
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 50.26% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x