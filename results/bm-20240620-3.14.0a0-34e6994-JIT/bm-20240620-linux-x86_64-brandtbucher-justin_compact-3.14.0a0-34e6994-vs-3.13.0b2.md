# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_compact
- machine: linux-x86_64
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.03x faster
- HPT reliability: 99.86%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 273 ms: 1.00x faster                                                  |
| docutils       | 2.83 sec                                                   | 2.87 sec: 1.02x slower                                                |
| html5lib       | 67.2 ms                                                    | 66.8 ms: 1.01x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 94.0 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.00x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 364 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 567 ms: 1.04x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 483 ms: 1.04x slower                                                  |
| async_tree_io_tg           | 936 ms                                                     | 990 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (4): async_tree_io, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.8 ms: 1.13x faster                                                 |
| nbody          | 88.3 ms                                                    | 80.3 ms: 1.10x faster                                                 |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                      | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 23.8 ms: 1.05x faster                                                 |
| regex_compile  | 137 ms                                                     | 135 ms: 1.01x faster                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.66 ms: 1.00x faster                                                 |
| regex_dna      | 221 ms                                                     | 223 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                  |
| tomli_loads          | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                |
| xml_etree_generate   | 87.4 ms                                                    | 80.4 ms: 1.09x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 99.9 ms: 1.07x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 57.2 ms: 1.07x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                 |
| unpickle_list        | 5.34 us                                                    | 5.12 us: 1.04x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 297 us: 1.03x faster                                                  |
| pickle_list          | 5.11 us                                                    | 4.99 us: 1.02x faster                                                 |
| json_loads           | 28.9 us                                                    | 28.3 us: 1.02x faster                                                 |
| unpickle             | 15.1 us                                                    | 15.0 us: 1.01x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 217 us: 1.01x faster                                                  |
| pickle_dict          | 34.8 us                                                    | 35.2 us: 1.01x slower                                                 |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.04x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.9 ms: 1.01x slower                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.43 ms: 1.05x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.03x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.70 ms: 1.16x faster                                                 |
| django_template | 34.8 ms                                                    | 36.3 ms: 1.04x slower                                                 |
| genshi_text     | 23.7 ms                                                    | 24.9 ms: 1.05x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 57.4 ms: 1.11x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.8 us: 1.38x faster                                                 |
| deepcopy                   | 367 us                                                     | 278 us: 1.32x faster                                                  |
| scimark_fft                | 392 ms                                                     | 318 ms: 1.23x faster                                                  |
| richards                   | 50.9 ms                                                    | 41.5 ms: 1.23x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.75 us: 1.22x faster                                                 |
| richards_super             | 57.4 ms                                                    | 47.7 ms: 1.20x faster                                                 |
| mako                       | 11.2 ms                                                    | 9.70 ms: 1.16x faster                                                 |
| fannkuch                   | 402 ms                                                     | 348 ms: 1.15x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 67.4 ms: 1.15x faster                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.61 ms: 1.14x faster                                                 |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.13x faster                                                  |
| float                      | 78.9 ms                                                    | 69.8 ms: 1.13x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                  |
| pyflate                    | 484 ms                                                     | 438 ms: 1.10x faster                                                  |
| nbody                      | 88.3 ms                                                    | 80.3 ms: 1.10x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.2 ms: 1.09x faster                                                 |
| tomli_loads                | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                |
| xml_etree_generate         | 87.4 ms                                                    | 80.4 ms: 1.09x faster                                                 |
| mdp                        | 2.79 sec                                                   | 2.56 sec: 1.09x faster                                                |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                                 |
| pprint_pformat             | 1.56 sec                                                   | 1.44 sec: 1.08x faster                                                |
| xml_etree_iterparse        | 107 ms                                                     | 99.9 ms: 1.07x faster                                                 |
| pprint_safe_repr           | 758 ms                                                     | 707 ms: 1.07x faster                                                  |
| xml_etree_process          | 61.2 ms                                                    | 57.2 ms: 1.07x faster                                                 |
| gc_traversal               | 3.98 ms                                                    | 3.73 ms: 1.07x faster                                                 |
| telco                      | 8.41 ms                                                    | 7.89 ms: 1.07x faster                                                 |
| logging_format             | 6.47 us                                                    | 6.08 us: 1.07x faster                                                 |
| sqlite_synth               | 2.99 us                                                    | 2.82 us: 1.06x faster                                                 |
| regex_v8                   | 25.1 ms                                                    | 23.8 ms: 1.05x faster                                                 |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                 |
| chaos                      | 61.3 ms                                                    | 58.6 ms: 1.05x faster                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.81 sec: 1.04x faster                                                |
| unpickle_list              | 5.34 us                                                    | 5.12 us: 1.04x faster                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.04x faster                                                 |
| async_tree_none            | 378 ms                                                     | 364 ms: 1.04x faster                                                  |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                  |
| logging_simple             | 5.74 us                                                    | 5.54 us: 1.04x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 567 ms: 1.04x faster                                                  |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                 |
| asyncio_tcp                | 508 ms                                                     | 493 ms: 1.03x faster                                                  |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| pickle_pure_python         | 305 us                                                     | 297 us: 1.03x faster                                                  |
| pycparser                  | 1.16 sec                                                   | 1.13 sec: 1.03x faster                                                |
| pickle_list                | 5.11 us                                                    | 4.99 us: 1.02x faster                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                                 |
| json_loads                 | 28.9 us                                                    | 28.3 us: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.60 ms: 1.02x faster                                                 |
| regex_compile              | 137 ms                                                     | 135 ms: 1.01x faster                                                  |
| thrift                     | 823 us                                                     | 811 us: 1.01x faster                                                  |
| unpickle                   | 15.1 us                                                    | 15.0 us: 1.01x faster                                                 |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                 |
| tornado_http               | 94.6 ms                                                    | 94.0 ms: 1.01x faster                                                 |
| html5lib                   | 67.2 ms                                                    | 66.8 ms: 1.01x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 217 us: 1.01x faster                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.66 ms: 1.00x faster                                                 |
| bench_thread_pool          | 834 us                                                     | 831 us: 1.00x faster                                                  |
| 2to3                       | 274 ms                                                     | 273 ms: 1.00x faster                                                  |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| regex_dna                  | 221 ms                                                     | 223 ms: 1.01x slower                                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 56.1 ms: 1.01x slower                                                 |
| scimark_sor                | 127 ms                                                     | 129 ms: 1.01x slower                                                  |
| logging_silent             | 105 ns                                                     | 106 ns: 1.01x slower                                                  |
| pickle_dict                | 34.8 us                                                    | 35.2 us: 1.01x slower                                                 |
| python_startup             | 10.8 ms                                                    | 10.9 ms: 1.01x slower                                                 |
| dulwich_log                | 67.2 ms                                                    | 68.0 ms: 1.01x slower                                                 |
| docutils                   | 2.83 sec                                                   | 2.87 sec: 1.02x slower                                                |
| raytrace                   | 267 ms                                                     | 273 ms: 1.02x slower                                                  |
| pickle                     | 11.5 us                                                    | 11.7 us: 1.02x slower                                                 |
| scimark_lu                 | 122 ms                                                     | 125 ms: 1.02x slower                                                  |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.03x slower                                                  |
| typing_runtime_protocols   | 165 us                                                     | 169 us: 1.03x slower                                                  |
| hexiom                     | 6.30 ms                                                    | 6.52 ms: 1.04x slower                                                 |
| async_generators           | 442 ms                                                     | 458 ms: 1.04x slower                                                  |
| async_tree_memoization     | 463 ms                                                     | 483 ms: 1.04x slower                                                  |
| django_template            | 34.8 ms                                                    | 36.3 ms: 1.04x slower                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.43 ms: 1.05x slower                                                 |
| sympy_str                  | 282 ms                                                     | 296 ms: 1.05x slower                                                  |
| nqueens                    | 81.4 ms                                                    | 85.5 ms: 1.05x slower                                                 |
| genshi_text                | 23.7 ms                                                    | 24.9 ms: 1.05x slower                                                 |
| async_tree_io_tg           | 936 ms                                                     | 990 ms: 1.06x slower                                                  |
| sympy_expand               | 473 ms                                                     | 500 ms: 1.06x slower                                                  |
| sympy_integrate            | 20.5 ms                                                    | 22.0 ms: 1.07x slower                                                 |
| sympy_sum                  | 156 ms                                                     | 167 ms: 1.07x slower                                                  |
| pylint                     | 317 ms                                                     | 343 ms: 1.08x slower                                                  |
| deltablue                  | 3.25 ms                                                    | 3.55 ms: 1.09x slower                                                 |
| genshi_xml                 | 51.6 ms                                                    | 57.4 ms: 1.11x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                          |

Benchmark hidden because not significant (9): dask, async_tree_io, async_tree_cpu_io_mixed, generators, json, go, async_tree_none_tg, coverage, async_tree_memoization_tg
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.86% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x