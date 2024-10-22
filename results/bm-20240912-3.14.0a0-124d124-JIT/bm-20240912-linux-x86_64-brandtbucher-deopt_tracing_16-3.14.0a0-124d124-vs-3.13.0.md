# Results vs. 3.13.0

- fork: brandtbucher
- ref: deopt_tracing_16
- machine: linux-x86_64
- commit hash: 124d124
- commit date: 2024-09-12
- overall geometric mean: 1.01x slower
- HPT reliability: 62.42%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 283 ms: 1.07x slower                                                    |
| docutils       | 2.58 sec                                               | 2.97 sec: 1.15x slower                                                  |
| html5lib       | 64.5 ms                                                | 65.1 ms: 1.01x slower                                                   |
| tornado_http   | 91.5 ms                                                | 94.7 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 388 ms: 1.20x faster                                                    |
| async_tree_none            | 354 ms                                                 | 314 ms: 1.13x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 396 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 320 ms                                                 | 308 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 566 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 552 ms: 1.02x slower                                                    |
| asyncio_tcp                | 488 ms                                                 | 498 ms: 1.02x slower                                                    |
| async_tree_io              | 843 ms                                                 | 885 ms: 1.05x slower                                                    |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                                    |
| async_tree_io_tg           | 825 ms                                                 | 872 ms: 1.06x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.4 ms: 1.13x faster                                                   |
| nbody          | 85.7 ms                                                | 81.1 ms: 1.06x faster                                                   |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 24.0 ms: 1.05x faster                                                   |
| regex_effbot   | 3.88 ms                                                | 3.78 ms: 1.03x faster                                                   |
| regex_dna      | 220 ms                                                 | 221 ms: 1.01x slower                                                    |
| regex_compile  | 131 ms                                                 | 144 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.6 ms: 1.12x faster                                                   |
| xml_etree_process    | 60.4 ms                                                | 54.5 ms: 1.11x faster                                                   |
| tomli_loads          | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                  |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.08x faster                                                    |
| xml_etree_iterparse  | 102 ms                                                 | 98.7 ms: 1.03x faster                                                   |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                   |
| json_loads           | 27.0 us                                                | 27.4 us: 1.01x slower                                                   |
| pickle_list          | 5.01 us                                                | 5.08 us: 1.02x slower                                                   |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                    |
| pickle_dict          | 33.2 us                                                | 33.8 us: 1.02x slower                                                   |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                   |
| unpickle_list        | 4.96 us                                                | 5.12 us: 1.03x slower                                                   |
| pickle_pure_python   | 300 us                                                 | 313 us: 1.04x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                   |
| python_startup_no_site | 6.99 ms                                                | 7.02 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.71 ms: 1.14x faster                                                   |
| django_template | 34.4 ms                                                | 37.4 ms: 1.09x slower                                                   |
| genshi_text     | 22.9 ms                                                | 25.7 ms: 1.12x slower                                                   |
| genshi_xml      | 50.3 ms                                                | 59.8 ms: 1.19x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.1 us: 1.40x faster                                                   |
| deepcopy                   | 352 us                                                 | 268 us: 1.31x faster                                                    |
| scimark_fft                | 369 ms                                                 | 306 ms: 1.21x faster                                                    |
| async_tree_memoization_tg  | 465 ms                                                 | 388 ms: 1.20x faster                                                    |
| deepcopy_reduce            | 3.17 us                                                | 2.65 us: 1.20x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.33 ms: 1.16x faster                                                   |
| mako                       | 11.1 ms                                                | 9.71 ms: 1.14x faster                                                   |
| float                      | 78.5 ms                                                | 69.4 ms: 1.13x faster                                                   |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                    |
| async_tree_none            | 354 ms                                                 | 314 ms: 1.13x faster                                                    |
| xml_etree_generate         | 87.0 ms                                                | 77.6 ms: 1.12x faster                                                   |
| async_tree_memoization     | 442 ms                                                 | 396 ms: 1.12x faster                                                    |
| xml_etree_process          | 60.4 ms                                                | 54.5 ms: 1.11x faster                                                   |
| crypto_pyaes               | 73.0 ms                                                | 65.9 ms: 1.11x faster                                                   |
| tomli_loads                | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                  |
| mdp                        | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                  |
| xml_etree_parse            | 156 ms                                                 | 145 ms: 1.08x faster                                                    |
| gc_traversal               | 3.81 ms                                                | 3.53 ms: 1.08x faster                                                   |
| telco                      | 8.45 ms                                                | 7.86 ms: 1.08x faster                                                   |
| pathlib                    | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                   |
| richards_super             | 54.4 ms                                                | 51.1 ms: 1.06x faster                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.43 sec: 1.06x faster                                                  |
| nbody                      | 85.7 ms                                                | 81.1 ms: 1.06x faster                                                   |
| scimark_lu                 | 115 ms                                                 | 109 ms: 1.06x faster                                                    |
| regex_v8                   | 25.3 ms                                                | 24.0 ms: 1.05x faster                                                   |
| pyflate                    | 460 ms                                                 | 437 ms: 1.05x faster                                                    |
| scimark_monte_carlo        | 66.3 ms                                                | 63.0 ms: 1.05x faster                                                   |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.05x faster                                                    |
| async_tree_none_tg         | 320 ms                                                 | 308 ms: 1.04x faster                                                    |
| sqlite_synth               | 2.85 us                                                | 2.75 us: 1.04x faster                                                   |
| xml_etree_iterparse        | 102 ms                                                 | 98.7 ms: 1.03x faster                                                   |
| logging_format             | 6.25 us                                                | 6.05 us: 1.03x faster                                                   |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                   |
| richards                   | 48.1 ms                                                | 46.7 ms: 1.03x faster                                                   |
| go                         | 142 ms                                                 | 137 ms: 1.03x faster                                                    |
| regex_effbot               | 3.88 ms                                                | 3.78 ms: 1.03x faster                                                   |
| logging_simple             | 5.66 us                                                | 5.52 us: 1.03x faster                                                   |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.02x faster                                                    |
| fannkuch                   | 381 ms                                                 | 375 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 566 ms: 1.01x faster                                                    |
| json                       | 5.20 ms                                                | 5.14 ms: 1.01x faster                                                   |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                   |
| thrift                     | 796 us                                                 | 791 us: 1.01x faster                                                    |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| python_startup_no_site     | 6.99 ms                                                | 7.02 ms: 1.01x slower                                                   |
| regex_dna                  | 220 ms                                                 | 221 ms: 1.01x slower                                                    |
| html5lib                   | 64.5 ms                                                | 65.1 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| coverage                   | 83.7 ms                                                | 84.6 ms: 1.01x slower                                                   |
| json_loads                 | 27.0 us                                                | 27.4 us: 1.01x slower                                                   |
| pickle_list                | 5.01 us                                                | 5.08 us: 1.02x slower                                                   |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 552 ms: 1.02x slower                                                    |
| pickle_dict                | 33.2 us                                                | 33.8 us: 1.02x slower                                                   |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                                   |
| comprehensions             | 16.4 us                                                | 16.7 us: 1.02x slower                                                   |
| asyncio_tcp                | 488 ms                                                 | 498 ms: 1.02x slower                                                    |
| bench_thread_pool          | 815 us                                                 | 833 us: 1.02x slower                                                    |
| pprint_pformat             | 1.51 sec                                               | 1.55 sec: 1.03x slower                                                  |
| unpickle_list              | 4.96 us                                                | 5.12 us: 1.03x slower                                                   |
| typing_runtime_protocols   | 159 us                                                 | 165 us: 1.03x slower                                                    |
| tornado_http               | 91.5 ms                                                | 94.7 ms: 1.03x slower                                                   |
| pickle_pure_python         | 300 us                                                 | 313 us: 1.04x slower                                                    |
| async_tree_io              | 843 ms                                                 | 885 ms: 1.05x slower                                                    |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                                    |
| async_tree_io_tg           | 825 ms                                                 | 872 ms: 1.06x slower                                                    |
| 2to3                       | 265 ms                                                 | 283 ms: 1.07x slower                                                    |
| nqueens                    | 80.6 ms                                                | 86.5 ms: 1.07x slower                                                   |
| dulwich_log                | 63.0 ms                                                | 68.0 ms: 1.08x slower                                                   |
| sqlglot_parse              | 1.27 ms                                                | 1.37 ms: 1.08x slower                                                   |
| django_template            | 34.4 ms                                                | 37.4 ms: 1.09x slower                                                   |
| sqlglot_transpile          | 1.57 ms                                                | 1.71 ms: 1.09x slower                                                   |
| create_gc_cycles           | 1.61 ms                                                | 1.76 ms: 1.09x slower                                                   |
| raytrace                   | 262 ms                                                 | 286 ms: 1.09x slower                                                    |
| sqlglot_optimize           | 53.9 ms                                                | 59.1 ms: 1.10x slower                                                   |
| regex_compile              | 131 ms                                                 | 144 ms: 1.10x slower                                                    |
| sympy_str                  | 274 ms                                                 | 307 ms: 1.12x slower                                                    |
| genshi_text                | 22.9 ms                                                | 25.7 ms: 1.12x slower                                                   |
| sympy_expand               | 462 ms                                                 | 521 ms: 1.13x slower                                                    |
| sqlglot_normalize          | 107 ms                                                 | 122 ms: 1.14x slower                                                    |
| hexiom                     | 6.13 ms                                                | 7.00 ms: 1.14x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.97 sec: 1.15x slower                                                  |
| deltablue                  | 3.15 ms                                                | 3.66 ms: 1.16x slower                                                   |
| generators                 | 28.8 ms                                                | 33.6 ms: 1.17x slower                                                   |
| sympy_integrate            | 19.9 ms                                                | 23.4 ms: 1.18x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 177 ms: 1.18x slower                                                    |
| genshi_xml                 | 50.3 ms                                                | 59.8 ms: 1.19x slower                                                   |
| pylint                     | 313 ms                                                 | 385 ms: 1.23x slower                                                    |
| unpack_sequence            | 42.4 ns                                                | 110 ns: 2.60x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (8): unpickle, pycparser, chaos, asyncio_websockets, bench_mp_pool, pprint_safe_repr, logging_silent, coroutines
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 62.42% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.11x