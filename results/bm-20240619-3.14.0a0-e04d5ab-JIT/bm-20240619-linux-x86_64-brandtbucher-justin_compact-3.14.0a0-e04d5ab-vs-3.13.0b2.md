# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_compact
- machine: linux-x86_64
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.01x faster
- HPT reliability: 72.42%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 281 ms: 1.03x slower                                                  |
| docutils       | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                |
| tornado_http   | 94.6 ms                                                    | 96.3 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|---------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_cpu_io_mixed   | 611 ms                                                     | 626 ms: 1.03x slower                                                  |
| async_tree_memoization_tg | 444 ms                                                     | 466 ms: 1.05x slower                                                  |
| async_tree_memoization    | 463 ms                                                     | 493 ms: 1.06x slower                                                  |
| async_tree_io_tg          | 936 ms                                                     | 1.01 sec: 1.08x slower                                                |
| Geometric mean            | (ref)                                                      | 1.03x slower                                                          |

Benchmark hidden because not significant (4): async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.8 ms: 1.10x faster                                                 |
| nbody          | 88.3 ms                                                    | 80.8 ms: 1.09x faster                                                 |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                      | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 23.8 ms: 1.06x faster                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.71 ms: 1.01x slower                                                 |
| regex_dna      | 221 ms                                                     | 230 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 149 ms: 1.08x faster                                                  |
| tomli_loads          | 2.12 sec                                                   | 1.97 sec: 1.07x faster                                                |
| xml_etree_generate   | 87.4 ms                                                    | 82.3 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 102 ms: 1.05x faster                                                  |
| xml_etree_process    | 61.2 ms                                                    | 58.3 ms: 1.05x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 301 us: 1.02x faster                                                  |
| json_dumps           | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                                 |
| unpickle             | 15.1 us                                                    | 15.0 us: 1.01x faster                                                 |
| json_loads           | 28.9 us                                                    | 28.7 us: 1.01x faster                                                 |
| pickle_list          | 5.11 us                                                    | 5.12 us: 1.00x slower                                                 |
| unpickle_list        | 5.34 us                                                    | 5.37 us: 1.01x slower                                                 |
| pickle_dict          | 34.8 us                                                    | 35.6 us: 1.02x slower                                                 |
| unpickle_pure_python | 218 us                                                     | 224 us: 1.03x slower                                                  |
| pickle               | 11.5 us                                                    | 12.2 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.1 ms: 1.04x slower                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.63 ms: 1.07x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                                 |
| django_template | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                                 |
| genshi_text     | 23.7 ms                                                    | 24.7 ms: 1.05x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 56.3 ms: 1.09x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|---------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo             | 39.7 us                                                    | 28.8 us: 1.38x faster                                                 |
| deepcopy                  | 367 us                                                     | 277 us: 1.32x faster                                                  |
| scimark_fft               | 392 ms                                                     | 310 ms: 1.27x faster                                                  |
| deepcopy_reduce           | 3.35 us                                                    | 2.77 us: 1.21x faster                                                 |
| scimark_sparse_mat_mult   | 5.27 ms                                                    | 4.43 ms: 1.19x faster                                                 |
| richards                  | 50.9 ms                                                    | 42.8 ms: 1.19x faster                                                 |
| richards_super            | 57.4 ms                                                    | 49.4 ms: 1.16x faster                                                 |
| crypto_pyaes              | 77.5 ms                                                    | 67.1 ms: 1.15x faster                                                 |
| spectral_norm             | 116 ms                                                     | 102 ms: 1.14x faster                                                  |
| fannkuch                  | 402 ms                                                     | 356 ms: 1.13x faster                                                  |
| mako                      | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                                 |
| scimark_monte_carlo       | 69.2 ms                                                    | 62.3 ms: 1.11x faster                                                 |
| float                     | 78.9 ms                                                    | 71.8 ms: 1.10x faster                                                 |
| nbody                     | 88.3 ms                                                    | 80.8 ms: 1.09x faster                                                 |
| pyflate                   | 484 ms                                                     | 445 ms: 1.09x faster                                                  |
| xml_etree_parse           | 162 ms                                                     | 149 ms: 1.08x faster                                                  |
| tomli_loads               | 2.12 sec                                                   | 1.97 sec: 1.07x faster                                                |
| xml_etree_generate        | 87.4 ms                                                    | 82.3 ms: 1.06x faster                                                 |
| pathlib                   | 17.3 ms                                                    | 16.3 ms: 1.06x faster                                                 |
| regex_v8                  | 25.1 ms                                                    | 23.8 ms: 1.06x faster                                                 |
| pprint_pformat            | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                                |
| xml_etree_iterparse       | 107 ms                                                     | 102 ms: 1.05x faster                                                  |
| pprint_safe_repr          | 758 ms                                                     | 722 ms: 1.05x faster                                                  |
| xml_etree_process         | 61.2 ms                                                    | 58.3 ms: 1.05x faster                                                 |
| logging_format            | 6.47 us                                                    | 6.17 us: 1.05x faster                                                 |
| telco                     | 8.41 ms                                                    | 8.03 ms: 1.05x faster                                                 |
| gc_traversal              | 3.98 ms                                                    | 3.82 ms: 1.04x faster                                                 |
| sqlite_synth              | 2.99 us                                                    | 2.89 us: 1.03x faster                                                 |
| chaos                     | 61.3 ms                                                    | 59.4 ms: 1.03x faster                                                 |
| logging_simple            | 5.74 us                                                    | 5.57 us: 1.03x faster                                                 |
| pidigits                  | 191 ms                                                     | 188 ms: 1.02x faster                                                  |
| bpe_tokeniser             | 5.02 sec                                                   | 4.94 sec: 1.02x faster                                                |
| pickle_pure_python        | 305 us                                                     | 301 us: 1.02x faster                                                  |
| meteor_contest            | 110 ms                                                     | 108 ms: 1.01x faster                                                  |
| json_dumps                | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                                 |
| unpickle                  | 15.1 us                                                    | 15.0 us: 1.01x faster                                                 |
| create_gc_cycles          | 1.82 ms                                                    | 1.80 ms: 1.01x faster                                                 |
| coroutines                | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                                 |
| json_loads                | 28.9 us                                                    | 28.7 us: 1.01x faster                                                 |
| sqlglot_parse             | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                 |
| comprehensions            | 16.6 us                                                    | 16.5 us: 1.01x faster                                                 |
| mdp                       | 2.79 sec                                                   | 2.77 sec: 1.01x faster                                                |
| pickle_list               | 5.11 us                                                    | 5.12 us: 1.00x slower                                                 |
| unpickle_list             | 5.34 us                                                    | 5.37 us: 1.01x slower                                                 |
| sqlglot_transpile         | 1.63 ms                                                    | 1.65 ms: 1.01x slower                                                 |
| asyncio_tcp_ssl           | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                                |
| regex_effbot              | 3.67 ms                                                    | 3.71 ms: 1.01x slower                                                 |
| thrift                    | 823 us                                                     | 833 us: 1.01x slower                                                  |
| generators                | 29.6 ms                                                    | 30.0 ms: 1.01x slower                                                 |
| scimark_sor               | 127 ms                                                     | 129 ms: 1.01x slower                                                  |
| asyncio_tcp               | 508 ms                                                     | 516 ms: 1.02x slower                                                  |
| json                      | 5.31 ms                                                    | 5.40 ms: 1.02x slower                                                 |
| tornado_http              | 94.6 ms                                                    | 96.3 ms: 1.02x slower                                                 |
| pickle_dict               | 34.8 us                                                    | 35.6 us: 1.02x slower                                                 |
| coverage                  | 93.1 ms                                                    | 95.3 ms: 1.02x slower                                                 |
| bench_thread_pool         | 834 us                                                     | 854 us: 1.02x slower                                                  |
| async_tree_cpu_io_mixed   | 611 ms                                                     | 626 ms: 1.03x slower                                                  |
| scimark_lu                | 122 ms                                                     | 125 ms: 1.03x slower                                                  |
| 2to3                      | 274 ms                                                     | 281 ms: 1.03x slower                                                  |
| dask                      | 369 ms                                                     | 379 ms: 1.03x slower                                                  |
| unpickle_pure_python      | 218 us                                                     | 224 us: 1.03x slower                                                  |
| dulwich_log               | 67.2 ms                                                    | 69.1 ms: 1.03x slower                                                 |
| go                        | 145 ms                                                     | 149 ms: 1.03x slower                                                  |
| sqlglot_optimize          | 55.5 ms                                                    | 57.2 ms: 1.03x slower                                                 |
| python_startup            | 10.8 ms                                                    | 11.1 ms: 1.04x slower                                                 |
| sqlglot_normalize         | 110 ms                                                     | 115 ms: 1.04x slower                                                  |
| regex_dna                 | 221 ms                                                     | 230 ms: 1.04x slower                                                  |
| typing_runtime_protocols  | 165 us                                                     | 171 us: 1.04x slower                                                  |
| django_template           | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                                 |
| genshi_text               | 23.7 ms                                                    | 24.7 ms: 1.05x slower                                                 |
| docutils                  | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                |
| raytrace                  | 267 ms                                                     | 279 ms: 1.05x slower                                                  |
| async_tree_memoization_tg | 444 ms                                                     | 466 ms: 1.05x slower                                                  |
| logging_silent            | 105 ns                                                     | 110 ns: 1.05x slower                                                  |
| hexiom                    | 6.30 ms                                                    | 6.68 ms: 1.06x slower                                                 |
| pickle                    | 11.5 us                                                    | 12.2 us: 1.06x slower                                                 |
| async_tree_memoization    | 463 ms                                                     | 493 ms: 1.06x slower                                                  |
| async_generators          | 442 ms                                                     | 471 ms: 1.07x slower                                                  |
| sympy_str                 | 282 ms                                                     | 301 ms: 1.07x slower                                                  |
| nqueens                   | 81.4 ms                                                    | 86.8 ms: 1.07x slower                                                 |
| python_startup_no_site    | 7.11 ms                                                    | 7.63 ms: 1.07x slower                                                 |
| sympy_expand              | 473 ms                                                     | 508 ms: 1.07x slower                                                  |
| async_tree_io_tg          | 936 ms                                                     | 1.01 sec: 1.08x slower                                                |
| genshi_xml                | 51.6 ms                                                    | 56.3 ms: 1.09x slower                                                 |
| sympy_integrate           | 20.5 ms                                                    | 22.6 ms: 1.10x slower                                                 |
| sympy_sum                 | 156 ms                                                     | 172 ms: 1.10x slower                                                  |
| pylint                    | 317 ms                                                     | 353 ms: 1.11x slower                                                  |
| deltablue                 | 3.25 ms                                                    | 3.69 ms: 1.14x slower                                                 |
| Geometric mean            | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (9): async_tree_none, async_tree_cpu_io_mixed_tg, regex_compile, html5lib, asyncio_websockets, pycparser, bench_mp_pool, async_tree_io, async_tree_none_tg
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 72.42% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x