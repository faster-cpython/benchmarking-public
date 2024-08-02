# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_align
- machine: linux-x86_64
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.01x faster
- HPT reliability: 75.58%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 280 ms: 1.02x slower                                                |
| chameleon      | 7.22 ms                                                    | 7.07 ms: 1.02x faster                                               |
| docutils       | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                              |
| html5lib       | 67.2 ms                                                    | 68.0 ms: 1.01x slower                                               |
| tornado_http   | 94.6 ms                                                    | 96.8 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                      | 1.02x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 80.3 ms: 1.10x faster                                               |
| float          | 78.9 ms                                                    | 72.3 ms: 1.09x faster                                               |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                      | 1.07x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 138 ms: 1.01x slower                                                |
| regex_v8       | 25.1 ms                                                    | 25.7 ms: 1.02x slower                                               |
| regex_dna      | 221 ms                                                     | 230 ms: 1.04x slower                                                |
| regex_effbot   | 3.67 ms                                                    | 3.94 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                      | 1.04x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                              |
| xml_etree_parse      | 162 ms                                                     | 151 ms: 1.07x faster                                                |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.07x faster                                                |
| xml_etree_generate   | 87.4 ms                                                    | 82.8 ms: 1.06x faster                                               |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                               |
| xml_etree_process    | 61.2 ms                                                    | 58.6 ms: 1.04x faster                                               |
| pickle_pure_python   | 305 us                                                     | 297 us: 1.03x faster                                                |
| unpickle_list        | 5.34 us                                                    | 5.28 us: 1.01x faster                                               |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                               |
| pickle_dict          | 34.8 us                                                    | 34.6 us: 1.01x faster                                               |
| pickle_list          | 5.11 us                                                    | 5.08 us: 1.00x faster                                               |
| unpickle_pure_python | 218 us                                                     | 220 us: 1.01x slower                                                |
| pickle               | 11.5 us                                                    | 11.8 us: 1.02x slower                                               |
| unpickle             | 15.1 us                                                    | 15.8 us: 1.04x slower                                               |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.9 ms: 1.02x slower                                               |
| python_startup_no_site | 7.11 ms                                                    | 7.61 ms: 1.07x slower                                               |
| Geometric mean         | (ref)                                                      | 1.04x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.00 ms: 1.12x faster                                              |
| genshi_text     | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                               |
| django_template | 34.8 ms                                                    | 36.9 ms: 1.06x slower                                               |
| genshi_xml      | 51.6 ms                                                    | 58.2 ms: 1.13x slower                                               |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                        |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|--------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| scimark_fft              | 392 ms                                                     | 314 ms: 1.25x faster                                                |
| richards                 | 50.9 ms                                                    | 41.6 ms: 1.22x faster                                               |
| richards_super           | 57.4 ms                                                    | 47.3 ms: 1.21x faster                                               |
| spectral_norm            | 116 ms                                                     | 99.5 ms: 1.17x faster                                               |
| fannkuch                 | 402 ms                                                     | 350 ms: 1.15x faster                                                |
| crypto_pyaes             | 77.5 ms                                                    | 67.5 ms: 1.15x faster                                               |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.59 ms: 1.15x faster                                               |
| mako                     | 11.2 ms                                                    | 10.00 ms: 1.12x faster                                              |
| scimark_monte_carlo      | 69.2 ms                                                    | 62.1 ms: 1.11x faster                                               |
| pyflate                  | 484 ms                                                     | 437 ms: 1.11x faster                                                |
| nbody                    | 88.3 ms                                                    | 80.3 ms: 1.10x faster                                               |
| float                    | 78.9 ms                                                    | 72.3 ms: 1.09x faster                                               |
| tomli_loads              | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                              |
| mdp                      | 2.79 sec                                                   | 2.59 sec: 1.08x faster                                              |
| xml_etree_parse          | 162 ms                                                     | 151 ms: 1.07x faster                                                |
| pprint_pformat           | 1.56 sec                                                   | 1.45 sec: 1.07x faster                                              |
| pprint_safe_repr         | 758 ms                                                     | 711 ms: 1.07x faster                                                |
| xml_etree_iterparse      | 107 ms                                                     | 101 ms: 1.07x faster                                                |
| xml_etree_generate       | 87.4 ms                                                    | 82.8 ms: 1.06x faster                                               |
| sqlite_synth             | 2.99 us                                                    | 2.85 us: 1.05x faster                                               |
| json_dumps               | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                               |
| xml_etree_process        | 61.2 ms                                                    | 58.6 ms: 1.04x faster                                               |
| pathlib                  | 17.3 ms                                                    | 16.7 ms: 1.04x faster                                               |
| deepcopy_memo            | 39.7 us                                                    | 38.3 us: 1.04x faster                                               |
| chaos                    | 61.3 ms                                                    | 59.3 ms: 1.03x faster                                               |
| logging_format           | 6.47 us                                                    | 6.26 us: 1.03x faster                                               |
| telco                    | 8.41 ms                                                    | 8.16 ms: 1.03x faster                                               |
| gc_traversal             | 3.98 ms                                                    | 3.86 ms: 1.03x faster                                               |
| pickle_pure_python       | 305 us                                                     | 297 us: 1.03x faster                                                |
| logging_simple           | 5.74 us                                                    | 5.62 us: 1.02x faster                                               |
| chameleon                | 7.22 ms                                                    | 7.07 ms: 1.02x faster                                               |
| pidigits                 | 191 ms                                                     | 188 ms: 1.02x faster                                                |
| meteor_contest           | 110 ms                                                     | 108 ms: 1.02x faster                                                |
| json                     | 5.31 ms                                                    | 5.22 ms: 1.02x faster                                               |
| sqlglot_parse            | 1.32 ms                                                    | 1.30 ms: 1.02x faster                                               |
| unpickle_list            | 5.34 us                                                    | 5.28 us: 1.01x faster                                               |
| json_loads               | 28.9 us                                                    | 28.6 us: 1.01x faster                                               |
| coroutines               | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                               |
| pickle_dict              | 34.8 us                                                    | 34.6 us: 1.01x faster                                               |
| pickle_list              | 5.11 us                                                    | 5.08 us: 1.00x faster                                               |
| create_gc_cycles         | 1.82 ms                                                    | 1.82 ms: 1.00x slower                                               |
| bench_mp_pool            | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                               |
| unpickle_pure_python     | 218 us                                                     | 220 us: 1.01x slower                                                |
| regex_compile            | 137 ms                                                     | 138 ms: 1.01x slower                                                |
| comprehensions           | 16.6 us                                                    | 16.8 us: 1.01x slower                                               |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                              |
| html5lib                 | 67.2 ms                                                    | 68.0 ms: 1.01x slower                                               |
| deepcopy                 | 367 us                                                     | 372 us: 1.01x slower                                                |
| scimark_sor              | 127 ms                                                     | 129 ms: 1.02x slower                                                |
| python_startup           | 10.8 ms                                                    | 10.9 ms: 1.02x slower                                               |
| go                       | 145 ms                                                     | 147 ms: 1.02x slower                                                |
| sqlglot_optimize         | 55.5 ms                                                    | 56.4 ms: 1.02x slower                                               |
| logging_silent           | 105 ns                                                     | 107 ns: 1.02x slower                                                |
| 2to3                     | 274 ms                                                     | 280 ms: 1.02x slower                                                |
| sqlglot_normalize        | 110 ms                                                     | 113 ms: 1.02x slower                                                |
| dask                     | 369 ms                                                     | 377 ms: 1.02x slower                                                |
| flaskblogging            | 9.01 ms                                                    | 9.21 ms: 1.02x slower                                               |
| tornado_http             | 94.6 ms                                                    | 96.8 ms: 1.02x slower                                               |
| regex_v8                 | 25.1 ms                                                    | 25.7 ms: 1.02x slower                                               |
| typing_runtime_protocols | 165 us                                                     | 169 us: 1.02x slower                                                |
| pickle                   | 11.5 us                                                    | 11.8 us: 1.02x slower                                               |
| asyncio_tcp              | 508 ms                                                     | 522 ms: 1.03x slower                                                |
| dulwich_log              | 67.2 ms                                                    | 69.1 ms: 1.03x slower                                               |
| scimark_lu               | 122 ms                                                     | 126 ms: 1.03x slower                                                |
| raytrace                 | 267 ms                                                     | 276 ms: 1.03x slower                                                |
| bench_thread_pool        | 834 us                                                     | 864 us: 1.04x slower                                                |
| pycparser                | 1.16 sec                                                   | 1.20 sec: 1.04x slower                                              |
| genshi_text              | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                               |
| regex_dna                | 221 ms                                                     | 230 ms: 1.04x slower                                                |
| generators               | 29.6 ms                                                    | 30.9 ms: 1.04x slower                                               |
| unpickle                 | 15.1 us                                                    | 15.8 us: 1.04x slower                                               |
| hexiom                   | 6.30 ms                                                    | 6.58 ms: 1.05x slower                                               |
| docutils                 | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                              |
| async_generators         | 442 ms                                                     | 463 ms: 1.05x slower                                                |
| nqueens                  | 81.4 ms                                                    | 85.4 ms: 1.05x slower                                               |
| django_template          | 34.8 ms                                                    | 36.9 ms: 1.06x slower                                               |
| sympy_str                | 282 ms                                                     | 301 ms: 1.07x slower                                                |
| python_startup_no_site   | 7.11 ms                                                    | 7.61 ms: 1.07x slower                                               |
| regex_effbot             | 3.67 ms                                                    | 3.94 ms: 1.07x slower                                               |
| sympy_expand             | 473 ms                                                     | 509 ms: 1.08x slower                                                |
| sympy_integrate          | 20.5 ms                                                    | 22.4 ms: 1.09x slower                                               |
| sympy_sum                | 156 ms                                                     | 171 ms: 1.10x slower                                                |
| pylint                   | 317 ms                                                     | 353 ms: 1.11x slower                                                |
| genshi_xml               | 51.6 ms                                                    | 58.2 ms: 1.13x slower                                               |
| deltablue                | 3.25 ms                                                    | 3.73 ms: 1.15x slower                                               |
| Geometric mean           | (ref)                                                      | 1.01x faster                                                        |

Benchmark hidden because not significant (13): deepcopy_reduce, coverage, async_tree_cpu_io_mixed_tg, async_tree_none_tg, sqlglot_transpile, async_tree_memoization_tg, thrift, asyncio_websockets, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none, async_tree_io
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2

# HPT report

- Reliability score: 75.58% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x