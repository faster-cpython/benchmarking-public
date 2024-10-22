# Results vs. 3.13.0

- fork: brandtbucher
- ref: tracing_jumps
- machine: linux-x86_64
- commit hash: 6590af5
- commit date: 2024-07-18
- overall geometric mean: 1.01x faster
- HPT reliability: 62.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 275 ms: 1.04x slower                                                 |
| docutils       | 2.58 sec                                               | 2.88 sec: 1.11x slower                                               |
| html5lib       | 64.5 ms                                                | 65.9 ms: 1.02x slower                                                |
| tornado_http   | 91.5 ms                                                | 92.5 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.04x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 377 ms: 1.23x faster                                                 |
| async_tree_none_tg        | 320 ms                                                 | 298 ms: 1.08x faster                                                 |
| async_tree_none           | 354 ms                                                 | 330 ms: 1.07x faster                                                 |
| async_tree_memoization    | 442 ms                                                 | 413 ms: 1.07x faster                                                 |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                 |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                               |
| asyncio_tcp               | 488 ms                                                 | 498 ms: 1.02x slower                                                 |
| async_tree_io_tg          | 825 ms                                                 | 844 ms: 1.02x slower                                                 |
| async_generators          | 433 ms                                                 | 451 ms: 1.04x slower                                                 |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, coroutines, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.8 ms: 1.09x faster                                                |
| nbody          | 85.7 ms                                                | 82.4 ms: 1.04x faster                                                |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.87 ms: 1.00x faster                                                |
| regex_v8       | 25.3 ms                                                | 25.4 ms: 1.00x slower                                                |
| regex_compile  | 131 ms                                                 | 132 ms: 1.01x slower                                                 |
| regex_dna      | 220 ms                                                 | 228 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.91 sec: 1.11x faster                                               |
| xml_etree_generate   | 87.0 ms                                                | 79.9 ms: 1.09x faster                                                |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                 |
| xml_etree_process    | 60.4 ms                                                | 56.8 ms: 1.06x faster                                                |
| xml_etree_iterparse  | 102 ms                                                 | 98.9 ms: 1.03x faster                                                |
| pickle_pure_python   | 300 us                                                 | 295 us: 1.02x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                 |
| json_loads           | 27.0 us                                                | 27.4 us: 1.02x slower                                                |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                         |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                |
| python_startup_no_site | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.65 ms: 1.15x faster                                                |
| django_template | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                |
| genshi_text     | 22.9 ms                                                | 24.0 ms: 1.05x slower                                                |
| genshi_xml      | 50.3 ms                                                | 53.5 ms: 1.06x slower                                                |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                         |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-6590af5 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 29.2 us: 1.30x faster                                                |
| deepcopy                  | 352 us                                                 | 276 us: 1.28x faster                                                 |
| async_tree_memoization_tg | 465 ms                                                 | 377 ms: 1.23x faster                                                 |
| richards                  | 48.1 ms                                                | 40.8 ms: 1.18x faster                                                |
| richards_super            | 54.4 ms                                                | 46.5 ms: 1.17x faster                                                |
| scimark_fft               | 369 ms                                                 | 316 ms: 1.17x faster                                                 |
| deepcopy_reduce           | 3.17 us                                                | 2.74 us: 1.15x faster                                                |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.35 ms: 1.15x faster                                                |
| mako                      | 11.1 ms                                                | 9.65 ms: 1.15x faster                                                |
| spectral_norm             | 115 ms                                                 | 102 ms: 1.12x faster                                                 |
| tomli_loads               | 2.11 sec                                               | 1.91 sec: 1.11x faster                                               |
| scimark_monte_carlo       | 66.3 ms                                                | 60.4 ms: 1.10x faster                                                |
| crypto_pyaes              | 73.0 ms                                                | 66.7 ms: 1.09x faster                                                |
| float                     | 78.5 ms                                                | 71.8 ms: 1.09x faster                                                |
| pyflate                   | 460 ms                                                 | 421 ms: 1.09x faster                                                 |
| xml_etree_generate        | 87.0 ms                                                | 79.9 ms: 1.09x faster                                                |
| async_tree_none_tg        | 320 ms                                                 | 298 ms: 1.08x faster                                                 |
| async_tree_none           | 354 ms                                                 | 330 ms: 1.07x faster                                                 |
| async_tree_memoization    | 442 ms                                                 | 413 ms: 1.07x faster                                                 |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                 |
| pathlib                   | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                |
| fannkuch                  | 381 ms                                                 | 358 ms: 1.06x faster                                                 |
| xml_etree_process         | 60.4 ms                                                | 56.8 ms: 1.06x faster                                                |
| mdp                       | 2.74 sec                                               | 2.61 sec: 1.05x faster                                               |
| telco                     | 8.45 ms                                                | 8.08 ms: 1.05x faster                                                |
| nbody                     | 85.7 ms                                                | 82.4 ms: 1.04x faster                                                |
| logging_format            | 6.25 us                                                | 6.03 us: 1.04x faster                                                |
| logging_simple            | 5.66 us                                                | 5.48 us: 1.03x faster                                                |
| meteor_contest            | 108 ms                                                 | 104 ms: 1.03x faster                                                 |
| xml_etree_iterparse       | 102 ms                                                 | 98.9 ms: 1.03x faster                                                |
| pprint_safe_repr          | 744 ms                                                 | 724 ms: 1.03x faster                                                 |
| gc_traversal              | 3.81 ms                                                | 3.71 ms: 1.03x faster                                                |
| bpe_tokeniser             | 4.69 sec                                               | 4.57 sec: 1.03x faster                                               |
| pycparser                 | 1.19 sec                                               | 1.17 sec: 1.02x faster                                               |
| pickle_pure_python        | 300 us                                                 | 295 us: 1.02x faster                                                 |
| pprint_pformat            | 1.51 sec                                               | 1.49 sec: 1.01x faster                                               |
| chaos                     | 58.4 ms                                                | 58.0 ms: 1.01x faster                                                |
| regex_effbot              | 3.88 ms                                                | 3.87 ms: 1.00x faster                                                |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                 |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                |
| regex_v8                  | 25.3 ms                                                | 25.4 ms: 1.00x slower                                                |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                 |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                               |
| unpickle_pure_python      | 213 us                                                 | 215 us: 1.01x slower                                                 |
| regex_compile             | 131 ms                                                 | 132 ms: 1.01x slower                                                 |
| thrift                    | 796 us                                                 | 803 us: 1.01x slower                                                 |
| tornado_http              | 91.5 ms                                                | 92.5 ms: 1.01x slower                                                |
| bench_thread_pool         | 815 us                                                 | 826 us: 1.01x slower                                                 |
| json_loads                | 27.0 us                                                | 27.4 us: 1.02x slower                                                |
| go                        | 142 ms                                                 | 144 ms: 1.02x slower                                                 |
| sqlglot_parse             | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                |
| asyncio_tcp               | 488 ms                                                 | 498 ms: 1.02x slower                                                 |
| html5lib                  | 64.5 ms                                                | 65.9 ms: 1.02x slower                                                |
| async_tree_io_tg          | 825 ms                                                 | 844 ms: 1.02x slower                                                 |
| sqlglot_optimize          | 53.9 ms                                                | 55.3 ms: 1.02x slower                                                |
| python_startup_no_site    | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                |
| raytrace                  | 262 ms                                                 | 269 ms: 1.03x slower                                                 |
| sqlglot_transpile         | 1.57 ms                                                | 1.62 ms: 1.03x slower                                                |
| 2to3                      | 265 ms                                                 | 275 ms: 1.04x slower                                                 |
| nqueens                   | 80.6 ms                                                | 83.8 ms: 1.04x slower                                                |
| regex_dna                 | 220 ms                                                 | 228 ms: 1.04x slower                                                 |
| logging_silent            | 102 ns                                                 | 106 ns: 1.04x slower                                                 |
| async_generators          | 433 ms                                                 | 451 ms: 1.04x slower                                                 |
| sqlglot_normalize         | 107 ms                                                 | 112 ms: 1.04x slower                                                 |
| django_template           | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                |
| genshi_text               | 22.9 ms                                                | 24.0 ms: 1.05x slower                                                |
| scimark_sor               | 122 ms                                                 | 129 ms: 1.05x slower                                                 |
| genshi_xml                | 50.3 ms                                                | 53.5 ms: 1.06x slower                                                |
| dask                      | 338 ms                                                 | 363 ms: 1.07x slower                                                 |
| typing_runtime_protocols  | 159 us                                                 | 171 us: 1.08x slower                                                 |
| dulwich_log               | 63.0 ms                                                | 67.8 ms: 1.08x slower                                                |
| pylint                    | 313 ms                                                 | 339 ms: 1.08x slower                                                 |
| scimark_lu                | 115 ms                                                 | 125 ms: 1.08x slower                                                 |
| sympy_expand              | 462 ms                                                 | 501 ms: 1.09x slower                                                 |
| sympy_str                 | 274 ms                                                 | 297 ms: 1.09x slower                                                 |
| coverage                  | 83.7 ms                                                | 90.9 ms: 1.09x slower                                                |
| hexiom                    | 6.13 ms                                                | 6.67 ms: 1.09x slower                                                |
| create_gc_cycles          | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                |
| docutils                  | 2.58 sec                                               | 2.88 sec: 1.11x slower                                               |
| sympy_integrate           | 19.9 ms                                                | 22.4 ms: 1.12x slower                                                |
| sympy_sum                 | 150 ms                                                 | 169 ms: 1.13x slower                                                 |
| deltablue                 | 3.15 ms                                                | 3.57 ms: 1.13x slower                                                |
| generators                | 28.8 ms                                                | 33.0 ms: 1.15x slower                                                |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, comprehensions, json_dumps, bench_mp_pool, coroutines, json, async_tree_io
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 62.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x